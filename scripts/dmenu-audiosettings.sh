#!/usr/bin/sh
# See available list cards with pactl (pactl list cards | less)

opt1="I/O: Analógico"
opt2="O: HDMI, I: Analógico"

opt="$(printf "$opt1\n$opt2" | dmenu -p "Perfil de audio" -c -l 2)"

case "$opt" in
    "$opt1")
        pactl set-card-profile 0 output:analog-stereo+input:analog-stereo ;;
    "$opt2")
        pactl set-card-profile 0 output:hdmi-stereo+input:analog-stereo ;;
esac
