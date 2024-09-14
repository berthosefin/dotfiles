#!/bin/sh

# ----------------------------------------------
# Description : ColorScheme Switcher
# Author : Berthose Fin (Thos)
# Date : 2024-09-12
# ----------------------------------------------

# Function to change GTK settings
change_gtk_settings() {
  local theme_name="$1"
  local icon_theme="$2"
  local cursor_theme="$3"

  sed -i "s/^gtk-theme-name=.*/gtk-theme-name=${theme_name}/" ~/.config/gtk-3.0/settings.ini
  sed -i "s/^gtk-icon-theme-name=.*/gtk-icon-theme-name=${icon_theme}/" ~/.config/gtk-3.0/settings.ini
  sed -i "s/^gtk-cursor-theme-name=.*/gtk-cursor-theme-name=${cursor_theme}/" ~/.config/gtk-3.0/settings.ini
}

# Function to change wallpaper directory
change_randomwall_image_dir() {
  local image_dir="$1"

  sed -i "s|^image_dir=.*|image_dir=\"${image_dir}\"|" ~/.config/i3/scripts/randomwall.sh
  pkill -f randomwall
  sleep 0.5
  nohup sh ~/.config/i3/scripts/randomwall.sh >/dev/null 2>&1 &
}

# Function to change notification colors
change_dunst_colors() {
  ln -sf ~/.cache/wal/colors-dunst ~/.config/dunst/dunstrc
  pkill -f dunst
  sleep 0.5
  dunst &
}

# Function to change Mousepad colors
change_mousepad_colors() {
  ln -sf ~/.cache/wal/colors-mousepad.xml ~/.local/share/gtksourceview-4/styles/pywal.xml
}

# Function to change xfce4-terminal colors
change_xfce4_terminal_colors() {
  # Source the pywal color file
  . "${HOME}/.cache/wal/colors.sh"

  # Apply the colors to xfce4-terminal
  xfconf-query -c xfce4-terminal -p /color-cursor -s "${foreground}"
  xfconf-query -c xfce4-terminal -p /color-foreground -s "${foreground}"
  xfconf-query -c xfce4-terminal -p /color-background -s "${background}"
  xfconf-query -c xfce4-terminal -p /tab-activity-color -s "${color6}"
  xfconf-query -c xfce4-terminal -p /color-palette -s "${color0};${color1};${color2};${color3};${color4};${color5};${color6};${color7};${color8};${color9};${color10};${color11};${color12};${color13};${color14};${color15}"
}

# ----------------------------------------------
# Menu
# ----------------------------------------------

# Options
catppuccin_frappe="Catppuccin Frappe"
catppuccin_latte="Catppuccin Latte"
catppuccin_macchiato="Catppuccin Macchiato"
catppuccin_mocha="Catppuccin Mocha"
dracula="Dracula"
gruvbox="Gruvbox"
nord="Nord"
quit="Quit"

# Variable passed to menu tool (rofi for i3, wofi for Hyprland)
options="$catppuccin_frappe\n$catppuccin_latte\n$catppuccin_macchiato\n$catppuccin_mocha\n$dracula\n$gruvbox\n$nord\n\n$quit"

choice=$(echo -e "${options}" | rofi -dmenu -i -l 9 -p 'ColorScheme')

if ! [ "${choice}" ] || [ "${choice}" = $quit ]; then
  printf 'No theme chosen\n' >&2
  exit 1
fi

# Change parameters based on choice
case "${choice}" in
$catppuccin_frappe)
  wal --theme catppuccin-frappe
  bat --theme="Catppuccin Frappe"
  change_gtk_settings "Catppuccin-Frappe-Standard-Blue-Dark" "Papirus-Dark" "Catppuccin-Frappe-Dark-Cursors"
  change_randomwall_image_dir "$HOME/Images/Catppuccin"
  ;;
$catppuccin_latte)
  wal --theme catppuccin-latte -l
  bat --theme="Catppuccin Latte"
  change_gtk_settings "Catppuccin-Latte-Standard-Blue-Light" "Papirus-Light" "Catppuccin-Latte-Dark-Cursors"
  change_randomwall_image_dir "$HOME/Images/Catppuccin"
  ;;
$catppuccin_macchiato)
  wal --theme catppuccin-macchiato
  bat --theme="Catppuccin Macchiato"
  change_gtk_settings "Catppuccin-Macchiato-Standard-Blue-Dark" "Papirus-Dark" "Catppuccin-Macchiato-Dark-Cursors"
  change_randomwall_image_dir "$HOME/Images/Catppuccin"
  ;;
$catppuccin_mocha)
  wal --theme catppuccin-mocha
  bat --theme="Catppuccin Mocha"
  change_gtk_settings "Catppuccin-Mocha-Standard-Blue-Dark" "Papirus-Dark" "Catppuccin-Mocha-Dark-Cursors"
  change_randomwall_image_dir "$HOME/Images/Catppuccin"
  ;;
$dracula)
  wal --theme dracula
  bat --theme="Dracula"
  change_gtk_settings "Dracula" "dracula-icons" "Dracula-cursors"
  change_randomwall_image_dir "$HOME/Images/Dracula"
  ;;
$gruvbox)
  wal --theme gruvbox
  bat --theme="gruvbox-dark"
  change_gtk_settings "Gruvbox-Dark-BL-MOD" "Gruvbox-plus-icon-MOD" "Gruvbox_Cursors_Dark"
  change_randomwall_image_dir "$HOME/Images/Gruvbox"
  ;;
$nord)
  wal --theme nord
  bat --theme="Nord"
  change_gtk_settings "Nordic-darker" "Nordic-Darker" "Nordic-cursors"
  change_randomwall_image_dir "$HOME/Images/Nord"
  ;;
esac

# Others
change_dunst_colors
change_mousepad_colors
change_xfce4_terminal_colors

# Notify user
notify-send -u normal "ColorScheme Changed" "The color scheme has been changed to ${choice}."
