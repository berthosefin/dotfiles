#!/bin/bash

image_dir="/home/thos/Images/Nord"

while true; do
  feh --bg-fill "$(find $image_dir -type f \( -name '*.jpg' -o -name '*.png' \) | shuf -n 1)"
  sleep 600s
done &
