#! /bin/bash

~/.screenlayout/main.sh &
nitrogen --restore &
nm-applet || nm-applet &
volumeicon || volumeicon &
# for laptop users only!
# is_running cbatticon || cbatticon
conky -c ~/.config/conky/qtile/conky.conf &
udiskie &
xclip &
easyeffects &
solaar &
picom &
dex -vad &
protonvpn &

# No more caps lock
setxkbmap -option caps:none

