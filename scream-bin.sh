#! /bin/bash

setterm -foreground blue
git clone https://github.com/MRX90902WX/Card-extrapolaccion
git clone https://github.com/MRX90902WX/MundoBinsRH
clear
chmod 777 scream-bin.sh
echo -e "\e[1;33m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\e[0m"
echo -e "\e[1;33m█\e[0m \e[1;33m╭╮╭╮╭┳━━━┳╮  ╭━━━┳━━━┳━╮╭━┳━━━╮\e[0m \e[1;33m█\e[0m"
echo -e "\e[1;33m█\e[0m \e[1;33m┃┃┃┃┃┃╭━━┫┃╱╱┃╭━╮┃╭━╮┃┃╰╯┃┃╭━━╯\e[0m \e[1;33m█\e[0m"
echo -e "\e[1;33m█\e[0m \e[1;34m┃┃┃┃┃┃╰━━┫┃╱╱┃┃╱╰┫┃╱┃┃╭╮╭╮┃╰━━╮\e[0m \e[1;33m█\e[0m"
echo -e "\e[1;33m█\e[0m \e[1;34m┃╰╯╰╯┃╭━━┫┃╱╭┫┃╱╭┫┃╱┃┃┃┃┃┃┃╭━━╯\e[0m \e[1;33m█\e[0m"
echo -e "\e[1;33m█\e[0m \e[1;31m╰╮╭╮╭┫╰━━┫╰━╯┃╰━╯┃╰━╯┃┃┃┃┃┃╰━━╮\e[0m \e[1;33m█\e[0m"
echo -e "\e[1;33m█\e[0m  \e[1;31m╰╯╰╯╰━━━┻━━━┻━━━┻━━━┻╯╰╯╰┻━━━╯\e[0m \e[1;33m█\e[0m"
echo -e "\e[1;33m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\e[0m"
echo ""
echo -e -n "\e[1;31m[\e[0m\e[1;36m♤\e[0m\e[1;31m]\e[0m\e[1;32mIngresa tu nick binnero:\e[0m \e[1;37m\e[0m"
read nick
echo ""
echo -e "\e[1;33mHola ,\e[0m \e[1;37m$nick\e[0m \e[1;36mencantado de conocerte :)\e[0m"
echo ""
sleep 2
echo -e "\e[1;31m---------------------------------\e[0m"
echo -e "\e[1;36m#\e[0m \e[1;33mGrupo Scream BINS en WhatsApp\e[0m \e[1;36m#\e[0m"
echo -e "\e[1;31m---------------------------------\e[0m"
echo -e "\e[1;32mhttps://chat.whatsapp.com/BQQ9ARePQEJGz99DFz8CN8\e[0m"
echo -e "\e[1;34m__________________________________________________\e[0m"
echo ""
echo -e "\e[1;32mIngreso exitosamente, todas las opciones funcionan\e[0m"
echo ""
echo -e "\e[1;32mLa opción 7 debe crear el archivo\e[0m \e[1;37mcc.txt\e[0m \e[1;32muna vez\e[0m"
echo ""
echo -e "\e[1;32mSe crea por que adentro del txt deben poner las cc\e[0m"
echo ""
echo -e "\e[1;37mEj:\e[0m \e[1;36mcc\e[0m\e[1;31m|\e[0m\e[1;36mmm\e[0m\e[1;31m|\e[0m\e[1;36maaaa\e[0m\e[1;31m|\e[0m\e[1;36mccv\e[0m"
echo -e "\e[1;34m__________________________________________________\e[0m"
while :
do
echo -e "\e[1;33mCree el archivo cc.txt una vez, desea crear\e[0m \e[1;37msi/no\e[0m"
echo -e -n "\e[1;37m>> \e[0m"
read gen
case $gen in
si)
#! /bin/bash
echo ""
touch cc.txt
echo -e "\e[1;37mcc.txt\e[0m \e[1;36mse creo, para la proxima solo responda no\e[0m"
sleep 2
python scream.py
exit
;;
no)
#! /bin/bash
python scream.py
exit
;;
esac
done
