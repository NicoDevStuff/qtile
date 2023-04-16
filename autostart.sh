#! /bin/bash
~/.screenlayout/main.sh &
picom &
nm-applet &
volumeicon &
# for laptop users only!
# cbatticon &
blueman-applet &
conky -c ~/.config/conky/qtile/conky.conf
udiskie &
easyeffects &
solaar &
xclip &
nitrogen --restore &  
