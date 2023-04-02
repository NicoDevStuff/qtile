#! /bin/bash
picom &
nm-applet &
volumeicon &
# for laptop users only!
# cbatticon &
conky -c ~/.config/conky/qtile/conky.conf
~/.screenlayout/main.sh &
udiskie &
easyeffects &
solaar &
xclip &
nitrogen --restore &  
