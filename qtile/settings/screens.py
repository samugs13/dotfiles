################################
#            SCREENS           #
################################

from libqtile.config import Screen
from libqtile import bar
from .colors import colors
from .widgets import primary_widgets, secondary_widgets

screens = [

    Screen(

        #TOP BAR
        top=bar.Bar(primary_widgets, size=23, margin=[7, 7, 0, 7], background=colors[0]), #margin: top,right,bottom,left

        #BOTTOM BAR
        bottom=bar.Bar(secondary_widgets, size=20, margin=[0, 0, 0, 0], background="#00000000"),
    ),
]