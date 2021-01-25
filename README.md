# Dotfiles
My personal backup of my dotfiles.

## Previews
### i3-gaps
![alt text](https://raw.githubusercontent.com/berthosefin/dotfiles/main/Images/Previews/preview1.png)
![alt text](https://raw.githubusercontent.com/berthosefin/dotfiles/main/Images/Previews/preview2.png)
### xfce
![alt text](https://raw.githubusercontent.com/berthosefin/dotfiles/main/Images/Previews/preview3.png)

## Details
- **Display Server** X11
- **Display Manager** LightDM
- **Greeter** LightDM Webkit2 Greeter
- **Desktop Environment** Xfce
- **WM** Xfwm4, i3-gaps
- **Launcher** Rofi, Synapse
- **Panel** Polybar
- **Dock** Plank
- **Compositor** Picom-ibhagwan
- **GTK+ Theme Switcher** Lxappearance
- **GTK Theme** Nordic, Nordic-Darker
- **Icons** Nord-Icons
- **GTK Fonts** Iosevka
- **File Manager** Thunar, Nautilus
- **Web Browser** Firefox
- **Task Manager** Htop
- **Power Manager** Tlp
- **Image Viewer** Ristretto, Feh, Sxiv
- **Sound Mixer** PulseAudio
- **Terminal** URxvt, Xfce4-terminal, Gnome-terminal
- **CLI Shell** Zsh
- **Archiver** Xarchiver, File-roller
- **Notification Daemon** Dunst
- **Graphic Editor** Gimp
- **CLI File Manager** Ranger
- **CLI Text Editor** Vim
- **GUI Text Editor** Visual Studio Code
- **CLI Music Player** Mpd, Ncmpcpp
- **GUI Music Player** Rhythmbox, Clementine
- **Media Player** Mpv, Vlc
- **Policy Kit Frontend** Polkit-gnome
- **Screenshooter** Scrot, Xfce4-screenshooter
- **Wallpaper Handler** Feh, Pywal

## Keybinds & Mousebinds
- **Super + Enter** launch a terminal
- **Super + Shift + Enter** launch alternative terminal
- **Super + Shift + W** launch firefox
- **Super + Shift + F** launch thunar
- **Super + D** launch rofi
- **Ctrl + Space** launch synapse 
- **Super + Arrows** change focus
- **Super + Shift + Arrows** move focused window
- **Super + 1-9** switch to workspace 1-9
- **Super + Shift + 1-9** move focused container to workspace 1-9
- **Super + Q** kill focused window
- **Super + F** fullscreen toggle
- **Super + S** layout toggle split
- **Super + Z** layout stacking
- **Super + W** layout tabbed
- **Super + H** split in horizontal orientation
- **Super + V** split in vertical orientation
- **Super + Space** floating toggle
- **Super + Shift + Space** focus mode_toggle
- **Super + Shift + BackSpace** reload the configuration file
- **Super + Shift + r** restart i3
- **Super + Shift + c** reload i3 configuration
- ..More keybinds just read the *~/.config/i3/config* file

## Notes
- If you want to use this configuration, inspect the code before use.
- Install git
- Clone this repo `git clone --depth=1 https://github.com/berthosefin/Dotfiles ~/.Dotfiles`
- Deploy the dotfiles `cp -rv ~/.Dotfiles/* ~`
- Change the default CLI Shell `chsh $(whoami) -s /bin/zsh`
- If you find "birkhoff" in the configuration file, replace it with your own username.
- Edit some system configuration, example in ~/.Dotfiles/.system
- Reboot
- Fix some errors
- Start working
