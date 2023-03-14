#!/usr/bin/python
import random
from os import system

#Code: G.I.T.S 
#Edited: demo-hacks

# Credit card prefixes
visa_prefixes = ['4']
mastercard_prefixes = ['5']
amex_prefixes = ['3']
discover_prefixes = ['6']
diners_prefixes = ['3']

# Card length
visa_length = 16
mastercard_length = 16
amex_length = 15
discover_length = 16
diners_length = 14

# Generate completed credit card number
def generate_credit_card_number(prefix, length):
    ccnumber = list(prefix)
    while len(ccnumber) < (length - 1):
        digit = str(random.randint(0, 9))
        ccnumber.append(digit)

    sum = 0
    pos = 0
    reversedCCnumber = ccnumber[::-1]

    while pos < length - 1:
        odd = int(reversedCCnumber[pos]) * 2
        if odd > 9:
            odd -= 9
        sum += odd

        if pos != (length - 2):
            sum += int(reversedCCnumber[pos + 1])

        pos += 2

    checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
    ccnumber.append(str(int(checkdigit)))
    return ''.join(ccnumber)

# Generate multiple credit card numbers
def generate_credit_card_numbers(prefixes, length, how_many):
    result = []
    for i in range(how_many):
        prefix = random.choice(prefixes)
        ccnumber = generate_credit_card_number(prefix, length)
        result.append(ccnumber)
    return result

# Output credit card numbers
def output(title, numbers):
    result = []
    result.append(title)
    result.append('' * len(title))
    result.append('\n'.join(numbers))
    result.append('')
    return '\n'.join(result)
print("")

# Main program
print(" \033[1;31m--------------------")
print(" \033[1;31m| \033[1;32mGenerador de CCS \033[1;31m|")
print(" \033[1;31m--------------------")
print("")
print(" \033[1;31m1. \033[1;36mVisa")
print(" \033[1;31m2. \033[1;36mMastercard")
print(" \033[1;31m3. \033[1;36mAmerican Express")
print(" \033[1;31m4. \033[1;36mDiscover")
print(" \033[1;31m5. \033[1;36mDiners Club")
print("")

card_type = input(" \033[1;34mOpcion: \033[1;37m")
print("")

if card_type == "1":
    visa_numbers = generate_credit_card_numbers(visa_prefixes, visa_length, 20)
    print(output(" \033[1;37mVisa", visa_numbers))
    print("------------------")
elif card_type == "2":
    mastercard_numbers = generate_credit_card_numbers(mastercard_prefixes, mastercard_length, 20)
    print(output(" \033[1;37mMastercard", mastercard_numbers))
    print("------------------")
elif card_type == "3":
    amex_numbers = generate_credit_card_numbers(amex_prefixes, amex_length, 20)
    print(output(" \033[1;37mAmerican Express", amex_numbers))
    print("-----------------")
elif card_type == "4":
    discover_numbers = generate_credit_card_numbers(discover_prefixes, discover_length, 20)
    print(output(" \033[1;37mDiscover", discover_numbers))
    print("------------------")
elif card_type == "5":
    diners_numbers = generate_credit_card_numbers(diners_prefixes, diners_length, 20)
    print(output(" \033[1;37mDiners", diners_numbers))
    print("----------------")
else:
    print(" \033[1;31m[x]Opcion invalida")
    exit()

print("")
#MENU
print(" \033[1;31m1. \033[1;36mConocer info del bin/cc")
print(" \033[1;31m2. \033[1;36mSalir")

opcion = input(" \033[1;36m>> \033[1;37m")
print("")

if opcion == "1":
    system("python tree.py")
elif opcion == "2":
    exit()
else:
    print(" \033[1;31m[x]Opcion invalida")
