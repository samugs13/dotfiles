#!/usr/bin/bash

r=$(echo -e ":r  Apagar\n:r  Reiniciar\n:r  Suspender\n:r  Cerrar Sesión" | dmenu -p "" -c -l 4 -h -1 -sb "#c792eb")

case "$r" in
     ":r  Apagar") poweroff ;;
     ":r  Reiniciar") reboot ;;
     ":r  Suspender") systemctl suspend && slock ;;
     ":r  Cerrar Sesión") killall qtile ;;
esac
