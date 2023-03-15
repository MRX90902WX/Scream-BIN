import random
from os import system

#CODE: DEMO 
#PAIS: ECUADOR
system("clear")
print("\033[1;33m╭━━━┳━━━┳━━━┳━━━┳━━━┳━╮╭━╮")
print("\033[1;33m┃╭━╮┃╭━╮┃╭━╮┃╭━━┫╭━╮┃┃╰╯┃┃")
print("\033[1;34m┃╰━━┫┃╱╰┫╰━╯┃╰━━┫┃╱┃┃╭╮╭╮┃")
print("\033[1;34m╰━━╮┃┃╱╭┫╭╮╭┫╭━━┫╰━╯┃┃┃┃┃┃")
print("\033[1;31m┃╰━╯┃╰━╯┃┃┃╰┫╰━━┫╭━╮┃┃┃┃┃┃")
print("\033[1;31m╰━━━┻━━━┻╯╰━┻━━━┻╯╱╰┻╯╰╯╰╯")
print("")
print("\033[1;33m╭━━╮╭━━┳━╮ ╭╮")
print("\033[1;33m┃╭╮┃╰┫┣┫┃╰╮┃┃")
print("\033[1;34m┃╰╯╰╮┃┃┃╭╮╰╯┃")
print("\033[1;34m┃╭━╮┃┃┃┃┃╰╮┃┃")
print("\033[1;31m┃╰━╯┣┫┣┫┃ ┃┃┃")
print("\033[1;31m╰━━━┻━━┻╯ ╰━╯")


print("")
print("\033[1;36m▬▬▬▬▬▬ MENU ▬▬▬▬▬▬")
print("")
print("\033[1;31m[\033[1;32m1\033[1;31m] \033[1;37mGenerador BINS aleatorios")
print("\033[1;31m[\033[1;32m2\033[1;31m] \033[1;37mGenerador de CCS")
print("\033[1;31m[\033[1;32m3\033[1;31m] \033[1;37mGenerar BIN Rnd")
print("\033[1;31m[\033[1;32m4\033[1;31m] \033[1;37mGenerar BIN con fecha")
print("\033[1;31m[\033[1;32m5\033[1;31m] \033[1;37mInformacion BIN/CC")
print("\033[1;31m[\033[1;32m6\033[1;31m] \033[1;37mHerramienta AIO-CC")
print("\033[1;31m[\033[1;32m7\033[1;31m] \033[1;37mCCGEN Jorge Barba")
print("\033[1;31m[\033[1;32m8\033[1;31m] \033[1;37mExtrapolar CC [WEB]")
print("\033[1;31m[\033[1;32m9\033[1;31m] \033[1;37m(593) MundoBinsRH")
print("\033[1;31m[\033[1;32m10\033[1;31m] \033[1;37mBin YouTube Premiun")
print("\033[1;31m[\033[1;32m00\033[1;31m] \033[1;37mSalir")

opcion = input("\033[1;36m[~]OPCION : \033[1;37m")

if opcion == "1":
        print("")
        aumentando = 1                                                                                                                                                   
        cantidad = int(input("\033[1;33mCuantas BIN'S te gustaria generar: \033[1;37m"))
        print("")
        while aumentando <= cantidad:                                                                                                                                       
               generador = str(random.randint(4,6)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) +  str(random.randint(0,9)) + str(random.randint(0,9))
               bingen = generador + "xxxxxxxxxx"
               print(f"\033[1;37m{bingen}")
               aumentando += 1
               

elif opcion == "2":
        system("python two.py")
elif opcion == "3":
        system("python bingnd.py")
elif opcion == "4":
        system("python binfecha.py")
elif opcion == "5":
        system("python tree.py")
elif opcion == "6":
        system("python aio.py")
elif opcion == "7":
        system("python jorgecc.py")
elif opcion == "8":
        system("sleep 1")
        system("bash card.sh")
elif opcion == "9":
        system("sleep 1")
        system("bash mundo.sh")
elif opcion == "10":
        system("python yt.py")
elif opcion == "00":
        exit()
else:
     print("\033[1;31m[x]Opcion invalida")
     exit()
