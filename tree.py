import requests
import json
from os import system


def get_info():
   
                        system("setterm -foreground green")
                        system("figlet BIN/CC")
                        ccbin = input( "\033[1;31m[\033[1;33m+\033[1;31m]\033[1;37mDigita el BIN/CC: ")
                        print("")
                        r = requests.get("https://bin-checker.net/api/" + ccbin)                                                             
                        json = r.json()
                        print(" CC o Bin: " + str(ccbin))
                        print(" MARCA: ", json["scheme"])
                        print(" TIPO: ", json["type"])
                        print(" NIVEL: ", json["level"])
                        country = json["country"]
                        pais = country["name"]
                        codigo = country["code"]
                        print(" NOMBRE PAIS: ", pais)
                        print(" CODIGO PAIS: ", codigo)
                        bank = json["bank"]
                        nombre = bank["name"]
                        sitioweb = bank["website"]
                        numero = bank["phone"]
                        print(" NOMBRE BANCO: ", nombre)
                        print(" SITIO WEB BANCO: ", sitioweb)
                        print(" NUMERO BANCO: ", numero)
                        todo = str("CC: " + str(ccbin +
                                " \nMARCA: " + json["scheme"] +
                                " \nTIPO: " + json["type"] +
                                " \nNIVEL: " + json["level"] +
                                " \nNOMBRE PAIS: " + pais +
                                " \nCODIGO PAIS: " + codigo +
                                " \nNOMBRE BANCO: " + nombre +
                                " \nSITIO WEB BANCO: " + sitioweb +
                                " \nNUMERO BANCO: " + numero +
                                " \nººººººººººººººººººººººººººººººººººº"))
                        print( " ºººººººººººººººººººººººººººººººººº")      
                  
get_info()

print("")
print(" \033[1;33mDesea continuar usando el programa \033[1;37msi/no")
volver = input(" \033[1;37m>>> ")

if volver == "si":                                                                      
         system("python scream.py")
else:                        
         print("")                                                               
         print(" \033[1;37m[+]\033[1;32mSCREAM BIN ,BYE")
         system("sleep 1")
         exit()
