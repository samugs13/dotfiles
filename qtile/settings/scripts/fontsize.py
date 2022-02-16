#!/usr/bin/python3

import os 
import subprocess as sp
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove 

home = os.environ['HOME']
temp_path = "%s/.config/alacritty.yml" % home 
file_path = "%s/.config/alacritty/alacritty.yml" % home 

connected_monitors = sp.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=sp.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

def replace(file_path, pattern, subst):
    #Create temp file
    fh, temp_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Copy the file permissions from the old file to the new file
    copymode(file_path, temp_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(temp_path, file_path)

if connected_monitors == 1:
    replace(file_path, "size: 14.0", "size: 12.0")

if connected_monitors == 2:
    replace(file_path, "size: 12.0", "size: 14.0")
