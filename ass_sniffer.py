#Created by Aaron Beimborn on 8/30/2025
#Soli Deo Gloria
#--------------------------------------
import os
import subprocess
import json
continue_search = "y"
__version__ = "0.1.0-alpha"
#Set Default Path to current directory of python executable
path = os.path.dirname(os.path.realpath(__file__))
stream = ":$DATA"
banner = r"""
  /$$$$$$   /$$$$$$   /$$$$$$         /$$$$$$  /$$   /$$ /$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$ /$$__  $$       /$$__  $$| $$$ | $$|_  $$_/| $$_____/| $$_____/| $$_____/| $$__  $$
| $$  \ $$| $$  \__/| $$  \__/      | $$  \__/| $$$$| $$  | $$  | $$      | $$      | $$      | $$  \ $$
| $$$$$$$$|  $$$$$$ |  $$$$$$       |  $$$$$$ | $$ $$ $$  | $$  | $$$$$   | $$$$$   | $$$$$   | $$$$$$$/
| $$__  $$ \____  $$ \____  $$       \____  $$| $$  $$$$  | $$  | $$__/   | $$__/   | $$__/   | $$__  $$
| $$  | $$ /$$  \ $$ /$$  \ $$       /$$  \ $$| $$\  $$$  | $$  | $$      | $$      | $$      | $$  \ $$
| $$  | $$|  $$$$$$/|  $$$$$$/      |  $$$$$$/| $$ \  $$ /$$$$$$| $$      | $$      | $$$$$$$$| $$  | $$
|__/  |__/ \______/  \______/        \______/ |__/  \__/|______/|__/      |__/      |________/|__/  |__/
                                                                                                        
                                                                                                       
"""
valid_selections = ["0", "1", "2", "3"]
def displayMenu():
    print("Please make a selection from the menu below: ")
    print("[1] Scan a specific file for ADS ")
    print("[2] View a files ADS (Interactive)")
    print("[3] Save a files ADS (Interactive)")

print(banner)
print("Welcome to Alternate Stream Scanner (ASS) and Sniffing Tool! The Interactive ADS Tool!")
displayMenu()
user_selection = input("Selection: ")

while True:
    if (user_selection not in valid_selections):
        print("Please Enter a valid selection ID: ")
        user_selection = input("Selection: ")
    elif (user_selection == "0"):
        displayMenu()
        user_selection = input("Selection: ")
    else:
        match user_selection:
            case "1":
                path = input("Enter the name of the file that you would like to scan for ADS: ")
                if not os.path.isfile(path):
                    print(f"File does not exist: {path}")
                else:
                    cmd= ["powershell", "-Command", f"Get-Item -Path {path} -Stream * | ConvertTo-Json"]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    output = result.stdout
                    json_data = json.loads(output)     
                    print("====RESULTS====")
                    for stream in json_data:
                        print("Data Stream: " + stream['Stream'] + "\nLength: " + str(stream['Length']) + "\nPSChildName: " + stream['PSChildName'])
                        print("----------------------------")
                    continue_search = input("Search Another File for ADS? (y/n) ")
                    if(continue_search == "y"):
                        user_selection = "1"
                    elif(continue_search =="n"):
                        user_selection = "0"
                    else:
                        print("Invalid Character Entered. Please respond with (y/n)")
                        continue_search = input("(y/n)")
            case "2":
                path = input("Enter the name of the file that you would like to scan for ADS: ")
                if not os.path.isfile(path):
                    print(f"File does not exist: {path}")
                else:
                    # Run Search to pull all the ADS for the file
                    cmd= ["powershell", "-Command", f"Get-Item -Path {path} -Stream * | ConvertTo-Json"]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    output = result.stdout
                    json_data = json.loads(output)
                    for index, stream in enumerate(json_data):
                        print("[" + str(index) + "]: " + stream['Stream'])
                        
                    ads_read_select = input("Enter the ADS that you would like to read: ")
                    while True:
                        try:
                            int_ads_read_select = int(ads_read_select)
                            break
                        except ValueError:
                            print(f"Error: '{ads_read_select}' is not a valid number, please try again! ")
                    
                    cmd = ["powershell", "-Command", f"Get-Content {path} -Stream {json_data[int_ads_read_select]['Stream']}"]   
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    output = result.stdout
                    print(output)
                    # Save output to separate file:
                    save_file = input("Would you like to save the ADS data to a separate file? (y/n) ")
                    if(save_file == "y"):
                        save_file_name = input("Name for save file: ")
                        if(os.path.exists(save_file_name)):
                            while True:
                                print("WARNING!!! The filename that you entered already exists, if you continue you will overwrite data.")
                                err_cont = input("Would you like to overwrite the file? (y/n): ")
                                if(err_cont == "y"):
                                    with open(save_file_name, "w") as y:
                                        y.write(output)
                                    user_selection = "0"
                                    print("File SAVED")
                                    break
                                elif(err_cont =="n"):
                                    save_file_name = input("Name for save file: ")
                                else:
                                    print("Invalid Character Entered. Please respond with (y/n)")
                                    err_cont = input("Would you like to overwrite the file? (y/n): ")
                        else:
                            with open(save_file_name, "w") as f:
                                f.write(output)
                            print("File SAVED")    
                            user_selection = "0"
                    else:
                        user_selection = "0"
            case "3":
                path = input("Enter the name of the file to extract an ADS from: ")
                if not os.path.isfile(path):
                    print(f"File does not exist: {path}")
                else:
                    cmd= ["powershell", "-Command", f"Get-Item -Path {path} -Stream * | ConvertTo-Json"]
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    output = result.stdout
                    json_data = json.loads(output)
                    for index, stream in enumerate(json_data):
                        print("[" + str(index) + "]: " + stream['Stream'])
                    ads_save_select = input("Enter the number of the ADS that you would like to save: ")
                    while True:
                        try:
                            int_ads_save_select = int(ads_save_select)
                            break
                        except ValueError:
                            print(f"Error: '{ads_save_select}' is not a valid number, please try again! ")
                            
                    cmd = ["powershell", "-Command", f"Get-Content {path} -Stream {json_data[ads_save_select]['Stream']}"]   
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    output = result.stdout
                    save_file_name = input("Name for save file: ")
                    if(os.path.exists(save_file_name)):
                        while True:
                            print("WARNING!!! The filename that you entered already exists, if you continue you will overwrite data.")
                            err_cont = input("Would you like to overwrite the file? (y/n): ")
                            if(err_cont == "y"):
                                with open(save_file_name, "w") as y:
                                    y.write(output)
                                user_selection = "0"
                                print("File SAVED")
                                break
                            elif(err_cont =="n"):
                                save_file_name = input("Name for save file: ")
                            else:
                                print("Invalid Character Entered. Please respond with (y/n)")
                                err_cont = input("Would you like to overwrite the file? (y/n): ")
                    else:
                        with open(save_file_name, "w") as f:
                            f.write(output)
                        print("File SAVED")
                        user_selection = "0"