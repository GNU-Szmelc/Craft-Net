#!/bin/bash
# WORK IN PROGRESS

import subprocess
import os
import threading
import time
import shlex

 #ps -ef | awk '/minecraft/{print $2}'
 #echo $2
#ps -ef | grep 'minecraft' | grep -v grep | awk '{print $2}'
#echo $2
subprocess.Popen("ps -ef | grep 'minecraft' | grep -v grep | awk '{print $2}'", shell=True),
subprocess.Popen(["kill (echo $2=awk)"], shell=True)

 #eval "echo $2!" | ""
# kill -l | grep 'minecraft' | grep -v grep | awk '{print $2}'
