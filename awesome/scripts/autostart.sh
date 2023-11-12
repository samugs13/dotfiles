#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

setxkbmap es  # Keyboard layout

#starting utility applications at boot time
numlockx on
run nm-applet
blueberry-tray
run cbatticon -i notification   # Battery systray icon
run volumeicon
run flameshot
run solaar --window=hide
xautolock -time 10 -locker slock
