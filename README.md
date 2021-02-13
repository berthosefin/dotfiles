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
- **Web Browser** Firefox, Google-Chrome
- **Task Manager** Htop
- **Power Manager** Tlp
- **Image Viewer** Ristretto, Feh
- **Sound Mixer** PulseAudio
- **Terminal** Termite, Xfce4-terminal, Gnome-terminal
- **CLI Shell** Zsh
- **Archiver** Xarchiver, File-roller
- **Notification Daemon** Dunst
- **Graphic Editor** Gimp
- **CLI File Manager** Ranger
- **CLI Text Editor** Vim
- **GUI Text Editor** Mousepad
- **CLI Music Player** Ncmpcpp
- **GUI Music Player** Rhythmbox
- **Media Player** Mpv, Vlc
- **Policy Kit Frontend** Polkit-gnome
- **Screenshooter** Scrot, Xfce4-screenshooter
- **Wallpaper Handler** Feh, Pywal

## Keybinds & Mousebinds
- **Super + Enter** launch termite
- **Super + Shift + Enter** launcha xfce4-terminal
- **Super + Shift + w** launch firefox
- **Super + Shift + f** launch thunar
- **Super + d** launch rofi
- **Ctrl + Space** launch synapse 
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
- Clone this repo `git clone --depth=1 https://github.com/berthosefin/Dotfiles ~/.dotfiles`
- Deploy the dotfiles `cp -rv ~/.dotfiles/* ~`
- Change the default CLI Shell `chsh $(whoami) -s /bin/zsh`
- If you find "birkhoff" in the configuration file, replace it with your own username.
- Edit some system configuration, example in ~/.dotfiles/.system
- Reboot
- Fix some errors
- Start working
