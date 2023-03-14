#! /bin/bash

clear
cd Card-extrapolaccion
echo ""
echo -e "\e[1;33m╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮\e[0m"
echo -e "\e[1;33m┃╭━━╯╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱┃┃\e[0m"
echo -e "\e[1;33m┃╰━━┳╮┣╮╭╋━┳━━┳━━┳━━┫┃╭━━┳━━┳━━┳┳━━┳━╮\e[0m"
echo -e "\e[1;34m┃╭━━┻╋╋┫┃┃╭┫╭╮┃╭╮┃╭╮┃┃┃╭╮┃╭━┫╭━╋┫╭╮┃╭╮╮\e[0m"
echo -e "\e[1;34m┃╰━━┳╋╋┫╰┫┃┃╭╮┃╰╯┃╰╯┃╰┫╭╮┃╰━┫╰━┫┃╰╯┃┃┃┃\e[0m"
echo -e "\e[1;34m╰━━━┻╯╰┻━┻╯╰╯╰┫╭━┻━━┻━┻╯╰┻━━┻━━┻┻━━┻╯╰╯\e[0m"
echo -e "\e[1;31m╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃\e[0m"
echo -e "\e[1;31m╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯\e[0m"
echo ""
echo -e "\e[1;36mFacebook:\e[0m \e[1;37mhttps://www.facebook.com/jimber.cevallos\e[0m"
echo ""
echo -e -n "\e[1;31m[\e[0m\e[1;36m♤\e[0m\e[1;31m]\e[0m\e[1;32mEscriba un puerto >>\e[0m \e[1;37m\e[0m"
read puerto
echo ""
setterm -foreground red
echo "# Iniciando localhost al puerto $puerto ..."
echo ""
sleep 2
setterm -foreground blue
echo "-----------------------------------"
setterm -foreground yellow
echo "Extrapole sus targetas cc en un bin"
echo "Entrando en el siguiente link "
echo "Copielo y peguelo en su navegador"
setterm -foreground blue
echo "-----------------------------------"
echo ""
setterm -foreground green                            
echo "------------------------------"
setterm -foreground cyan
echo "Link = http://localhost:$puerto"
setterm -foreground green
echo "------------------------------"
echo ""
php -S 0.0.0.0:$puerto 
