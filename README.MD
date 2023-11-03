<img src="static/img/69DFD530-BC83-47C3-B485-30325DE37374.jpeg" style="width: 40px; border-radius: 40px">
<span style="position: absolute; top: 13px; font-size: 14px"> &nbsp Tesfahiwet Truneh
<br>
&nbsp Script Developer & Cyber Security geek
</span>
<br>
<hr>

> Disclaimer: This reverse shell should only be used in the lawful, remote administration of authorized systems. Accessing a computer network without authorization or permission is 
> illegal

* `Evil-X RAT` is a remote administration tool that gives a reverse shell to a remote client device.

* The tool uses `TCP(Transmisiion Control Protocol)` data transmission which is conection-oriented to send/receive data bytes from and to the server.

* Once the client side code is installed on the target machine. it will try to connect to the host server based on the `socket IP and Port`

* Once the client is connected to the the socket server default and custom commands can be excuted on the victim device from the remote server.

# Custom Commands

* `display       `       : List of all connected clients to server socket
* `quit       `          : Break current connection with the client
* `attack <index>`       : Select a client to execute remote commands
* `browse        `       : Open browser and execute queries remotely
* `background    `       : Change client desktop backgroud image
* `info          `       : Display device hardware information
* `webcam        `       : Open webcam and take a photo
* `screenshot    `       : Take a screenshot of the main screen and save it as an image file
* `upload        `       : Upload the specified file from server to the client
* `Download      `       : Download the specified file from client to the server
* `record        `       : Turn on mic and record conversation for number of seconds

# How to Use

1. before we run the script mae sure you the server is assigned to the right `ip address` and `closed port number`
2. Change host address and port number of `client.py` to the actual IP of the attacker on `server.py`
3. Transfer `client.py` to the target machine or generate window executable file of `client.py` using the following command 
``` bash
$ pyinstaller --noconfirm --onefile --windowed --icon "<Icon File Path>"  "client.py Path" 
```
4. Run `server.py` on the attacker machines