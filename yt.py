#!/usr/bin/env Python 3.6
#Codigo by sRBill96 para netixzen.blogspot.com.ar
from os import system
import sys
import math
import json
import random
import datetime
system("clear")

system("setterm -foreground green")
print("  ____                           _       ____ ___ _   _")
print(" / ___| ___ _ __   ___ _ __ __ _| |_ ___| __ )_ _| \ | |")
print("| |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \  _ \| ||  \| |")
print("| |_| |  __/ | | |  __/ | | (_| | ||  __/ |_) | || |\  |")
print(" \____|\___|_| |_|\___|_|  \__,_|\__\___|____/___|_| \_|")
print(" ")
print(" ")
print(" ")

print("[♤]Usuario: admin")
print("User login")

print("[♤]Password: mrx12345")
print("Passwd login")
print(" ")
print("[+]Bienvenido ☆")
system("sleep 1")
print("")

class Generar_tarjeta():
	def __init__(self,BIN, cantidad=1, solo_impresion=True):
		self.BIN = BIN.replace(" ","")#Procesar espacios
		self.db_bins = ()			

		if(len(self.BIN) > 16 or len(self.BIN) < 15):#Tiene que tener la longitud indicada
			print("Por favor revisa la longitud del BIN.")
		elif(BIN[0].lower() == "x"):#Si no hay un bin especifico se elige uno de la db al azar
			print("No hay un BIN asignado, eligiendo uno al azar de la base de datos")
			bin_reg = list(self.BIN)
			bin_nuevo = self.bin_al_azar()
			for i in range(0,5):bin_reg[i] = bin_nuevo[i]
			self.BIN = "".join([i for i in bin_reg])
			
		##Comienza generacion
		print(" TARGET           CVV   MM/AA    TIPO")
		self.localidad_bin = "Visa"
		self.RONDAS_GEN = 1000
		self.CANTIDAD_TARJETAS = cantidad
		self.lista_tarjetas = []
		self.dic_tarjetas = {}
		if self.CANTIDAD_TARJETAS >= 1:
			for i in range(0, self.CANTIDAD_TARJETAS):
				tarj_creada = self.crear_tarjeta()
				self.lista_tarjetas.append(tarj_creada["datos_completos"])
				#Plantilla dato
				self.dic_tarjetas[i] = {
						"numero":tarj_creada["numero_tarjeta"],
						"codigo_seg":tarj_creada["codigo_seg"],
						"tipo_tarjeta":tarj_creada["tipo_tarjeta"],
						"fecha":tarj_creada["venc"],
						"dato_completo":tarj_creada["datos_completos"]
				}
		else:
			self.crear_tarjeta()
		
		if solo_impresion:#solo impresion
			for n in self.lista_tarjetas:
				print(n)
		
	
	def json(self):
		return json.dumps(self.dic_tarjetas)

	def crear_tarjeta(self):
		tarjeta = {}
		tarjeta["numero_tarjeta"] = self.crear_numero(self.BIN)
		tarjeta["codigo_seg"] 	  = self.generar_codigo_seguridad()
		if(self.localidad_bin == "Desconocida"):
			tarjeta["tipo_tarjeta"] = (tarjeta["numero_tarjeta"])
			self.localidad_bin = tarjeta["tipo_tarjeta"]
		else:
			tarjeta["tipo_tarjeta"] = self.localidad_bin
		tarjeta["venc"]			  = self.generar_fecha_venc()
		self.string = ""
		self.string += tarjeta["numero_tarjeta"]
		self.string += " | " + tarjeta["codigo_seg"]
		self.string += " | " + tarjeta["venc"]["fecha_acortada"]
		self.string += " | " + tarjeta["tipo_tarjeta"]
		tarjeta["datos_completos"] = self.string
		return tarjeta
		
	def gen_aleatorio(self, BIN):	
		numero = ""
		for i in BIN:
			numero+=str(random.randint(0,9)) if i.lower() == "x" else i
		return numero
		
	def checkear(self, cc):
		num = list((map(int, str(cc))))
		return sum(num[::-2] + [sum(divmod(d * 2, 10)) for d in num[-2::-2]]) % 10 == 0

	def crear_numero(self, BIN):
		numero = self.gen_aleatorio(BIN)
		for i in range(1,self.RONDAS_GEN):
			numero = self.gen_aleatorio(BIN)
			chk0 = self.checkear(numero)
			if(chk0 and numero):
				return numero
		
	def generar_fecha_venc(self):
		fecha = {
			"anio":None,
			"mes":None,
			"fecha_completa":None,
			"fecha_acortada":None
		}
		def gen_anio():
			anio_actual = datetime.datetime.now().year
			return anio_actual  + random.randint(2,3)
		fecha["anio"] = str(gen_anio())
		def gen_mes(): 
			mes = random.randint(1,12)
			if(mes > 9):
				return str(mes)
			else:
				return "0"+str(mes)	
		
		fecha["mes"] = gen_mes()
		fecha["fecha_completa"] = fecha["mes"] + "/" + fecha["anio"]
		fecha["fecha_acortada"] = fecha["mes"] + "/" + fecha["anio"][2:]
		return fecha
		
	def generar_codigo_seguridad(self):
		return str(random.randint(101,998))
	
	def rellenar(self,numero):
		numero_f = numero
		for i in range(0,16-len(numero)):
			numero_f+="x"
		return numero_f
	
		
if __name__ == "__main__":
	argv = sys.argv
	if(len(argv) > 2):
		bin_generar = str(argv[1])
		num = Generar_tarjeta(bin_generar,int(argv[2]),True)
	else:
		print("USO:  BIN DE YOUTUBE PREMIUN / EEUU")

# Bin para Youtube Premiun IP=USA
#CODIGO POSTAL = 10080

print("")
print("[+]Escoja ,copie e ingrese un bin")
print("---------------------------------------")
print("|               ,,,,,,,               |")
print("|                *BINS                |")
print("|               ```````               |")
print("| 424094011632xxxx   4240940578xxxxxx |")
print("| 424094000830xxxx   424094002574xxxx |")
print("| 4240940340xxxxxx   489504252230xxxx |")
print("|_____________________________________|")
print("")

bin_muestra = input("[+]Ingrese el bin: ")
#imprimir resultado en consola
print("")
print("Generando Bins ...")
system("sleep 3")
print("")
num = Generar_tarjeta(bin_muestra,16,True)
print("")
print("----------------------------------------------------")
print("Asociar su cuenta gmail a Google play")
print("Ponen el número de la tarjeta más mm/aa ,cvv")
print("Elijen el país Estados Unidos, codigo postal 10080")
print("")
print("\033[1;33mDesea continuar usando el programa \033[1;37msi/no")
volver = input("\033[1;37m>>> ")

if volver == "si":                                                  
         system("python scream.py")
else:
         print("")                         
         print(" \033[1;37m[+]\033[1;32mSCREAM BIN ,BYE")
         system("sleep 1")
         exit()
#num = Generar_tarjeta(bin_muestra,1)
#print()
#obtener diccionario
#diccionario = num.dic_tarjetas
#for e in diccionario:
#	print(e,diccionario[e])
#obtener un json para parsear
#json = num.json()

#obtener lista
#lista = num.lista_tarjetas





