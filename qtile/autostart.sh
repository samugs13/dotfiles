#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

setxkbmap es  # Keyboard layout

feh --bg-fill /home/s4mb4/.config/qtile/wallpapers/train.jpg  # Set wallpaper

onedriver /home/s4mb4/OneDrive &  # Automount my One Drive files

#starting utility applications at boot time
run nm-applet &
run pamac-tray &
run xfce4-power-manager &
numlockx on &
blueberry-tray &
run cbatticon -i notification &
run volumeicon &
#run variety &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &

