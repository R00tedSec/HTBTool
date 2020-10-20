#!/bin/python3

import nmap3
import subprocess
import htbapi
from prettytable import PrettyTable
from colorama import init,Fore,Back,Style

init(autoreset=True)
apikey=None


def main():
    banner()
    help()
    option=int(input(Fore.LIGHTYELLOW_EX+"Selected option: "+Fore.RESET))
    switch_menu.get(option,exit)()

def banner():
    f = open('art/art.txt', 'r')
    file_contents = f.read()
    print (Fore.LIGHTGREEN_EX+file_contents+Fore.RESET)
    f.close()



def help():
    f = open('art/menu.txt', 'r')
    file_contents = f.read()
    print(Fore.LIGHTYELLOW_EX+file_contents+Fore.RESET)



## Retrive all the Active Machines in HackTheBox
def htbList():
    global apikey
    print(Fore.LIGHTGREEN_EX+"\n\n[1] LISTING ALL ACTIVE MACHINES IN HTB\n")
    if apikey==None or apikey=="error":
        apikey=str(input("\tAPI KEY: "))
    try:
        htb=htbapi.machines
        allmachines=htb.getAllActiveMachines(apikey)
        x = PrettyTable()
        x.field_names=[Fore.LIGHTYELLOW_EX+"Name"+Fore.RESET,Fore.LIGHTMAGENTA_EX+"OS"+Fore.RESET,Fore.BLUE+"IP"+Fore.RESET,Fore.LIGHTBLUE_EX+"Release Date"+Fore.RESET,Fore.RED+"Rating"+Fore.RESET]
        for id in reversed(allmachines):
            x.add_row([Fore.LIGHTYELLOW_EX+id["name"]+Fore.RESET,Fore.LIGHTMAGENTA_EX+id["os"]+Fore.RESET,Fore.BLUE+id["ip"]+Fore.RESET,Fore.LIGHTBLUE_EX+id["release"]+Fore.RESET,Fore.RED+id["rating"]+Fore.RESET])
        x.padding_width = 5
        print (x)
    except:
        print(Fore.RED+"\t[!] ERROR: INVALID HTB APIKEY !!"+Fore.RESET)
        apikey="error"
    main()



def printNmapData(data):
    x = PrettyTable()
    x.field_names=[Fore.LIGHTYELLOW_EX+"Service"+Fore.RESET,Fore.LIGHTMAGENTA_EX+"Port"+Fore.RESET,Fore.BLUE+"State"+Fore.RESET]
    for port in data:
        if port["state"]=="open":
            x.add_row([Fore.LIGHTYELLOW_EX+port["service"]["name"]+Fore.RESET,Fore.LIGHTMAGENTA_EX+port["portid"]+Fore.RESET,Fore.BLUE+port["state"]+Fore.RESET])
    x.padding_width = 3
    print (x)



def scan():
    print(Fore.LIGHTGREEN_EX+"\n\n[2] SCAN YOUR TARGET WITH NMAP \n")

    try:
        try:
            host=str(input(Fore.LIGHTGREEN_EX+"\n\tHost to scan [10.10.10.XXX]: "+Fore.RESET))
            if host=="localhost":
                host="127.0.0.1"
            nmap = nmap3.Nmap()
            results = nmap.scan_top_ports(host,default=25)
            printNmapData(results[host])
        except KeyboardInterrupt:
            print (Fore.GREEN+"\nBack to the menu")
            
    except :
        print (Fore.GREEN+"\nBack to the menu")
    main() 



def reverseShell():
    print(Fore.LIGHTGREEN_EX+"\n\n[3] SETTING LISTENING PORT WITH NETCAT \n")

    try:
        port=input(Fore.LIGHTGREEN_EX+"\tPORT: "+Fore.RESET)
        try:
            print(Fore.LIGHTGREEN_EX+"\n[✓] Started netcat on port "+port)
            netcat= subprocess.run(["nc","-lnvp",str(port)])
        except FileNotFoundError:
            print(Fore.RED+"[!] ERROR: NETCAT IS NOT INSTALLED!!")
            
    except KeyboardInterrupt:
        print(Fore.RED+"[*] Stoping netcat ")
    main()


def fuzz():
    print(Fore.LIGHTGREEN_EX+"\n\n[4] BRUTE FORCE DIRECTORIES AND FILES ( FFUF )   \n")
    try:
        url=str(input(Fore.LIGHTGREEN_EX+"\t[1] Server to fuzz [ http[s]://IP:PORT/ ] : "+Fore.RESET))
        extensions=str(input(Fore.LIGHTGREEN_EX+"\t[2] Extensions to Fuzz [ .html,.php,.js ]: "+Fore.RESET))
        url+"FUZZ"
        httpcodes=str(input(Fore.LIGHTGREEN_EX+"\t[3] HTTP response status to manage[all by default]:  " +Fore.RESET) or "all")

        print(httpcodes)       
        try:
            fuzzing= subprocess.run(["ffuf","-w","wordlists/big.txt","-mc",httpcodes, "-e",extensions,"-u",url+"FUZZ"])
        except FileNotFoundError:
            print(Fore.RED+"\t[!] ERROR: FFUF NOT INSTALLED!!")
    except KeyboardInterrupt:
        print (Fore.GREEN+"\nBack to the menu")
    print(Fore.LIGHTYELLOW_EX+"\n\t[✓] FUZZING FINISHED !!")
    main()    
    

switch_menu={
        1:htbList,
        2:scan,
        3:reverseShell,
        4:fuzz
    }


def exit():
    print(Fore.LIGHTGREEN_EX+"\n\t[✓] BYE ... :D")


main()