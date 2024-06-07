# Stockbox
Stockbox is a comprehensive inventory management program designed specifically for hobbyists. 
Whether you're managing your collection of model trains, DIY electronics components, or any other hobby materials, Stockbox provides an easy and efficient way to keep track of your inventory.
---
## Features
- Simple and intuitive interface for easy inventory management
- Support for categorizing and tagging items to keep your collection organized
- Convert `.xlsx` file to database to keep the setup fast
- Detailed item descriptions, including quantity, storage location, and additional notes
- Alerts for low stock levels to ensure you never run out of essential items
- Separate menu for adding entries to keep your system up to date
- User-friendly interface with light and dark themes, featuring blue or green designs.
---
## Quick Setup Guide

This is the quick installation guide! I know, nobody reads the entire `ReadMe.md` file (but it's highly recommended!). Here's a short version to get you started:

### Windows

1. **Download & Unzip**
   - Download the latest release and unzip it to your preferred directory.

2. **Edit `config.ini`**
   - Open the `config.ini` file and update the settings.

3. **Start StockBox**
   - Launch **StockBox** and import your `.xlsx` file to quickly set up the database.

4. **You're All Set!**
   - Your setup is complete, and you're ready to go!

---

## Installation

### Windows setup

#### 1. Download & Extract

- **Download**: Get the latest release (`StockBox_V_XX.zip`) from the [releases page](1).
- **Extract**: Unzip all the files and move the folder to your preferred directory.
  - **Tip**: Avoid using `Program` or `Program Files (x86)` to sidestep administrative issues.

#### 2. Adjust the `config.ini` File

- **Locate**: Open the `config.ini` file in the project folder.
- **Configure**: Update the settings to match your environment and preferences. Ensure all required fields, such as database connection details and virtual keyboard settings, are correctly set up.
  - **More Info**: Detailed configuration instructions are provided below.

#### 3. You're Done!

- **Run**: With the folder moved and `config.ini` configured, your setup is complete!
  - **Tip**: Create a desktop shortcut for easier access.


### Linux

#### 1. Update system

- **Update** :Update your system, this may take some time.
```bash
sudo apt-get update
sudo apt-get dist-upgrade -y
```

#### 2. Install TKinter 
- **Install**: Install the Tkinter library for Python.
```bash
sudo apt install python3-tk
```

#### 3. Download package
- **Download**: Open terminal and download latest version of **StockBox**.
```bash
git clone https://github.com/CadamTechnology/StockBox
```  

#### 4. Install requirements
- **Navigate**: Move to the **StockBox** folder.
```bash
cd StockBox/StockBox
```
-**Install**: Install the required dependencies.
```bash
pip install -r requirments.txt
``` 

#### 5. Edit `config.ini`
- **Adjust**: Open the `config.ini` file to update the settings.
```bash
nano ~/StockBox/StockBox/config.ini
``` 
- **Save**: After making adjustments, save the changes by pressing <kbd>CTRL</kbd> + <kbd>S</kbd>, then exit the file by pressing <kbd>CTRL</kbd> + <kbd>X</kbd>.

#### 6. Test run
- **Run**: First navigate to stored location and run the `StockBox_Pi.py` file. if U don't move to the dicatrory you will get some Errors.
```bash
cd ~/StockBox/StockBox/
pyhton3 StockBox_Pi.py
``` 


4. Adjust the config.ini File
-----------------------------
Open the `config.ini` file with "sudo nano config.ini". Update the configuration settings according to your environment and preferences. 
Ensure that all required fields are correctly set up, such as database connection details, virtual keyboard settings, etc.

5. Test run
-----------
Move to the project folder and test run the python code with "python StockBox_Pi.py" 
If you don't move to the folder first, the images maybe won't be displayed. 
The main stockbox window should now appear without any issues.
It could be you get an error from the Pillow libary, if that's the case delete and reinstall Pillow with the follwoing commands.
"sudo apt-get remove python3-pil python3-pillow
sudo pip3 uninstall Pillow
pip3 install Pillow --break-system-packages"
now everythingshould be working fine.

6. Create bash file for auto start programm (optional)
-------------------------------------------
For an automatic start setup, first run "sudo nano /usr/bin/autostart_stockbox.sh" to create a bash file.
Insert:
"#!/bin/sh
(sleep 5s && cd /path/to/Stockbox_pyhton-script/ && pyhton StockBox_Pi.py) &
exit 0" 
into this file.

7. Create .desktop file 
-----------------------
After creating the bash file run "sudo nano /etc/xdg/autostart/Stockbox_Desktop.desktop"
and insert 
"[Desktop]
Name = free_choosable_name
Type = Application
Exec = sh /usr/bin/autostart_stockbox.sh (must be the path to the already created bash-file)
Terminal = false"

8. Reboot
---------
After creating and saving the files, shutdown the system with "sudo shutdown now" and start it again.
If everything went well, the StockBox window should appear a few seconds after starting.
Now ur system is ready to use

## Instructions

### Create new enrty
|Option | Description |
|-------|---------------------------------------------|
| Name | Choose a Name for the item you want to insert into the database| 
| Count | Set a Number of pieces u already own (must be a number)|
| Depot | Type in the storage place|
| Tags | Choose tags so u can search for items seperated by ',' (example: M3, Screw, Metric, Stainless-Steel, DIN-912)| 
| Description | Insert a short description for ur entry, this will be displayed|
| Trigger | Set to a number which reacts as a low stock alert (must be a number)|

### Searchbar Functions:
- Hit the search bar to list all entries.
- Regular searching into tags for precision output.
- Type "D:" into the search bar to search for specific depots, to find objects faster.
- Type "deleted" in the search bar to show all deleted items (items can be restored).

### Import from `.xslx` file
Please use the `Example_table.xlsx` table as reference. If u don#t use the exact format it wouldnt be working!!!


## `config.ini`

| Option  | Description                                      |
|---------|--------------------------------------------------|
| virtual_keyboard  | recomented for Raspberry Pi usage. 0=disabled, 1 = enabled|
| keyboard_layout  | Choose keyboard layout, temporary supported **qwerty** and **qwertz**|
| local_db  | 0 = use Server based database like MySQL, 1 = create a local database|
|dark_theme | 0 = Dark-Theme, 1 = Light-Theme|
|color_theme| Supported colors **blue** and **green**|
|Setting for server based Database|
|host| IP-adress from Database|
|port| Port from database (MySQL standard = 3306|
|username| User name from user who can create new Tables|
|password| Password for user|


## Credits

Note: Parts of the code in this example are from [CustomTkinter][2], [CTkMessagebox][3], 

If you find my programm help/- useful and would like to support me, feel free to buy me a Ko-fi. However, if you don't want to, that's okay too!

I'm always open to feedback to improve this project further!

[1]:https://github.com/CadamTechnology/StockBox/releases
[2]:https://github.com/TomSchimansky/CustomTkinter
[3]:https://github.com/Akascape/CTkMessagebox
