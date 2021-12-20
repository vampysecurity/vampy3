import os

import sys, os, webbrowser, platform, subprocess

import webbrowser

def menu():

  os.system('clear')

print ("\t1 - mercado negro")
print ("\t2 - venta de armas militares")
print ("\t3 - blockchain")
print ("\t4 - localizacion de personas")
print ("\t5 - dorks para sqlmap")
print ("\t6 - nmap online")
print ("\t7 - data generator")
print ("\t8 - email temporal")
print ("\t9 - namso")
print ("\ta - vpn")
print ("\tb - cuentas ssh")
print ("\tc - proxies")
print ("\td - bincodes")
print ("\te - manual de Tux")
print ("\tf - blog")
print ("\tg - Grupo de whatsapp")
print ("\th - sqlmap online")
print ("\ti - Numero virtual")
print ("\tj - salir")


def __limpiar():
  if os.name == 'nt':
            os.system('cls')
  else:
            os.system('clear')
def menu():
  __limpiar()


opcionMenu = raw_input("Vampy  > ")

if opcionMenu=="1":
    webbrowser.open ("https://mega.nz/#!eNwRnCjS!di9gP2Hxp4NVv3DeFNTPKlQEbRxVK2_DRdwiShnmMJU")

elif opcionMenu == "2":
    webbrowser.open('http://arminse.es/922-armas-de-fuego')

elif opcionMenu == "3":
    webbrowser.open('https://www.blockchain.com/es/')

elif opcionMenu == "4":
    webbrowser.open('https://www.google.com.mx/search?client=opera-gx&q=reverse+phone+lookup&sourceid=opera&ie=UTF-8&oe=UTF-8')

elif opcionMenu == "5":
    webbrowser.open('https://gbhackers.com/latest-google-sql-dorks/')

elif opcionMenu == "6":
    webbrowser.open('https://hackertarget.com/nmap-online-port-scanner/')

elif opcionMenu == "7":
    webbrowser.open('http://www.datafakegenerator.com')

elif opcionMenu == "8":
    webbrowser.open('https://correotemporal.org')

elif opcionMenu == "9":
    webbrowser.open('https://bestccgen.com/namso-ccgen/')

elif opcionMenu == "a":
    webbrowser.open('https://www.tunnelbear.com')

elif opcionMenu == "b":
    webbrowser.open('https://www.fastssh.com')

elif opcionMenu == "c":
    webbrowser.open('https://free-proxy-list.net')

elif opcionMenu == "d":
    webbrowser.open('https://www.bincodes.com')

elif opcionMenu == "e":
    webbrowser.open('http://www.mediafire.com/file/07gd0tci5y5zl3o/Manual_de_Tux.pdf/file')

elif opcionMenu == "f":
    webbrowser.open('https://tuxvmp.blogspot.com')

elif opcionMenu == "g":
    webbrowser.open('https://chat.whatsapp.com/KnBM8HfOqkyJBVBonPdq7P')


elif opcionMenu == "h":
    webbrowser.open('https://suip.biz/?act=sqlmap')

elif opcionMenu == "i":
    webbrowser.open('https://www.receive-sms-online.info')

elif opcionMenu == "j":
    menu()

else:
  print "opcion invalidad"
