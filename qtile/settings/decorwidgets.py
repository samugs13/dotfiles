################################
#            WIDGETS           #
################################

import fontawesome as fa

from libqtile import bar
from qtile_extras import widget
from libqtile import qtile

from .keys import terminal 
from .colors import onedark 
from .scripts import getIP
from .decorations import rect, redb, greenb, yellowb, purpleb, cyanb

ip=getIP.ip

widget_defaults = dict(
    font='Hack',
    fontsize=14,
    padding = 2,
)
extension_defaults = widget_defaults.copy()

altwidgets = [

    widget.GroupBox(
       font = 'Font Awesome 6 Free Solid',
       active = onedark[4],
       inactive = onedark[7],
       highlight_method="border",
       borderwidth = 2,
       this_current_screen_border = onedark[4],
       block_highlight_text_color = onedark[7],
       highlight_color = onedark[0],
       center_aligned = True,
       background = onedark[0],
       fontsize = 14,
       disable_drag = True,
       padding_y = 7,
       padding_x = 3,
    ),

    widget.Sep(),
    
    widget.WindowName(
        padding = 7,
        max_chars = 38,
        foreground = onedark[7],
        font = 'Hack Bold',
        fontsize = 14,
        empty_group_string = 'Desktop'
    ),

    widget.Spacer(length=bar.STRETCH),
    
    widget.Clock(
    font = 'Hack Nerd Font',
    foreground=onedark[0],
    format= fa.icons['clock'] + ' %H:%M ' + fa.icons['calendar-alt'] + ' %a, %d de %h de %Y',
    **rect),
     
    widget.Spacer(length=bar.STRETCH),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['sun'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **redb
    ),

    widget.Backlight(
        backlight_name = 'intel_backlight',
        brightness_file = 'brightness',
        fmt = '{}',
        padding = 5,
        foreground = onedark[7],
        background = onedark[0],
    ),
    
    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['keyboard'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **purpleb
    ),

    widget.KeyboardLayout(
        configured_keyboards = ['es','us'],
        fmt = '{}',
        background = onedark[0],
        padding = 5,
        foreground = onedark[7], 
    ), 

    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['user-secret'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **greenb
    ),

    widget.TextBox(
        text = ip,
        padding = 5,
        foreground = onedark[7],
        background = onedark[0],
    ),

    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['download'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **cyanb
    ),

    widget.CheckUpdates(
        update_interval=20,
        foreground = onedark[7],
        colour_have_updates = onedark[7],
        colour_no_updates = onedark[7],
        distro = 'Arch_checkupdates',
        display_format = '{updates} updates',
        no_update_string = 'updated',
        padding = 5,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " -e sudo pacman -Syu")},
        background = onedark[0],
    ),

     widget.Spacer(
        length = 5,
    ),

    widget.CurrentLayoutIcon(
        foreground = onedark[7],
        padding = 8,
        scale = 0.45,
        background = onedark[0],
        **yellowb
    ),

    widget.Spacer(
        length = 5,
    ),

    widget.CurrentLayout(
        foreground = onedark[7],
        padding = 0,
        background = onedark[0],
        fmt = '{} '
    ),
    
    widget.Sep(),
    
    # widget.Spacer(
    #     length = 5,
    # ),

    # widget.ALSAWidget(
    #      mode = 'both',
    #      theme_path = "/usr/share/icons/Papirus"
    # ),

    # widget.WiFiIcon(
    #     interface = 'wlo1',
    #     inactive_colour = onedark[7],
    #     fontsize = 11,
    # ),

    widget.Spacer(
        length = 5,
    ),

    widget.UPowerWidget(
        padding = 2,
        border_charge_colour = onedark[4],
        border_colour = onedark[7],
        border_critical_colour = onedark[1],
        fill_low = onedark[3],
        percentage_critical = 0.2,
        percentage_low = 0.3,
    ),

    widget.Systray(
        padding = 2,
    ),

    widget.Spacer(
        length = 5,
    ),

    widget.WidgetBox(widgets=[
                    
        widget.LaunchBar(
            progs=[
                (fa.icons['discord'], 'brave --new-window https://www.discord.com', 'Discord'),
                (fa.icons['github'], 'brave --new-window https://www.github.com', 'Github'),
                (fa.icons['reddit-alien'], 'brave --new-window https://www.reddit.com', 'Reddit'),
                (fa.icons['twitch'], 'brave --new-window https://www.twitch.com', 'Twitch'),
                (fa.icons['youtube'], 'brave --new-window https://www.youtube.com', 'Youtube'),
                (fa.icons['spotify'], 'spotify', 'Spotify'),
                (fa.icons['skype'], 'skypeforlinux', 'Skype'),
            ],
        ),
    ],
        font = 'Font Awesome 6 Free',
        fontsize = 14,
        foreground = onedark[7],
        background = onedark[0],
        text_closed = fa.icons['pager'],
        text_open = '|',
    ),

    widget.Spacer(
        length=8,
    ),
]

altwidgets2 = [
    
    widget.CurrentScreen(
        padding = 8,
        active_text = 'A',
        inactive_text = 'I',
    ),

    widget.Sep(),

    widget.GroupBox(
       font = 'Font Awesome 6 Free Solid',
       active = onedark[4],
       inactive = onedark[7],
       highlight_method="border",
       borderwidth = 2,
       this_current_screen_border = onedark[4],
       block_highlight_text_color = onedark[7],
       highlight_color = onedark[0],
       center_aligned = True,
       background = onedark[0],
       fontsize = 14,
       disable_drag = True,
       padding_y = 7,
       padding_x = 3,
       visible_groups=[fa.icons['terminal'], fa.icons['globe'], fa.icons['edit'], fa.icons['code'], fa.icons['tv']],
    ),

    widget.Sep(),
    
    widget.WindowName(
        padding = 7,
        max_chars = 200,
        foreground = onedark[7],
        font = 'Hack Bold',
        fontsize = 14,
        empty_group_string = 'Desktop'
    ),

    widget.Spacer(length=bar.STRETCH),
    
    widget.Clock(
    font = 'Hack Nerd Font',
    foreground=onedark[0],
    format= fa.icons['clock'] + ' %H:%M ' + fa.icons['calendar-alt'] + ' %a, %d de %h de %Y',
    **rect),
     
    widget.Spacer(length=bar.STRETCH),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['sun'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **redb
    ),

    widget.Backlight(
        backlight_name = 'intel_backlight',
        brightness_file = 'brightness',
        fmt = '{}',
        padding = 5,
        foreground = onedark[7],
        background = onedark[0],
    ),
    
    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['keyboard'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **purpleb
    ),

    widget.KeyboardLayout(
        configured_keyboards = ['es','us'],
        fmt = '{}',
        background = onedark[0],
        padding = 5,
        foreground = onedark[7], 
    ), 

    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['user-secret'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **greenb
    ),

    widget.TextBox(
        text = ip,
        padding = 5,
        foreground = onedark[7],
        background = onedark[0],
    ),

    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['download'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **cyanb
    ),

    widget.CheckUpdates(
        update_interval=20,
        foreground = onedark[7],
        colour_have_updates = onedark[7],
        colour_no_updates = onedark[7],
        distro = 'Arch_checkupdates',
        display_format = '{updates} updates',
        no_update_string = 'updated',
        padding = 5,
        mouse_callbacks = {"Button1": lambda: qtile.cmd_spawn(terminal + " -e sudo pacman -Syu")},
        background = onedark[0],
    ),

     widget.Spacer(
        length = 5,
    ),

    widget.CurrentLayoutIcon(
        foreground = onedark[7],
        padding = 8,
        scale = 0.45,
        background = onedark[0],
        **yellowb
    ),

    widget.Spacer(
        length = 5,
    ),

    widget.CurrentLayout(
        foreground = onedark[7],
        padding = 0,
        background = onedark[0],
        fmt = '{} '
    ),
    
    widget.Sep(),

    widget.LaunchBar(
        progs=[
            (fa.icons['discord'], 'brave --new-window https://www.discord.com', 'Discord'),
            (fa.icons['github'], 'brave --new-window https://www.github.com', 'Github'),
            (fa.icons['reddit-alien'], 'brave --new-window https://www.reddit.com', 'Reddit'),
            (fa.icons['twitch'], 'brave --new-window https://www.twitch.com', 'Twitch'),
            (fa.icons['youtube'], 'brave --new-window https://www.youtube.com', 'Youtube'),
            (fa.icons['skype'], 'skypeforlinux', 'Skype'),
        ],
    ),

    widget.Spacer(
        length=5,
    ),
]

altwidgets3 = [
    
    widget.CurrentScreen(
        padding = 8,
        active_text = 'A',
        inactive_text = 'I',
    ),

    widget.Sep(),

    widget.GroupBox(
       font = 'Font Awesome 6 Free Solid',
       active = onedark[4],
       inactive = onedark[7],
       highlight_method="border",
       borderwidth = 2,
       this_current_screen_border = onedark[4],
       block_highlight_text_color = onedark[7],
       highlight_color = onedark[0],
       center_aligned = True,
       background = onedark[0],
       fontsize = 14,
       disable_drag = True,
       padding_y = 7,
       padding_x = 3,
       visible_groups=[fa.icons['folder-open'], fa.icons['video'], fa.icons['music'], fa.icons['comment-dots'], fa.icons['envelope']],
    ),

    widget.Sep(),
    
    widget.WindowName(
        padding = 7,
        max_chars = 100,
        foreground = onedark[7],
        font = 'Hack Bold',
        fontsize = 14,
        empty_group_string = 'Desktop'
    ),
    
    widget.Spacer(
         length = 5
    ),

    widget.Mpris2(
        fmt = fa.icons['spotify'] + ' {}',
        foreground = onedark[0],
        name='spotify',
        objname="org.mpris.MediaPlayer2.spotify",
        display_metadata=['xesam:title', 'xesam:artist'],
        scroll_chars=None,
        stop_pause_text=fa.icons['play'],
        **rect 
    ),

    widget.Spacer(
        length = 30,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['brain'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **redb
    ),

    widget.CPU(
        format = 'CPU {load_percent}%',
        padding = 5,
        foreground = onedark[7],
        background = onedark[0],
    ),
    
    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['hdd'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **purpleb
    ),

    widget.DF(
        visible_on_warn = False,
        format = '{p}: {uf}{m} free',
        padding = 5,
        foreground = onedark[7],
        background = onedark[0],
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e df -h')},
    ),

    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['network-wired'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **greenb
    ),

    widget.Wlan(
            interface = 'wlo1',
        font = 'Hack Nerd Font',
        fmt = '{}',
        padding = 5,
        foreground = onedark[7],
        background = onedark[0],
    ),

    widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['temperature-low'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **cyanb
    ),

    widget.ThermalSensor(
        foreground = onedark[7],
        padding = 5,
        background = onedark[0],
    ),

     widget.Spacer(
        length = 5,
    ),

    widget.TextBox(
        font = 'Font Awesome 6 Free',
        text = fa.icons['city'],
        padding = 8,
        foreground = onedark[7],
        background = onedark[0],
        **yellowb
    ),

    widget.OpenWeather(
        location = 'Madrid',
        foreground = onedark[7],
        padding = 5,
        background = onedark[0],
    ),

    widget.Spacer(
        length = 5,
    ),
    
    widget.Sep(),
   
    widget.Spacer(
        length = 5,
    ),

    widget.UPowerWidget(
        padding = 2,
        border_charge_colour = onedark[4],
        border_colour = onedark[7],
        border_critical_colour = onedark[1],
        fill_low = onedark[3],
        percentage_critical = 0.2,
        percentage_low = 0.3,
    ),

    widget.Systray(
        padding = 2,
    ),

    widget.Spacer(
        length=5,
    ),
]
