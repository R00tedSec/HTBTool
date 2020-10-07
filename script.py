
import nmap3


def banner():
    f = open('art.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()


def help():
    print("Ayuda iniciando .....")

def scan():
    host=input("Introduce el host a analizar (IP): ")
    try:
        print("Nmapeando el dispositivo....")
        nmap = nmap3.Nmap()
        results = nmap.scan_top_ports(host)
        print(results)
    except:
        print("Posiblemente hayas introducido mal el host o no tienes NMAP instalado.")
        


def ports():
    print("Escaneando puertos .....")

def fuzz():
     print("Fuzzeando directorios  .....")

def exit():
    print("Saliendo de la aplicacion.....")

switch_menu={
        1:scan,
        2:ports,
        3:fuzz
    }

if __name__ == '__main__':
    banner()
    option=int(input("Seleccione la opcion que desee: "))
    switch_menu.get(option,exit)()