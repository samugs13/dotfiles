from libqtile import qtile
from libqtile import widget
from libqtile.lazy import lazy

import fontawesome as fa
import os
import re
import socket
import subprocess

terminal ="alacritty"

negro = "#282D39"
blanco = "#ffffff"
gris = "#636A78"
#azul="#000080"
azul="#003366"
azul2 = "84c7e7"
rojo = "#ff5879"
gris2 = "#8292b2"
amarillo = "#EBCB8B"

################################
#            WIDGETS           #
################################

widget_defaults = dict(
    font='Hack',
    fontsize=12,
    padding = 2,
)
extension_defaults = widget_defaults.copy()    

def init_widget_list():
    widget_list = [

                widget.TextBox(
                    font = 'Ubuntu Bold',
                    fontsize = 18,
                    text= fa.icons['toggle-off'] + ' ',
                    background=gris,
                    foreground=blanco,
                    padding = 2,
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn("/home/s4mb4/Escritorio/scripts/dmenu-powermanager.sh")}
                ),

                widget.TextBox(
                    text = fa.icons["bars"],
                    background = gris,
                    foreground = blanco,
                    padding = 2,
                    fontsize = 18,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('dmenu_run')},
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 6,
                    background = gris
                ),

                widget.TextBox(
                    text = '\uf0d9',
                    background = gris,
                    foreground = azul2,
                    padding = 0,
                    fontsize = 37
                ),

                widget.WindowName(
                    foreground=negro,
                    background= azul2,
                    font = "Hack Bold",
                    fontsize = 13,
                    max_chars = 100,
                    padding = 5,
                ),

                widget.TextBox(
                    text = '\uf0da',
                    background = gris,
                    foreground = azul2,
                    padding = 0,
                    fontsize = 37
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                    background = gris
                ),
                
                widget.TextBox(
                    text = '\uf0d9',
                    background = gris,
                    foreground = negro,
                    padding = 0,
                    fontsize = 37
                ),

                widget.GroupBox(
                   font = "Ubuntu Bold",
                   fontsize = 15,
                   margin_y = 3,
                   margin_x = 0,
                   padding_y = 5,
                   padding_x = 3,
                   borderwidth = 3,
                   active = gris2,
                   inactive = blanco,
                   highlight_color = "#5d5d5d",
                   highlight_method="text",
                   this_current_screen_border = rojo,
                   background = negro,
                   foreground = blanco,
                ),
                
                widget.TextBox(
                    text = '\uf0da',
                    background = gris,
                    foreground = negro,
                    padding = 0,
                    fontsize = 37
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                    background = gris
                ),

                widget.TextBox(
                    text = '',
                    background = gris,
                    foreground = azul,
                    padding = 0,
                    fontsize = 37
                ),

                widget.CurrentLayoutIcon(
                    background = azul,
                    foreground = blanco,
                    padding = 3,
                    scale = 0.7

                ),

                widget.CurrentLayout(
                    background = azul,
                    foreground = blanco,
                    padding = 3,
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    background = azul
                ),
                
                widget.TextBox(
                    text = '| '+fa.icons['brain'],
                    foreground = blanco,
                    background = azul,
                    padding = 2,
                ),

                widget.CPU(
                    foreground = blanco,
                    background = azul,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                    format = 'CPU {load_percent}%',
                    padding = 3,
                ),
                
                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    background = azul
                ),

                widget.TextBox(
                    text = '| '+ fa.icons['temperature-low'],
                    foreground = blanco,
                    background = azul,
                    padding = 2,
                ),

                widget.ThermalSensor(
                    background = azul,
                    foreground = blanco,
                    padding = 3,
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e sensors')},
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    background = azul
                ),

                widget.TextBox(
                    text = '| ' + fa.icons['sync-alt'], 
                    background = azul,
                    foreground = blanco,
                    padding = 2,
                ),

                widget.CheckUpdates(
                    update_interval=20, 
                    foreground = blanco,
                    colour_have_updates = blanco,
                    background = azul,
                    distro = 'Arch_checkupdates',
                    display_format = '{updates} updates',
                    no_update_string = 'no updates',
                    padding = 3,
                ),

                 widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    background = azul
                ),

                widget.TextBox(
                   text = '| ' + fa.icons['sun'],
                   background = azul,
                   foreground = blanco,
                   padding = 2,
                ),
                
                widget.Backlight(
                   backlight_name = 'intel_backlight',
                   brightness_file = 'brightness',
                   padding = 3,
                   background = azul,
                   foreground = blanco,
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    background = azul
                ),

                widget.TextBox(
                   text = "| ",
                   background = azul,
                   foreground = blanco,
                   padding = 2,
                ),

                widget.Clock(
                    format='%A %d de %B - %H:%M',
                    background = azul,
                    foreground = blanco,
                    padding = 3,
                    mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " --hold -e cal -n 2")}
                ),

                widget.Sep(
                    linewidth = 0,
                    padding = 3,
                    background = azul
                ),

                widget.TextBox(
                    text = "|",
                    padding = 2,
                    background = azul,
                    foreground = blanco,
                ),

                widget.Systray(
                    padding =1,
                    icon_size = 18,
                    background = azul,
                ),

                widget.TextBox(
                    text = '\uf0da',
                    background = gris,
                    foreground = azul,
                    padding = 0,
                    fontsize = 37
                ),
              ]
    return widget_list
