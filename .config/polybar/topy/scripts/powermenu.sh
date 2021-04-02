	#!/bin/bash

## By Birkhoff

MENU="$(rofi -sep "|" -dmenu -i -p 'System' -width 12 -hide-scrollbar -line-padding 4 -padding 20 -lines 5 -theme ~/.config/polybar/topy/scripts/rofi/config.rasi <<< "> Lock|> Exit|> Suspend|> Reboot|> Shutdown")"
            case "$MENU" in
		*Lock) ~/.bin/blurlock ;;
		*Exit) i3-msg exit ;;
        	*Suspend) systemctl suspend ;;
		*Reboot) systemctl reboot ;;
		*Shutdown) systemctl poweroff
            esac
