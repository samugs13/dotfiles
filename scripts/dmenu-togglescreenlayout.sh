#!/usr/bin/bash

r=$(echo -e ":b   PC\n:p   HDMI\n:h   Duplicar pantalla\n:g   Multimonitor" | dmenu -p "Layout:" -c -l 4 -h -1 -sb "#e5c07b")

case "$r" in
     ":b   PC") xrandr --output HDMI-1 --off --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal ;;
     ":p   HDMI") xrandr --output eDP-1 --off --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal ;;
     ":h   Duplicar pantalla") xrandr --output HDMI-1 --mode 1920x1080 --pos 0x0 --rotate normal --output eDP-1 --mode 1920x1080 --pos 0x0 --rotate normal ;;
     ":g   Multimonitor") xrandr --output HDMI-1 --mode 1920x1080 --rate 75 --pos 0x0 --output eDP-1 --mode 1920x1080 --left-of HDMI-1 && qtile cmd-obj -o cmd -f restart ;;
esac
