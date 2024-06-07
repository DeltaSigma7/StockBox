from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from tkinter import ttk
import mysql.connector
import configparser
import sqlite3
import os
from PIL import Image
from CTkKeyboard import keyboard
from tkinter import filedialog
import pandas as pd


def config_info():
    config = configparser.ConfigParser()
    try:
        config.read('config.ini')
        sql_host = config.get('Database', 'host')
        sql_port = config.get('Database', 'port')
        sql_user = config.get('Database', 'username')
        sql_password = config.get('Database', 'password')

        keyboard_enabled = config.get('Setup', 'virtual_keyboard')
        local_db_enabled = config.get('Setup','local_db')
        dark_theme = config.get('Setup', 'dark_theme')
        theme_color = config.get('Setup', 'color_theme')
        keyboard_layout = config.get('Setup', 'keyboard_layout')
        return sql_host, sql_port, sql_user, sql_password, keyboard_enabled, local_db_enabled, dark_theme, theme_color, keyboard_layout
    except configparser.NoSectionError:
        return 'No file found'
   
def confirm_messagebox(text):
    try:
        CTkMessagebox(title="Info", message=text, icon="Img/check.png")
    except FileNotFoundError:
        CTkMessagebox(title="Info", message=text, icon="")

def error_messagebox(text):
    try:
        CTkMessagebox(title="Error", message=text, icon="Img/cancel.png")
    except FileNotFoundError:
        CTkMessagebox(title="Error", message=text, icon="")

def choice_messagebox(text):
    try:
        msg = CTkMessagebox(title="", message=text,
                  icon="Img/choice.png", option_1="No", option_2="Yes")
    except FileNotFoundError:
        msg = CTkMessagebox(title="", message=text,
                  icon="", option_1="No", option_2="Yes")
 
    if msg.get() == None:
        return False
    elif msg.get() == "Yes":
        return True
    else:
        return False

def check_trigger():
    
    pointer.execute("SELECT Count FROM Stockbox WHERE Deleted = 0;")
    counts = [row[0] for row in pointer.fetchall()]  
    

    pointer.execute("SELECT Trigger_Count FROM Stockbox WHERE Deleted = 0;")
    triggers = [row[0] for row in pointer.fetchall()]

    
    trigger_list = []
    for i, count in enumerate(counts):
      if count <= triggers[i]:
          
          pointer.execute(f"SELECT ID from Stockbox Where count = {count} AND trigger_count = {triggers[i]};")
          trigger_list.append(pointer.fetchone()[0])
    if len(trigger_list) == 0:
        pass
    else:
        trigger_toplevel = ctk.CTkToplevel()
        trigger_toplevel.title("Trigger Alert")
        trigger_toplevel.attributes("-topmost", True)
        trigger_toplevel.resizable(False,False)
        trigger_toplevel.rowconfigure(0, weight=1)
        trigger_toplevel.columnconfigure(0, weight=1)
        window_size = screen_height /2.5
        font_size = trigger_toplevel.winfo_height() / 15

        x = (screen_width/2) - (window_size/2)
        y = (screen_height/2) - (window_size/2)
        trigger_toplevel.geometry('%dx%d+%d+%d' % (window_size, window_size, x, y))
    
        scroll_frame = ctk.CTkScrollableFrame(trigger_toplevel)
        scroll_frame.grid(row=0, column= 0, padx=10, pady=10, sticky="nsew")
        scroll_frame.rowconfigure(0, weight=1)
        scroll_frame.columnconfigure(0, weight=1)

        conf_bttn= ctk.CTkButton(trigger_toplevel, text="OK", font=("Arial", font_size, "bold"), text_color="black", command=trigger_toplevel.destroy)
        conf_bttn.grid(row= 1, column=0, pady=10, padx=10, sticky="nsew")

        name_list = []
        for id in trigger_list:
            pointer.execute(f"SELECT Name FROM Stockbox where id like {id} ORDER BY Id ASC;")
            name_list.append(pointer.fetchone()[0])

        row= 0


        for item in name_list:
            label = ctk.CTkLabel(scroll_frame, text=f' "{item}" has reached the triggered amount', font=("Arial", font_size, "bold"), justify="center")
            label.grid(row=row, column=0, pady=(0,5), padx=10, sticky="nsew")
            label.columnconfigure(0, weight=1)
            row += 1

def edit_event_frame():
    
    
    event_frame.rowconfigure(0, weight=1)
    event_frame.rowconfigure(2, weight=1)
    event_frame.columnconfigure(0, weight=1)
    event_frame.columnconfigure(2, weight=1)

    if int(config_data[6]):
        if str(config_data[7]) == "blue":
            try:
                logo_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Logo.png")), size=(500,500))
                view_logo = ctk.CTkLabel(event_frame, text="", image=logo_img)
            except Exception:
                view_logo = ctk.CTkLabel(event_frame, text="")
        elif str(config_data[7]) == "green":
            try:
                logo_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Logo_green.png")), size=(500,500))
                view_logo = ctk.CTkLabel(event_frame, text="", image=logo_img)
            except Exception:
                view_logo = ctk.CTkLabel(event_frame, text="")
    else:
        try:
            logo_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Logo_light.png")), size=(500,500))
            view_logo = ctk.CTkLabel(event_frame, text="", image=logo_img)
        except Exception:
            view_logo = ctk.CTkLabel(event_frame, text="")
    
    
    

    view_logo.grid(row=1, column=1, sticky="nsew")
    
def remove_event_frames():
    for i in range(9):
        event_frame.grid_rowconfigure(i, weight=0) 
        event_frame.grid_columnconfigure(i, weight=0)
    for widget in event_frame.winfo_children():
        widget.grid_forget()

def add_take(id_value):
    global add_take_open_var
    
    id = id_value
    def add_item():
        global add_take_open_var, keyboard_open
        entry.unbind("<FocusIn>")
        number = entry.get()
        try: 
            number = int(number)
        except ValueError:
            error_messagebox(text="Count must be a number")
        else:
            pointer.execute(f"SELECT Count FROM Stockbox WHERE ID LIKE {id};")
            count = int(pointer.fetchone()[0])
            number = number + count
            try:
                pointer.execute(f"UPDATE Stockbox set Count = {number} WHERE Id = {id};")
                con.commit()
            except Exception as error:
                error_messagebox(f"Couldn't update Database \n {error}")
            add_take_open_var = 0
            entry.unbind("<FocusIn>")
            add_win.destroy()
            confirm_messagebox(text="Count successfully updated")
            keyboard_open = False
            search_menu()
       
    def remove_item():
        global add_take_open_var,keyboard_open
        entry.unbind("<FocusIn>")
        number = entry.get()
        try: 
            number = int(number)
        except ValueError:
            error_messagebox(text="Count must be a number")
        else:
            pointer.execute(f"SELECT Count FROM Stockbox WHERE ID LIKE {id};")
            count = int(pointer.fetchone()[0])
            number = count - number
            pointer.execute(f"UPDATE Stockbox set Count = {number} WHERE Id = {id};")
            con.commit()
            try:
                pointer.execute(f"UPDATE Stockbox set Count = {number} WHERE Id = {id};")
                con.commit()
            except Exception as error:
                error_messagebox(f"Couldn't update Database \n {error}")
            add_take_open_var = 0
            entry.unbind("<FocusIn>")
            add_win.destroy()
            confirm_messagebox(text="Count successfully updated")
            keyboard_open = False
            search_menu()
   
    def delete_item():
        global add_take_open_var, keyboard_open
        pointer.execute(f"UPDATE Stockbox set Deleted = 1 WHERE Id = {id};")
        con.commit()
        try:
            pointer.execute(f"UPDATE Stockbox set Count = {number} WHERE Id = {id};")
            con.commit()
        except Exception as error:
            error_messagebox(f"Couldn't update Database \n {error}")
        add_take_open_var = 0
        entry.unbind("<FocusIn>")
        add_win.destroy()
        confirm_messagebox(text="Count successfully updated")
        keyboard_open = False
        search_menu()


    if add_take_open_var == 0:
        pointer.execute(f"SELECT Deleted FROM Stockbox WHERE id = {id};")
        del_var = pointer.fetchone()[0]
        pointer.fetchall()
        if del_var == 0:

            add_take_open_var =+ 1
            font_size = screen_height / 40
            add_win = ctk.CTkToplevel(app)
            add_win.title("Add or Remove")
            add_win.attributes("-topmost", True)
            add_win.resizable(False,False)
            #change for PI
            window_size = screen_height 

            x = (screen_width/2) - (window_size/2)
            y = (screen_height/2) - (window_size/2)
            add_win.geometry('%dx%d+%d+%d' % (window_size, window_size/2, x, y))
            add_win.rowconfigure((0,1,2,3,4,5), weight=1)
            add_win.columnconfigure((0,1,2,3), weight=1)
            
            entry = ctk.CTkEntry(add_win, placeholder_text="Count", justify="center", font=("Arial", font_size, "bold"))
            entry.grid(row= 0, column= 1, columnspan=2, pady= 10, sticky="nsew", rowspan=4)
            include_button = ctk.CTkButton(add_win,text="Add", font=("Arial", font_size, "bold"), height=40, text_color="black", command=add_item)
            include_button.grid(row=4, column=1, padx=(0,20), pady= 10, sticky="nsew")
            takeout_button = ctk.CTkButton(add_win, text="Remove", font=("Arial", font_size, "bold"), height=40, text_color="black", command=remove_item)
            takeout_button.grid(row=4, column=2, padx=(20,0), pady= 10, sticky="nsew")
            del_bttn = ctk.CTkButton(add_win,text="Delete Entry", font=("Arial", font_size, "bold"), height=40, text_color="black", command=delete_item)
            del_bttn.grid(row=5, column=1, pady= 10, sticky="nsew", columnspan=2)
            if int(config_data[4]):
                def focus_in(event):
                    global keyboard_open
                    if not keyboard_open:
                        keyboard_open = True
                        try:
                            keyboard(app, entry, str(config_data[8]))
                        except Exception as error:
                            print(error)

                entry.bind("<FocusIn>", focus_in)
                
        else:
            msg = choice_messagebox(text="Do you want to restore the entry?")            
    
            if msg:
                pointer.execute(f"UPDATE Stockbox set Deleted = 0 WHERE Id = {id};")
                con.commit()
                add_take_open_var = 0
                confirm_messagebox(text="Entry successfully restored") 
                search_menu()    
            else:
                pass
    else:
        pass

def item_selected(event=None):
    try:
        selected_item = tree.selection()[0]
        id_value = int(selected_item)  # Using the iid as the ID
    except (IndexError, ValueError):
        pass
    else:
        add_take(id_value)
           
def search_menu():
    global tree
    global search_bar
    remove_event_frames()
    check_trigger()
    event_frame.columnconfigure(0, weight=1)
    event_frame.rowconfigure(1, weight=9)
    event_frame.rowconfigure(2, weight=1)
    headline_size = app.winfo_height() / 25
    column_size = app.winfo_height() / 35

    
    def search_in_database():
            count=0
            for item in tree.get_children():
                tree.delete(item)
            search=search_bar.get()
            if search[0:2] == "D:":
                search = "%"+ search[2:] + "%"
                pointer.execute(f"SELECT ID, Name, Depot, Count, Descript FROM Stockbox WHERE Depot like '{search}' and Deleted = 0 order by ID asc;")
            elif search == "":
                pointer.execute(f"SELECT ID, Name, Depot, Count, Descript FROM Stockbox WHERE Deleted = 0 order by ID asc;")
            elif search.lower() == "deleted":
                pointer.execute(f"SELECT ID, Name, Depot, Count, Descript FROM Stockbox WHERE Deleted = 1 order by ID asc;")

            else:
                search = search.split(" ")
                z = 0
                for w in search:
                    search[z] = "%" + w
                    z += 1
                search = "".join(map(str, search))
                search = search +'%'
                pointer.execute(f"SELECT ID, Name, Depot, Count, Descript FROM Stockbox WHERE Tags like '{search}' and Deleted = 0 order by ID asc;")
            
            for record in pointer.fetchall():
                tree.insert(parent="", index="end", iid=record[0], values=(record[1], record[2], record[3], record[4]))
                count += 1
            count = 0


    font_size = app.winfo_height() / 20
    search_bar = ctk.CTkEntry(event_frame, placeholder_text="Search", justify="center", font=("Arial", font_size, "bold"), height=40)
    search_bar.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
    search_bar.columnconfigure(0, weight=1)
    search_bttn =ctk.CTkButton(event_frame, text="Search", font=("Arial", font_size, "bold"), height=40, text_color="black", command=search_in_database)
    search_bttn.grid(row=0, column=1, pady=(10,0), padx=(0,10), sticky="ew")

    output_frame = ctk.CTkScrollableFrame(event_frame)
    output_frame.grid(row=1, column=0, sticky="nsew", columnspan=2, pady=(10,0))
    output_frame.columnconfigure(0, weight=1)

    bottom_frame = ctk.CTkFrame(event_frame)
    bottom_frame.grid(row=2, column=0, sticky="nsew", columnspan=2, pady=(10,0))
    bottom_frame.columnconfigure(0, weight=1)
    bottom_frame.rowconfigure((0,1,2), weight=1)

    search_bar.bind("<Return>",lambda e: search_in_database())
    if int(config_data[4]):
        search_bar.bind("<FocusIn>", lambda e: keyboard(app, search_bar,str(config_data[8])))

    if str(config_data[7]) == "blue":
        heading_active_bg = "3484f0"
        fg_color = "#1f6aa5"
        selected_color = "#22559b"

    elif str(config_data[7]) == "green":
        heading_active_bg = "#2cc985" 
        fg_color = "black"
        selected_color = "#0a934b"
    
    if int(config_data[6]):
        if str(config_data[7]) == "green":
            fg_color = "#0a934b"
        bg_color = "#333333"
        fieldbg_color = "#333333"
        border_color = "#333333"
        heading_bg_color = "#565b5e"
        heading_fg_color = "black"
        
    else:
        bg_color = "#cfcfcf"
        fieldbg_color = "#cfcfcf"
        border_color = "#cfcfcf"
        heading_bg_color = "#8d8d8d"
        heading_fg_color = "black"



    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background=bg_color, foreground=fg_color, fieldbackground=fieldbg_color, rowheight=int(column_size * 2),bordercolor=border_color, borderwidth=0, font=("Arial", int(column_size), "bold"))
    style.map("Treeview", background=[("selected", selected_color)])
    style.configure("Treeview.Heading", background=heading_bg_color, foreground=heading_fg_color, relief="flat", font=("Arial", int(headline_size), "bold"))
    style.map("Treeview.Heading", background=[("active", heading_active_bg)])
    output_frame.rowconfigure((0,1,2), weight=1)

    tree = ttk.Treeview(output_frame)
    tree["columns"] = ("Name", "Depot", "Count", "Description")
 
    tree.column("#0", width=0, stretch=ctk.NO)
    #tree.column("ID", anchor="center", width=80)
    tree.column("Name", anchor="center", width=120)
    tree.column("Depot", anchor="center", width=80)
    tree.column("Count", anchor="center", width=80)
    tree.column("Description", anchor="center", width=200)
    
    tree.heading("#0", text="", anchor="center")
    #tree.heading("ID", text="ID", anchor="center")
    tree.heading("Name", text="Name", anchor="center") 
    tree.heading("Depot", text="Depot", anchor="center")
    tree.heading("Count", text="Count", anchor="center")
    tree.heading("Description", text="Description", anchor="center")
    tree.grid(row=0, column=0,rowspan=2, sticky="nsew")


    bttn = ctk.CTkButton(bottom_frame, text="Select", font=("Arial", font_size, "bold"), height=40, text_color="black", command=item_selected)
    bttn.grid(row=1, column=0, sticky="sew")

def add_menu():

    def include():
        name = name_entry.get()
        count = count_entry.get()
        depot = depot_entry.get()
        tags = tags_entry.get()
        desc = desc_entry.get()
        trigger = trigger_entry.get()

        
        if not name or not count or not depot or not tags or not desc or not trigger:
            error_messagebox(text="Please fill out all required fields")
        else:
            try:
                count = int(count)
                trigger = int(trigger)
            except ValueError:
                error_messagebox(text="Count and Trigger must be a number")
            else:
                try:
                    pointer.execute(f"INSERT INTO Stockbox (Name, Count, Depot, Tags, Descript, Trigger_count) VALUES ('{name}',{count},'{depot}','{tags}','{desc}',{trigger});")
                    con.commit()
      
                except Exception as error:
                    error_messagebox(f"Couldn't update Database \n {error}")
                confirm_messagebox(text="Entry successfully added") 
                add_menu()

    remove_event_frames()
    font_size = app.winfo_height() / 15
  
    event_frame.columnconfigure(0, weight=1)
    for i in range (9):
        event_frame.rowconfigure(i, weight=1)

    name_entry = ctk.CTkEntry(event_frame, placeholder_text="Name", justify="center", font=("Arial", font_size, "bold"), height=40)
    count_entry = ctk.CTkEntry(event_frame, placeholder_text="Count", justify="center", font=("Arial", font_size, "bold"), height=40)
    depot_entry = ctk.CTkEntry(event_frame, placeholder_text="Depot", justify="center", font=("Arial", font_size, "bold"), height=40)
    tags_entry = ctk.CTkEntry(event_frame, placeholder_text="Tags", justify="center", font=("Arial", font_size, "bold"), height=40)
    desc_entry = ctk.CTkEntry(event_frame, placeholder_text="Description", justify="center", font=("Arial", font_size, "bold"), height=40)
    trigger_entry = ctk.CTkEntry(event_frame, placeholder_text="Trigger", justify="center", font=("Arial", font_size, "bold"), height=40)

    name_entry.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    name_entry.columnconfigure(0, weight=1)
    count_entry.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    count_entry.columnconfigure(0, weight=1)
    depot_entry.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    depot_entry.columnconfigure(0, weight=1)
    tags_entry.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
    tags_entry.columnconfigure(0, weight=1)
    desc_entry.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
    desc_entry.columnconfigure(0, weight=1)
    trigger_entry.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
    trigger_entry.columnconfigure(0, weight=1)
    if int(config_data[4]):
        name_entry.bind("<FocusIn>", lambda e: keyboard(app,name_entry,str(config_data[8])))
        count_entry.bind("<FocusIn>", lambda e: keyboard(app,count_entry,str(config_data[8])))
        depot_entry.bind("<FocusIn>", lambda e: keyboard(app,depot_entry,str(config_data[8])))
        tags_entry.bind("<FocusIn>", lambda e: keyboard(app,tags_entry,str(config_data[8])))
        desc_entry.bind("<FocusIn>", lambda e: keyboard(app,desc_entry,str(config_data[8])))
        trigger_entry.bind("<FocusIn>", lambda e: keyboard(app,trigger_entry,str(config_data[8])))

    include_button = ctk.CTkButton(event_frame, text="Include", font=("Arial", font_size, "bold"),text_color="black" ,command=include)
    include_button.grid(row=6, column=0, padx=10, pady=(30,10), sticky="nsew")

 

    
    event_frame.rowconfigure(6, weight=1) 

def excle_to_db():
    if choice_messagebox("Replace current entries with Excel values? There is no way back!!!"):
        file_path = filedialog.askopenfilename(
        title="Select an Excel File",
        filetypes=[("Excel files", "*.xlsx")]
        )
        if file_path:
            try:
                df = pd.read_excel(file_path)

                pointer.execute('DROP TABLE IF EXISTS Stockbox')

                # Create a new table with the specified schema
                if int(config_data[5]):
                    pointer.execute('''CREATE TABLE IF NOT EXISTS Stockbox (
                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        Name TEXT,
                                        Count INTEGER NOT NULL DEFAULT 0,
                                        Depot TEXT,
                                        Tags TEXT, 
                                        Descript TEXT, 
                                        Trigger_count INTEGER NOT NULL DEFAULT 0, 
                                        Deleted BOOLEAN NOT NULL DEFAULT 0
                                    );''')
                    for _, row in df.iterrows():
                        try:
                            count_value = int(row['Count'])
                        except ValueError:
                            count_value = 0  # Default value if conversion fails

                        try:
                            trigger_value = int(row['Trigger_count'])
                        except ValueError:
                            trigger_value = 0  # Default value if conversion fails

                        pointer.execute('''
                        INSERT INTO Stockbox (Name, Count, Depot, Tags, Descript, Trigger_count)
                        VALUES (?, ?, ?, ?, ?, ?)
                        ''', (row['Name'], count_value, row['Depot'], row['Tags'], row['Descript'], trigger_value))

                    con.commit()
                    confirm_messagebox("Database successfully updated")
                else:
                    pointer.execute('''CREATE TABLE IF NOT EXISTS Stockbox (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        Name TEXT,
                        Count INT NOT NULL DEFAULT 0,
                        Depot TEXT,
                        Tags TEXT, 
                        Descript TEXT, 
                        Trigger_count INT NOT NULL DEFAULT 0, 
                        Deleted BOOLEAN NOT NULL DEFAULT 0
                    );''')
                    for _, row in df.iterrows():
                        try:
                            trigger_value = int(row['Trigger_count'])
                        except ValueError:
                            trigger_value = 0  # Default value if conversion fails

                        pointer.execute('''
                        INSERT INTO Stockbox (Name, Count, Depot, Tags, Descript, Trigger_count)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ''', (row['Name'], row['Count'], row['Depot'], row['Tags'], row['Descript'], trigger_value))           
                    con.commit()
                    confirm_messagebox("Database successfully updated")
            except Exception as e:
                print(e)
                error_messagebox("Something went wrong")

        else:
            pass
    else:
        pass

def settings_menu():

    remove_event_frames()
    event_frame.grid_rowconfigure((0,2), weight=1)
    event_frame.grid_columnconfigure((0,5), weight=1)
    bttn_size = app.winfo_height()/4

    try:
        shutdown_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Shutdown_icon.png")), size=(bttn_size,bttn_size))
        reboot_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Reboot_icon.png")), size=(bttn_size,bttn_size))
        donate_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Donate_icon.png")), size=(bttn_size,bttn_size))
        import_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Import_icon.png")), size=(bttn_size,bttn_size))
        shutdown_bttn = ctk.CTkButton(event_frame, image=shutdown_img, text="", height=bttn_size, width=bttn_size, command=shutdown)
        reboot_bttn = ctk.CTkButton(event_frame, image=reboot_img, text="", height=bttn_size, width=bttn_size, command=reboot)
        donate_bttn = ctk.CTkButton(event_frame, image=donate_img, text="", height=bttn_size, width=bttn_size, command=donate)
        import_bttn = ctk.CTkButton(event_frame, image=import_img, text="", height=bttn_size, width=bttn_size, command=excle_to_db)
    except Exception:
        shutdown_bttn = ctk.CTkButton(event_frame, text="Shutdown", command=shutdown)
        reboot_bttn = ctk.CTkButton(event_frame, text="Reboot", command=reboot)
        donate_bttn = ctk.CTkButton(event_frame, text="Donate", command=donate)
        import_bttn = ctk.CTkButton(event_frame, text="Import", command=donate)

    shutdown_bttn.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    reboot_bttn.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
    donate_bttn.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")
    import_bttn.grid(row=1, column=4, padx=10, pady=10, sticky="nsew")

def donate():
    toplevel = ctk.CTkToplevel()
    toplevel.attributes("-topmost", True)
    toplevel.rowconfigure(0, weight=1)
    toplevel.rowconfigure(2, weight=1)
    toplevel.columnconfigure(0, weight=1)
    toplevel.columnconfigure(2, weight=1)
    
    window_size = screen_height /2.5

    x = (screen_width/2) - (window_size/2)
    y = (screen_height/2) - (window_size/2)
    toplevel.geometry('%dx%d+%d+%d' % (window_size, window_size, x, y))
    if int(config_data[6]):
         if str(config_data[7]) == "blue":
            try:
                qr_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "QR_code.png")), size=(window_size,window_size))
                view_qr = ctk.CTkLabel(toplevel, text="", image=qr_img)
            except Exception:
                view_qr = ctk.CTkLabel(toplevel, text="https://ko-fi.com/cadam")
         elif str(config_data[7]) == "green":
            try:
                qr_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "QR_code_green.png")), size=(window_size,window_size))
                view_qr = ctk.CTkLabel(toplevel, text="", image=qr_img)
            except Exception:
                view_qr = ctk.CTkLabel(toplevel, text="https://ko-fi.com/cadam")
             
    else:
        try:
            qr_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "QR_code_light.png")), size=(window_size,window_size))
            view_qr = ctk.CTkLabel(toplevel, text="", image=qr_img)
        except Exception:
            view_qr = ctk.CTkLabel(toplevel, text="https://ko-fi.com/cadam")

    view_qr.grid(row=1, column=1, sticky="nsew")

def shutdown():
    
    os.system("sudo shutdown now")
    #change for pi

def reboot():
    
    os.system("sudo reboot")
    #change for pi

def menu_bar():
    
    menu_frame.grid_rowconfigure((0, 1, 2), weight=1)
    try:
        search_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Search_icon.png")), size=(75,75))
        add_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Add_icon.png")), size=(75,75))
        settings_img = ctk.CTkImage(dark_image=Image.open(os.path.join("Img", "Settings_icon.png")), size=(75,75))
        search = ctk.CTkButton(menu_frame, image=search_img, text="", command=search_menu)
        add = ctk.CTkButton(menu_frame, image=add_img, text="", command=add_menu)
        settings = ctk.CTkButton(menu_frame, image=settings_img, text="", command=settings_menu)
    except Exception:
        search = ctk.CTkButton(menu_frame, text="Search", command=search_menu)
        add = ctk.CTkButton(menu_frame, text="Add", command=add_menu)
        settings = ctk.CTkButton(menu_frame, text="Settings", command=settings_menu)
        

    search.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    add.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    settings.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

app = ctk.CTk()

app.title("StockBox")
app.bind("<Escape>", lambda event: app.destroy())

config_data = config_info()

if int(config_data[6]):
    ctk.set_appearance_mode("Dark")
else:
    ctk.set_appearance_mode("Light")

ctk.set_default_color_theme(str(config_data[7]))

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


window_width = screen_width // 2
window_height = screen_height // 2
app.geometry(f"{window_width}x{window_height}+{screen_width//4}+{screen_height//4}")


app.attributes("-fullscreen", True)
#change for pi

app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=9)
app.grid_rowconfigure(0, weight=1)

menu_frame = ctk.CTkFrame(app)
menu_frame.grid(row=0, column=0, padx=(10, 0), pady=(10, 10), sticky="nsw")
event_frame = ctk.CTkFrame(app)
event_frame.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")



if int(config_data[5]):
    con = sqlite3.connect('Stockbox.db')
    pointer = con.cursor()
    pointer.execute('''CREATE TABLE IF NOT EXISTS Stockbox (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT,
                        Count INTEGER NOT NULL DEFAULT 0,
                        Depot TEXT,
                        Tags TEXT, 
                        Descript TEXT, 
                        Trigger_count INTEGER NOT NULL DEFAULT 0, 
                        Deleted BOOLEAN NOT NULL DEFAULT 0
                    );''')
    con.commit()
else:
    try:
        con = mysql.connector.connect(
            host= config_data[0],
            port= config_data[1],
            user= config_data[2],
            password= config_data[3]
        )

        pointer = con.cursor()
    except Exception as error:
        error_messagebox(f"Couldn't connect to Database \n {error}")
    try:
        pointer.execute("USE Stockbox")
    except mysql.connector.errors.ProgrammingError:
        pointer.execute("CREATE DATABASE IF NOT EXISTS Stockbox")
        pointer.execute("USE Stockbox")
        con.commit()

    pointer.execute('''CREATE TABLE IF NOT EXISTS Stockbox (
                        ID INT AUTO_INCREMENT PRIMARY KEY,
                        Name TEXT,
                        Count INT NOT NULL DEFAULT 0,
                        Depot TEXT,
                        Tags TEXT, 
                        Descript TEXT, 
                        Trigger_count INT NOT NULL DEFAULT 0, 
                        Deleted BOOLEAN NOT NULL DEFAULT 0
                    );''')
    con.commit()
add_take_open_var = 0
keyboard_open = False

menu_bar()
edit_event_frame()

app.mainloop()

