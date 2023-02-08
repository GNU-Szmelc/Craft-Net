#!/bin/bash

# BATCH SKYNETFLAYER SCRIPT
# Execute any ammount of bot.js scripts with batch.py
# 5 loops
# 5s delay

import subprocess
import os
import threading
import time
import shlex

count = 0
while (count < 5):
    count = count + 1
    subprocess.Popen('node bot.js', shell=True),
    time.sleep(5)
