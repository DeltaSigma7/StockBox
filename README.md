# Stockbox
Stockbox is a comprehensive inventory management program designed specifically for hobbyists. 
Whether you're managing your collection of model trains, DIY electronics components, or any other hobby materials, Stockbox provides an easy and efficient way to keep track of your inventory.

## Features
- Simple and intuitive interface for easy inventory management
- Support for categorizing and tagging items to keep your collection organized
- Detailed item descriptions, including quantity, storage location, and additional notes
- Alerts for low stock levels to ensure you never run out of essential items
- Convert '.xlsx' file to database to keep the setup fast
- Separate menu for adding entries to keep your system up to date


## Installation

### Windows

1. Download & Extract
-----------
Download complete code as zip. Extract all files and move 'StockBox_windows' folder to directory you want to store and run the project files.

2. 
3. 
1. Move the Folder to the Desired Directory
--------------------------------------------
Simply drag and drop the entire project folder into the directory where you want to store and run the project files.

2. Adjust the config.ini File
-----------------------------
Open the `config.ini` file located within the project folder. Update the configuration settings according to your environment and preferences. 
Ensure that all required fields are correctly set up, such as database connection details, virtual keyboard settings, etc.

3. You're Done!
---------------
Once you have moved the folder and adjusted the `config.ini` file, the setup is complete. You can now run the project without any further configuration.


### Linux

1. Update system
----------------
Run "sudo apt-get update" and "sudo apt-get dist-upgrade -y" to fully update ur system. This maybe take some time. 

2. Install TKinter 
------------------
Type "sudo apt-get install python3-tk" to install the Tkinter libary for python.  

3. Install requirements
-----------------------
Navigate to the folder the project files are stored in ("cd path/to/stored/project"). 
After you navigate there install all python libaries with "pip3 install -r requirements.txt --break-system-packages" make sure pip is already installed
wait till everything is installed.

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

Create new enrty:
- Name: Choose a Name for the item you want to insert into the database 
- Count: Set a Number of pieces u already own (must be a number)
- Depot: Type in the storage place
- Tags: Choose tags so u can search for items seperated by ',' (example: M3, Screw, Metric, Stainless-Steel, DIN-912) 
- Description: Insert a short description for ur entry, this will be displayed
- Trigger: Set to a number which reacts as a low stock alert (must be a number)

Searchbar Functions:
- Hit the search bar to list the first 50 entries.
- Regular searching into tags for precision output.
- Type "D:" into the search bar to search for specific depots, to find objects faster.
- Type "deleted" in the search bar to show all deleted items (items can be restored).

Thank you for using StockBox, if u like this programm feel free to buy me some coffee (https://ko-fi.com/cadam)
