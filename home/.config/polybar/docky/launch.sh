#!/usr/bin/env bash

# Add this script to your wm startup file.

DIR="$HOME/.config/polybar/docky"

# Terminate already running bar instances
killall -q polybar

# Wait until the processes have been shut down
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch the bar on each monitor
if type "xrandr" > /dev/null; then
  for m in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    MONITOR=$m polybar --reload -q main -c "$DIR"/config.ini &
  done
else
  polybar --reload -q main -c "$DIR"/config.ini &
fi
