#!/bin/bash
# Crappiest multi instance execute script ever

import subprocess
import os
import threading
import time
import shlex

#FANCY PRINT
print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print('')
print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print('')
print('--------------------------------------')
print('--                                  --')
print('--      > SKY-NET $hell  [v1.1]     --')
print('--                                  --')
print('--         [ 420666#9452 ]          --')
print('--                                  --')
print('--------------------------------------')
print("-------    Server to join?:    -------")
print('--------------------------------------')
print("--- -- * Leave blank for null * -- ---") #(null=null)
print("-- *  PREPPEND -s  * :  [-s <ip>] * --")
print('--------------------------------------')
print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print(''), '\n',print('')

inst = ['-l QUICKSILVER[1] ','eeee']
usr = ['-a Arch_x64 ','eeee']

#INPUT FIELD 1
search = input('>  ')

#FANCY PRINT 2
print(''), '\n',print('')
print('------------------------------')
print('... EXECUTING SKYNET SHELL ...')
print('------------------------------')
print(''), '\n', print('')

#INSTANCES
#10s Delay for good measure

subprocess.Popen('mplayer loading.mp4', shell=True)

# TO DO
# - Make Instance & User into array / list (alternatively read from .txt file)

print("- LAUNCHING CLIENT [#1]"),'\n',time.sleep(1),'\n',print(""), #PRINT
subprocess.Popen('prismlauncher -l QUICKSILVER[1] -a Silverainox ' + search, shell=True)
print("  - [10s Delay] -  "),'\n',time.sleep(10),'\n',print(""), #PRINT
print("- LAUNCHING CLIENT [#2]"),'\n',time.sleep(1),'\n',print(""), #PRINT
subprocess.Popen('prismlauncher -l QUICKSILVER[2] -a serainox ' + search, shell=True)

#print("- LAUNCHING CLIENT [#1]"),'\n',time.sleep(1),'\n',print(""), #PRINT
#subprocess.Popen(["prismlauncher -l QUICKSILVER[1] -a [usr:1]"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True),
#subprocess.Popen('prismlauncher -l QUICKSILVER[1] -a Silverainox ' + search, shell=True)
#subprocess.Popen("prismlauncher " + inst[1] + usr[1] + search, shell=True),
#stdout=subprocess.PIPE, stderr=subprocess.PIPE
# Bashton3 / PyShell3
# By Silverainox
# Dc: 420666#9452
# TO DO
# - Make Instance & User into array / list (alternatively read from .txt file)
#print("  - [10s Delay] -  "),'\n',time.sleep(10),'\n',print(""), #PRINT
#print("- LAUNCHING CLIENT [#2]"),'\n',time.sleep(1),'\n',print(""), #PRINT
#print("eeeeeeee") #PRINT
#subprocess.Popen('prismlauncher -l QUICKSILVER[2] -a serainox ' + search, shell=True)

