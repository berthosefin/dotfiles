#!/usr/bin/env bash

# Get brightness
get_backlight() {
  MAX=$(brightnessctl max)
  LIGHT=$(printf "%.0f\n" $(brightnessctl get))
  PERCENTAGE=$(expr 100 \* $LIGHT / $MAX)
  echo "${PERCENTAGE}%"
}

# Notify
notify_user() {
  notify-send -h string:x-canonical-private-synchronous:sys-notify -u low "Brightness : $(get_backlight)"
}

# Increase brightness
inc_backlight() {
  brightnessctl set 5%+ && notify_user
}

# Decrease brightness
dec_backlight() {
  brightnessctl set 5%- && notify_user
}

# Execute accordingly
if [[ "$1" == "--get" ]]; then
  get_backlight
elif [[ "$1" == "--inc" ]]; then
  inc_backlight
elif [[ "$1" == "--dec" ]]; then
  dec_backlight
else
  get_backlight
fi
