#!/bin/bash

function run {
    if ! pgrep $1;
    then
        $@&
    fi
}

# Set Wallpaper
#run ~/.fehbg &
run feh --randomize --bg-fill ~/Images/Nord/* &

# Run compositor
run picom &

# Run polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Run conky
conky -c ~/.config/conky/holybible.conf &
conky -c ~/.config/conky/datetime.conf &

# Others
run dunst &
run mpd &
run redshift &
run xsettingsd &
run xfce4-power-manager &
run xrdb ~/.Xresources &
run xset +fp ~/.fonts/misc &
