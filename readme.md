# Easy HTB Tool

_Basic tools in a basic way for HTB_

## Starting 🚀

_Just download the tool._

```
git clone https://github.com/Erheatex/HTBTool
```
You'll need some things to make this tool work

## Prerequisites  📋

_This are the prerequisites that you need_

#### FFUF

```
sudo apt install ffuf
```
#### Netcat

```
sudo apt install netcat
```
#### Python dependencies

```
pip install -r requirements.txt
```
## Usage 🔧

_How to use this tool_

```
python3 script.py
```
<img src="/ScreenShots/menu.png" width="700">

### 1. List all the HTB active machines

_With the HTB api key you can list all the active machines in HTB_

Insert your API key 

<img src="/ScreenShots/listHTB.png" width="500">

You will get a list with all the machines 

<img src="/ScreenShots/listHTB2.png" width="700">

### 2. Scan a machine using nmap

_With this method we can scan the most used ports in a machine_

The script will ask the ip address you want to scan

<img src="/ScreenShots/scan1.png" width="700">

You'll get the results

<img src="/ScreenShots/scan2.png" width="700">

### 3.Set listening port with Netcat
_With this method you can open a port for reverse shells_

The script will ask you the port you want to open

<img src="/ScreenShots/netcat.png" width="700">

### 4.Brute Force directories and files with Fuff
_With this method you can get hidden directories and files from a web server_

The script will ask you:
* URL ( http://webserver:port/ ) 
* Extensions to fuzz ( .php,.html,.txt)
* HTTP response codes to show ( 200,203,...)

<img src="/ScreenShots/ffuf1.png" width="700">

## Work in progress ⚙️

_This is not a finished tool_

Im using this project , as a way of learning python so any advice or bug reported will be thanked.

I am open to new ideas and functionalities that you think the tool needs

## TO DO ⚒
* Full nmap with more options ( -A -Pn ....)
* More HTB Info 
  * User roots, owns 
  * Retired Machines
  * Server Status
* Add more tools 
¿ What do you thing i have to add ?

## Disclamer ⚡

The use of this tool is your responsability. I hereby disclaim any responsibility for actions taken with this tool.

## Share this tool 🎁

* Show it to your friends 📢
* Let me know what do you think <a href=https://twitter.com/R00tedSec>My Twitter</a>


