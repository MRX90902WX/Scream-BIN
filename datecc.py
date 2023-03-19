from random import randint
import datetime

#Code: D€m0
#CODIGO DE USO LIBRE#
dates = input("\033[1;37m[\033[1;31m#\033[1;37m]\033[1;33mGenerar fecha de cad. \033[1;37msi/no: ")

if dates == "si":
 def dategen():
   now = datetime.datetime.now()
   date = ""                                                                         
   month = str(randint(1, 9))
   current_year = str(now.year)                                                 
   year = str(randint(int(current_year[-2:]) + 1, int(current_year[-2:]) + 6))
   date = month + "/" + year

   return date

else:
    exit()

def main():
    print("")
    print(f"\033[1;36m----> \033[1;37m{dategen()}")
main()
