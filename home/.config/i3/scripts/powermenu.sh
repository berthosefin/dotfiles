#!/usr/bin/env bash

# Get system uptime
uptime=$(uptime -p | sed -e 's/up //g')

# Define options
shutdown=" Poweroff"
reboot=" Reboot"
suspend=" Suspend"
lock=" Lock"
logout=" Logout"
options="$lock\n$suspend\n$logout\n$reboot\n$shutdown"

chosen="$(echo -e "$options" | rofi -dmenu -l 5 -p "Uptime: $uptime")"

# Execute the corresponding command
case $chosen in
$shutdown)
  systemctl poweroff
  ;;
$reboot)
  systemctl reboot
  ;;
$lock)
  sh ~/.config/i3/scripts/lock.sh
  ;;
$suspend)
  systemctl suspend
  ;;
$logout)
  i3-msg exit
  ;;
esac
