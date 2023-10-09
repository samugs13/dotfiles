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
numlockx on
blueberry-tray
run cbatticon -i notification   # Battery systray icon
run volumeicon
run flameshot
picom --config $HOME/.config/qtile/settings/scripts/picom.conf
run xautolock -time 10 -locker slock
