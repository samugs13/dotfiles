#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

setxkbmap es  # Keyboard layout

feh --bg-fill /home/s4mb4/.config/qtile/wallpapers/train.jpg  # Set wallpaper

#starting utility applications at boot time
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
run cbatticon -i notification &
run volumeicon &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
run xautolock -time 10 -locker slock

