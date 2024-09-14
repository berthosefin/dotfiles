# Dotfiles

My personal backup of my dotfiles.

## Some screenshots

![preview](https://raw.githubusercontent.com/berthosefin/dotfiles/main/previews/Oc8yPyKWNR.gif)

## Details

- **WM** i3-wm
- **Launcher** rofi
- **Panel** polybar
- **Compositor** picom
- **GTK Fonts** 0xProto, Iosevka Custom, etc.
- **File Manager** thunar
- **Web Browser** firefox
- **Task Manager** htop
- **Power Manager** tlp
- **Image Viewer** viewnior, feh
- **Terminal** alacritty, xfce4-terminal
- **CLI Shell** zsh
- **Notification Daemon** dunst
- **Text Editor** vim, neovim
- **Music Player** rhythmbox, mixxx
- **Media Player** mpv, vlc
- **Wallpaper Handler** feh, pywal

## Keybinds & Mousebinds

- **Super + Enter** launch alacritty
- **Super + Shift + Enter** launch xfce4-terminal
- **Super + Shift + w** launch firefox
- **Super + Shift + f** launch thunar
- **Super + d** launch rofi
- **Ctrl + Print** xfce4-screenshooter
- **Print** scrot
- **Super + h,j,k,l** change focus
- **Super + Arrows** change focus
- **Super + Shift + h,j,k,l** move focused window
- **Super + Shift + Arrows** move focused window
- **Super + 1-9** switch to workspace 1-9
- **Super + Shift + 1-9** move focused container to workspace 1-9
- **Super + q** kill focused window
- **Super + f** fullscreen toggle
- **Super + s** layout toggle split
- **Super + z** layout stacking
- **Super + w** layout tabbed
- **Alt + b** split in horizontal orientation
- **Alt + v** split in vertical orientation
- **Super + Space** floating toggle
- **Super + Shift + Space** focus mode_toggle
- **Super + r** mode resize
- **Super + e** launch powermenu
- **Super + Shift + r** restart i3
- **Super + Shift + c** reload i3 configuration
- **Ctrl + Alt + p** switch polybar style
- **Ctrl + Alt + c** switch colorscheme
- ...More keybinds just read the _~/.config/i3/config_ file

## Notes

- If you want to use this configuration, inspect the code before use.
- Make a backup of your current configuration.
- Install dependencies :
  - git
  - stow
  - i3-wm
  - i3lock-color
  - feh
  - polybar
  - rofi
  - alacritty
  - dunst
  - picom-git
  - brightnessctl
  - xidlehook
  - scrot
  - papirus-icon-theme
- Clone this repo :

```sh
git clone --depth=1 https://github.com/berthosefin/dotfiles ~/dotfiles
```

- Deploy the dotfiles :

```sh
cd ~/dotfiles && stow home -t ~
```

- If you find `thos` in the configuration file, replace it with your own username.
- Reboot.
- Fix some errors.
- Start working.
