################################
#            SCREENS           #
################################

from libqtile.config import Screen
from libqtile import bar
from .colors import colors, onedark
from .widgets import primary_widgets, secondary_widgets, extra_bottom_widgets
from .decorwidgets import altwidgets, altwidgets2, altwidgets3 

import subprocess 

screens = [

    #Screen(

        #TOP BAR
        #top=bar.Bar(altwidgets, size=30, margin=[0, 0, 0, 0], background=onedark[0]), #margin: top,right,bottom,left
        #top=bar.Bar(primary_widgets, size=23, margin=[7, 7, 0, 7], background=colors[0]), #margin: top,right,bottom,left

        #BOTTOM BAR 
        #bottom=bar.Bar(extra_bottom_widgets, size=20, margin=[0, 0, 0, 0], background="#00000000"),
    #),
]

connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

# if connected_monitors > 1:
#     for i in range(1, connected_monitors):
#         screens.append(Screen(top=bar.Bar(altwidgets2, size=30, background=onedark[0])))

if connected_monitors == 1:
    screens.append(Screen(top=bar.Bar(altwidgets, size=30, background=onedark[0])))

if connected_monitors == 2:
        screens.append(Screen(top=bar.Bar(altwidgets2, size=30, background=onedark[0]))),
        screens.append(Screen(top=bar.Bar(altwidgets3, size=30, background=onedark[0])))
