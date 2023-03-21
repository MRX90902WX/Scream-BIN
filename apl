#! /bin/bash

echo ""
echo -e "\e[1;33m☆☆\e[0m\e[1;34m☆☆\e[0m\e[1;31m☆☆\e[0m\e[1;32mAPKS-PREMIUN\e[0m\e[1;33m☆☆\e[0m\e[1;34m☆☆\e[0m\e[1;31m☆☆\e[0m"
echo ""
sleep 2
echo -e -n "\e[1;37m[\e[0m\e[1;33m~\e[0m\e[1;37m]\e[0m\e[1;33mDescargar start+,spotify,playhub premiun:\e[0m "
read des
echo ""
echo -e "\e[1;33mCopia el enlace y pegalo en tu navegador\e[0m"
echo ""
echo -e "\e[1;33mEnlace:\e[0m\e[1;37mhttps://drive.google.com/drive/folders/1MAyZ0XXY0q7pLaCWwP3JdhHfP_aXJaQS\e[0m"
echo ""
while :
do
echo ""
echo -e "\e[1;32mDesea continuar usando el programa\e[0m \e[1;37msi/no\e[0m"
echo -e -n "\e[1;37m>>> \e[0m"
read menu                                                                     
case $menu in
si)
#! /bin/bash                                                                  
python scream.py
exit
;;
no)
#! /bin/bash
echo -e "\e[1;37m[+]\e[0m \e[1;32mSCREAM BIN ,BYE\e[0m"
sleep 1
exit
;;
esac
done
