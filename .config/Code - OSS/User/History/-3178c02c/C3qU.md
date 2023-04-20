# Dotfiles
My personal backup of my dotfiles.

## Previews
![img-3](https://raw.githubusercontent.com/berthosefin/dotfiles/main/Previews/img-1.png)
![img-1](https://raw.githubusercontent.com/berthosefin/dotfiles/main/Previews/img-1.png)
![img-2](https://raw.githubusercontent.com/berthosefin/dotfiles/main/Previews/img-2.png)

## Details
- **Display Server** X11
- **Display Manager** LightDM
- **Greeter** LightDM Webkit2 Greeter
- **Desktop Environment** Xfce
- **WM** Xfwm4, i3-gaps
- **Launcher** Rofi, Ulauncher
- **Panel** Xfce4-panel, Polybar
- **Compositor** Picom-ibhagwan-git
- **GTK+ Theme Switcher** Lxappearance
- **GTK Theme** Fluent-light, Nordic-Darker
- **Icons** Fluent, Nord-Darker
- **GTK Fonts** Iosevka Custom
- **File Manager** Thunar
- **Web Browser** Firefox
- **Task Manager** Htop
- **Power Manager** Tlp
- **Image Viewer** Ristretto, Viewnior, Feh
- **Sound Mixer** PulseAudio
- **Terminal** Alacritty, Xfce4-terminal
- **CLI Shell** Zsh
- **Archiver** File-roller
- **Notification Daemon** Dunst
- **Graphic Editor** Gimp
- **CLI Text Editor** Vim
- **GUI Text Editor** Code - OSS
- **CLI Music Player** Ncmpcpp
- **GUI Music Player** Rhythmbox
- **Media Player** Mpv, Vlc
- **Policy Kit Frontend** Polkit-gnome
- **Screenshooter** Scrot, Xfce4-screenshooter
- **Wallpaper Handler** Feh, Pywal

## Keybinds & Mousebinds
- **Super + Enter** launch alacritty
- **Super + Shift + Enter** launch xfce4-terminal
- **Super + Shift + w** launch firefox
- **Super + Shift + f** launch thunar
- **Super + d** launch rofi
- **Ctrl + Space** launch ulauncher
- **Ctrl + Print** xfce4-screenshooter
- **Print** scrot
- **Super + h,j,k,l** change focus
- **Super + Arrows** change focus
- **Super + Shift + h,j,k,l** move focused window
- **Super + Shift + Arrows** move focused window
- **Super + 1-9** switch to workspace 1-9
- **Super + Shift + 1-9** move focused container to workspace 1-9
- **Alt + Tab** workspace next
- **Alt + Shift + Tab** workspace prev
- **Super + q** kill focused window
- **Super + f** fullscreen toggle
- **Super + s** layout toggle split
- **Super + z** layout stacking
- **Super + w** layout tabbed
- **Alt + h** split in horizontal orientation
- **Alt + v** split in vertical orientation
- **Super + Space** floating toggle
- **Super + Shift + Space** focus mode_toggle
- **Super + r** mode resize
- **Super + g** mode gaps
- **Alt + l** lock screen
- **Super + e** launch powermenu
- **Super + Shift + e** exit i3
- **Super + Shift + r** restart i3
- **Super + Shift + c** reload i3 configuration
- ..More keybinds just read the *~/.config/i3/config* file

## Notes
- If you want to use this configuration, inspect the code before use.
- Install git
- Clone this repo `git clone --depth=1 https://github.com/berthosefin/dotfiles ~/.dotfiles`
- Deploy the dotfiles `cp -rv ~/.dotfiles/* ~`
- Change the default CLI Shell `chsh $(whoami) -s /bin/zsh`
- If you find "thos" in the configuration file, replace it with your own username.
- Edit some system configuration, example in ~/.dotfiles/.system
- Reboot
- Fix some errors
- Start working
