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

#### 1. Download & Unzip
- Download the latest release and unzip it to your preferred directory.

#### 2. Edit `config.ini`
- Open the `config.ini` file and update the settings.

#### 3. Start StockBox
- Launch **StockBox** and import your `.xlsx` file to quickly set up the database.

#### 4. You're All Set!
- Your setup is complete, and you're ready to go!

### Linux/Debian

#### 1. Update & Download
- Update your system and download the code with **git clone**.

#### 2. Installation
- Install tkinter and all requirements

#### 3. Edit `config.ini`
- Open the `config.ini` file and update the settings.

#### 4. Navigate to folder
- Befor running the code make sure u are in the right diratory, otherwise you will get some errors. 

#### 5. Start StockBox
- Launch **StockBox** and import your `.xlsx` file to quickly set up the database.

#### 6. Auto start (optional)
- Create `.bash` and `.desktop` file for auto starting.
  
---

## Installation

### Windows setup

#### 1. Download & Extract

- **Download**: Get the latest release (`StockBox_V_XX.zip`) from the [release page](1).
- **Extract**: Unzip all the files and move the folder to your preferred directory.
  - **Tip**: Avoid using `Program` or `Program Files (x86)` to sidestep administrative issues.

#### 2. Adjust the `config.ini` File

- **Locate**: Open the `config.ini` file in the project folder.
- **Configure**: Update the settings to match your environment and preferences. Ensure all required fields, such as database connection details and virtual keyboard settings, are correctly set up.
  - **More Info**: Detailed configuration instructions are provided below.
  - **Default**: By default it's set to a local databse without a virtual keyboard in darkmode with green color

#### 3. You're Done!

- **Run**: With the folder moved and `config.ini` configured, your setup is complete!
  - **Tip**: Create a desktop shortcut for easier access.


### Linux/Debian

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
- **Adjust**: Open the `config.ini` file to update the settings. By default it's set to a local databse without a virtual keyboard in darkmode with green color.
```bash
nano ~/StockBox/StockBox/config.ini
``` 
- **Save**: After making adjustments, save the changes by pressing <kbd>CTRL</kbd> + <kbd>S</kbd>, then exit the file by pressing <kbd>CTRL</kbd> + <kbd>X</kbd>.
  - **More Info**: Detailed configuration instructions are provided below.

#### 6. Run the code
- **Run**: Navigate to the stored location and execute the `StockBox_v_x_x.py` file (make sure to enter the right version). If you don't move to the directory, it maybe cause some errors.
```bash
cd ~/StockBox/StockBox/
pyhton3 StockBox_v_x_x.py
``` 

### Raspberry Pi
The following steps are for setup the code on autostart for a raspberry pi with touchscreen as standalone. I recommend a Raspberry Pi 4b with 4GB Ram. Please following the **Linux-Instrucion** above. 

#### 1. Bash file

- **Create**: For an automatic start setup, first create a bash file.
```bash
sudo nano /usr/bin/autostart_stockbox.sh
```
- **Insert**: add the following lines to the new created file. make sure u enter the right path and version number.
```bash
#!/bin/sh
(sleep 5s && cd /path/to/Stockbox_pyhton-script/ && pyhton StockBox_v_x_x.py) &
exit 0
```

#### 2. `.desktop` file

- **Create**: After creating the bash file, run the following command:
```bash
sudo nano /etc/xdg/autostart/Stockbox_Desktop.desktop
```
- **Insert**: Add the following lines to the newly created file. Make sure to enter the correct path to the already created bash file.
```bash 
[Desktop]
Name=free_choosable_name
Type=Application
Exec=sh /usr/bin/autostart_stockbox.sh (must be the path to the already created bash-file)
Terminal=false
```
After rebooting the system everything should work well.

---
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

### Import from a `.xslx` file
For a faster setup, first create a `.xlsx.` table. Use the provided `Example_table.xlsx` as a reference. (If you don't use the exact format it wouldnt be working!) he first two entries in the example are just placeholders and can be removed. 
Ensure that the headers and structure remain intact. Only enter digits into the colums Count and Trigger_count. After saving the file, open **StockBox**, go to settings and hit the **import** button. Notice the Message that shows up. Every existing entry will be deleted and **CAN'T** be restored!
Select your `.xlsx.` table and a new database will be created. 


---
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

---
## Credits

Note: Parts of the code in this example are from [CustomTkinter][2], [CTkMessagebox][3]

If you find my programm help/- useful and would like to support me, feel free to buy me a Ko-fi. However, if you don't want to, that's okay too!

I'm always open to feedback to improve this project further!

[1]:https://github.com/CadamTechnology/StockBox/releases
[2]:https://github.com/TomSchimansky/CustomTkinter
[3]:https://github.com/Akascape/CTkMessagebox
