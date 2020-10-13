
import nmap 
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

def main():
    banner()
    htbList()
    #menu()



def menu():
    option=int(input(Fore.RED+"Seleccione la opcion que desee: "))
    switch_menu.get(option,exit)()

def banner():
    f = open('art.txt', 'r')
    file_contents = f.read()
    print (Fore.GREEN+file_contents)
    f.close()


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
        menu()


def scan():
    host=str(input("Introduce el host a analizar (IP): "))
    if host=="localhost":
        host="127.0.0.1"
    nmap = nmap3.Nmap()
    results = nmap.scan_top_ports(host,default=25)
    printNmapData(results[host])
    main()


def ports():
    print("Escaneando puertos .....")

def fuzz():
    try:
        extensions=str(input("Extensiones que quieres fuzzear: "))
        url=str(input("Direccion del servidor web a fuzzear: "))
        url+"FUZZ"
        fuzzing= subprocess.run(["ffuf","-w","big.txt", "-e",extensions,"-u",url+"FUZZ"])
        print(fuzzing)
    except KeyboardInterrupt:
        print ("\nBack to the menu")
        menu()

def htbList():
    htb=htbapi.machines
    allmachines=htb.getAllActiveMachines("nqvyG2Jn3VDJmB3bsiCfjxAJsirGG4oLrMnfqfm5ZTXTJNCyniP6sIt4eT4i")
    print(allmachines)
    x = PrettyTable()
    x.field_names=["Name","OS","IP"]
    for id in allmachines:
        x.add_row([id["name"],id["os"],id["ip"]])
    print (x)

def exit():
    print("Saliendo de la aplicacion.....")

switch_menu={
        1:htbList,
        2:scan,
        2:reverseShell,
        3:fuzz
    }

main()