#!/bin/bash

# Get Volume
get_volume() {
  volume=$(pamixer --get-volume)
  echo "$volume"
}

# Notify
notify_user() {
  notify-send -h string:x-canonical-private-synchronous:sys-notify -u low "Volume : $(get_volume)"
}

# Increase Volume
inc_volume() {
  pamixer -i 5 && notify_user
}

# Decrease Volume
dec_volume() {
  pamixer -d 5 && notify_user
}

# Toggle Mute
toggle_mute() {
  if [ "$(pamixer --get-mute)" == "false" ]; then
    pamixer -m && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low "Volume Switched OFF"
  elif [ "$(pamixer --get-mute)" == "true" ]; then
    pamixer -u && notify-send -h string:x-canonical-private-synchronous:sys-notify -u low "Volume Switched ON"
  fi
}

# Execute accordingly
if [[ "$1" == "--get" ]]; then
  get_volume
elif [[ "$1" == "--inc" ]]; then
  inc_volume
elif [[ "$1" == "--dec" ]]; then
  dec_volume
elif [[ "$1" == "--toggle" ]]; then
  toggle_mute
else
  get_volume
fi
