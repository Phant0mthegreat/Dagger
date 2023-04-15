import phonenumbers
import re
import random 
import colorama
from colorama import Fore
from colorama import Style
from os import system
import sys
import time
import random
import string
import pathlib
from phonenumbers import carrier
from phonenumbers import geocoder

#colors--
black="\033[0;30m"
red="\033[0;31m"
bred="\033[1;31m"
green="\033[0;32m"
bgreen="\033[1;32m"
yellow="\033[0;33m"
byellow="\033[1;33m"
blue="\033[0;34m"
bblue="\033[1;34m"
purple="\033[0;35m"
bpurple="\033[1;35m"
cyan="\033[0;36m"
bcyan="\033[1;36m"
white="\033[0;37m"
nc="\033[00m"
#colors--
while True:
 system("clear")
 print(f"""
{bred}      :::::::::           :::        ::::::::       ::::::::       ::::::::::       :::::::::
     :+:    :+:        :+: :+:     :+:    :+:     :+:    :+:      :+:              :+:    :+:
    +:+    +:+       +:+   +:+    +:+            +:+             +:+              +:+    +:+
   +#+    +:+      +#++:++#++:   :#:            :#:             +#++:++#         +#++:++#:
  +#+    +#+      +#+     +#+   +#+   +#+#     +#+   +#+#      +#+              +#+    +#+
 #+#    #+#      #+#     #+#   #+#    #+#     #+#    #+#      #+#              #+#    #+#
#########       ###     ###    ########       ########       ##########       ###    ###
{byellow} Developed by Phant0m The Great{white}
""")
 print(f"""[{bcyan}!{white}] Enter the number you want to query (use a valid format, example: {purple}+5521999999999{white})""")
 print('')
 telefone = input(f"""[{blue}?{white}] Number >>> """)
 pattern = re.compile(r'\s+')
 telefone = re.sub(pattern, '', telefone)
 (len(telefone))
 if len(telefone) > 14:
   print('')
   print(f"""[{yellow}#{white}] Number too big, check.""")
 if len(telefone) < 14:
   print('')
   print(f"""[{yellow}#{white}] Number too small, check""")
#system.number-
 telefone_ajustado = phonenumbers.parse(telefone)
 local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
 operadora = carrier.name_for_number(telefone_ajustado,'pt-br')
#system.number-
 print('')

 print(f"""[{cyan}${white}] {telefone_ajustado}""")
 print(f"""[{cyan}${white}] State: {local}""")
 print(f"""[{cyan}${white}] Operator: {operadora}""") 
 print('')
 input('[?] Do you want to make another query? if yes, press enter.')
