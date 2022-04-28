#!/bin/sh

setxkbmap fr
xmodmap $HOME/.xmodmaprc
xrdb $HOME/.Xressources

# Start i3 and log to ~/.config/i3/logfile
echo "Starting at $(date)" >> ~/.config/i3/logfile
exec /usr/bin/i3 -V -d all >> ~/.config/i3/logfile
