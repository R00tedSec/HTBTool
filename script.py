
import nmap3
import subprocess
import signal
import socket
import sys
import requests
import htbapi
from prettytable import PrettyTable
from colorama import init,Fore,Back,Style

init(autoreset=True)
apikey=None

def main():
    banner()





def banner():
    f = open('art.txt', 'r')
    file_contents = f.read()
    print (Fore.LIGHTGREEN_EX+file_contents)
    f.close()
    f = open('menu.txt', 'r')
    file_contents = f.read()
    print(Fore.LIGHTYELLOW_EX+file_contents)
    option=int(input(Fore.LIGHTYELLOW_EX+"Selected option: "))
    switch_menu.get(option,exit)()


def help():
    print("Ayuda iniciando .....")

def printNmapData(data):
    x = PrettyTable()
    x.field_names=["Service","Port","State"]
    for port in data:
        x.add_row([port["service"]["name"],port["portid"],port["state"]])
    print (x)

def reverseShell():
    try:
        port = 8888
        netcat= subprocess.run(["nc","-lnvp",str(port)])
    except KeyboardInterrupt:
        print("Cerrando la conexion ...")
        banner()


def scan():
    host=str(input("\n\nIntroduce el host a analizar (IP): "))
    if host=="localhost":
        host="127.0.0.1"
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(host,default=25)
    printNmapData(results[host])
    banner()



def fuzz():
    try:
        extensions=str(input("Extensiones que quieres fuzzear: "))
        url=str(input("Direccion del servidor web a fuzzear: "))
        url+"FUZZ"
        try:
            fuzzing= subprocess.run(["ffuf","-w","big.txt", "-e",extensions,"-u",url+"FUZZ"])
            print(fuzzing)
        except FileNotFoundError:
            print(Fore.RED+"\t[!] ERROR FFUF NOT INSTALLED!!")
    except KeyboardInterrupt:
        print ("\nBack to the menu")
        banner()
    

def htbList():
    global apikey
    print(Fore.LIGHTGREEN_EX+"\n\n[1] LISTING ALL ACTIVE MACHINES IN HTB\n")
    apikey="nqvyG2Jn3VDJmB3bsiCfjxAJsirGG4oLrMnfqfm5ZTXTJNCyniP6sIt4eT4i"
    if apikey==None:
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
        print(Fore.RED+"\tERROR: Your HTB key is invalid!!!"+Fore.RESET)

    banner()

def exit():
    print("Saliendo de la aplicacion.....")

switch_menu={
        1:htbList,
        2:scan,
        3:reverseShell,
        4:fuzz
    }

main()