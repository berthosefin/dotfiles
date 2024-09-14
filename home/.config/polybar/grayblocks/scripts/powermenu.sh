#!/usr/bin/env bash

uptime=$(uptime -p | sed -e 's/up //g')
dir="~/.config/rofi"
rofi_command="rofi -no-config -theme $dir/config.rasi"

# Options
shutdown=" Poweroff"
reboot=" Reboot"
suspend=" Suspend"
lock=" Lock"
logout=" Logout"

# Variable passed to rofi
options="$lock\n$suspend\n$logout\n$reboot\n$shutdown"

chosen="$(echo -e "$options" | $rofi_command -dmenu -selected-row 0 -l 5 -p "Uptime: $uptime")"

case $chosen in
    $shutdown)
			systemctl poweroff
      ;;
    $reboot)
			systemctl reboot
      ;;
    $lock)
			betterlockscreen -l blur
      ;;
    $suspend)
			systemctl suspend
      ;;
    $logout)
    	i3-msg exit
      ;;
esac
