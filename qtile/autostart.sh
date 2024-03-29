#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

setxkbmap es  # Keyboard layout

#feh --bg-fill /home/s4mb4/.config/qtile/settings/wallpapers/w003.png  # Set wallpaper 

#starting utility applications at boot time
run nm-applet
#run pamac-tray &
run xfce4-power-manager
numlockx on
blueberry-tray
#run cbatticon -i notification &   # Battery systray icon
run volumeicon
run variety
#wal -R  # -R restores the last colorscheme and wallpaper that was in use
picom --config $HOME/.config/qtile/settings/scripts/picom.conf
dunst
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
run xautolock -time 10 -locker slock

