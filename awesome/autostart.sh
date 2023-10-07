#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

setxkbmap es  # Keyboard layout

#starting utility applications at boot time
run nm-applet
run xfce4-power-manager
numlockx on
blueberry-tray
run cbatticon -i notification   # Battery systray icon
run volumeicon
run variety
picom --config $HOME/.config/qtile/settings/scripts/picom.conf
dunst
run xautolock -time 10 -locker slock
