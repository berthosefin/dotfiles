## Qtile Configuration
## by Birkhoff
## -------------------------------------------------------------------------

import os
import re
import socket
import subprocess
import json

from typing import List  # noqa: F401

from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile import qtile, bar, layout, widget, hook
from libqtile.command import lazy
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
alt = "mod1"
home = os.path.expanduser("~")
terminal = guess_terminal()
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

## Colors-------------------------------------------------------------------

colorsFile = home + '/.cache/wal/colors.json'

with open(colorsFile, 'r') as f:
    colors = json.load(f)

color0 = colors['colors']['color0']
color1 = colors['colors']['color1']
color2 = colors['colors']['color2']
color3 = colors['colors']['color3']
color4 = colors['colors']['color4']
color5 = colors['colors']['color5']
color6 = colors['colors']['color6']
color7 = colors['colors']['color7']
color8 = colors['colors']['color8']
color9 = colors['colors']['color9']
color10 = colors['colors']['color10']
color11 = colors['colors']['color11']
color12 = colors['colors']['color12']
color13 = colors['colors']['color13']
color14 = colors['colors']['color14']
color15 = colors['colors']['color15']

## Commands------------------------------------------------------------------

class command:
    terminal        = 'termite'
    explorer        = 'thunar'
    browser         = 'firefox'
    windowmenu      = 'rofi -show window'
    runmenu         = 'rofi -show run'
    programmenu     = 'rofi -show drun -show-icons'

    def script(scriptname):
        return os.path.join(home, '.bin/'+ scriptname)

## Keymaps-------------------------------------------------------------------

keys = [
    # Switch between windows
    Key([mod], "h",                 lazy.layout.left(),                             desc="Move focus to left"),
    Key([mod], "l",                 lazy.layout.right(),                            desc="Move focus to right"),
    Key([mod], "j",                 lazy.layout.down(),                             desc="Move focus down"),
    Key([mod], "k",                 lazy.layout.up(),                               desc="Move focus up"),
    
    Key([mod], "Left",              lazy.layout.left(),                             desc="Move focus to left"),
    Key([mod], "Right",             lazy.layout.right(),                            desc="Move focus to right"),
    Key([mod], "Down",              lazy.layout.down(),                             desc="Move focus down"),
    Key([mod], "Up",                lazy.layout.up(),                               desc="Move focus up"),
    
    Key([mod, "shift"], "space",    lazy.layout.next(),                             desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h",        lazy.layout.shuffle_left(),                     desc="Move window to the left"),
    Key([mod, "shift"], "l",        lazy.layout.shuffle_right(),                    desc="Move window to the right"),
    Key([mod, "shift"], "j",        lazy.layout.shuffle_down(),                     desc="Move window down"),
    Key([mod, "shift"], "k",        lazy.layout.shuffle_up(),                       desc="Move window up"),

    Key([mod, "shift"], "Left",     lazy.layout.shuffle_left(),                     desc="Move window to the left"),
    Key([mod, "shift"], "Right",    lazy.layout.shuffle_right(),                    desc="Move window to the right"),
    Key([mod, "shift"], "Down",     lazy.layout.shuffle_down(),                     desc="Move window down"),
    Key([mod, "shift"], "Right",    lazy.layout.shuffle_up(),                       desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h",      lazy.layout.grow_left(),                        desc="Grow window to the left"),
    Key([mod, "control"], "l",      lazy.layout.grow_right(),                       desc="Grow window to the right"),
    Key([mod, "control"], "j",      lazy.layout.grow_down(),                        desc="Grow window down"),
    Key([mod, "control"], "k",      lazy.layout.grow_up(),                          desc="Grow window up"),

    Key([mod, "control"], "Left",   lazy.layout.grow_left(),                        desc="Grow window to the left"),
    Key([mod, "control"], "Right",  lazy.layout.grow_right(),                       desc="Grow window to the right"),
    Key([mod, "control"], "Down",   lazy.layout.grow_down(),                        desc="Grow window down"),
    Key([mod, "control"], "Up",     lazy.layout.grow_up(),                          desc="Grow window up"),

    Key([mod], "n",                 lazy.layout.normalize(),                        desc="Reset all window sizes"),
    Key([mod], "f",                 lazy.window.toggle_fullscreen(),                desc='toggle fullscreen'),
    Key([mod], "space",             lazy.window.toggle_floating(),                  desc='toggle floating'),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod], "s",                 lazy.layout.toggle_split(),                     desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",               lazy.next_layout(),                             desc="Toggle between layouts"),

    Key([mod], "r",                 lazy.spawncmd(),                                desc="Spawn a command using a prompt widget"),
    Key([mod], "q",                 lazy.window.kill(),                             desc="Kill focused window"),
    Key([mod, "shift"], "r",        lazy.restart(),                                 desc="Restart Qtile"),
    Key([mod, "shift"], "e",        lazy.shutdown(),                                desc="Shutdown Qtile"),

    # Command Keymaps
    Key([mod], "d",                 lazy.spawn(command.programmenu),                desc="App launcher"),
    Key([mod], "Return",            lazy.spawn(command.terminal),                   desc="Launch a terminal"),
    Key([mod, "shift"], "f",        lazy.spawn(command.explorer),                   desc="Launch a file manager"),
    Key([mod, "shift"], "w",        lazy.spawn(command.browser),                    desc="Launch a web browser"),
    Key([alt], "Tab",               lazy.spawn(command.windowmenu),                 desc="Switch Open Windows"),

    # Basic Keymaps
    Key([],"XF86AudioMute",         lazy.spawn(command.script("togglemute")),       desc="Toggle Mute"),
    Key([],"XF86AudioLowerVolume",  lazy.spawn(command.script("volumedown")),       desc="Volume Down"),
    Key([],"XF86AudioRaiseVolume",  lazy.spawn(command.script("volumeup")),         desc="Volume Up"),
    Key([],"XF86MonBrightnessDown", lazy.spawn(command.script("brightnessdown")),   desc="Brightness Down"),
    Key([],"XF86MonBrightnessUp",   lazy.spawn(command.script("brightnessup")),     desc="Brightness Up"),

    # Others Keymaps
    Key([alt], "f",                 lazy.spawn("fsearch"),                          desc="Search file"),
    Key([alt], "g",                 lazy.spawn("galculator"),                       desc="Start a calculator"),
    Key([alt], "l",                 lazy.spawn(command.script("blurlock")),         desc="Lock screen"),
    Key([mod], "e",                 lazy.spawn(command.script("powermenu")),        desc="Power menu"),

    Key([], "Print",                lazy.spawn("scrot"),                            desc="Print Screen"),
    Key(["control"], "Print",       lazy.spawn("xfce4-screenshooter"),              desc="Print Screen"),
]

## Groups--------------------------------------------------------------------------------

groups = [Group(i) for i in "aztyuiop"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

## Layouts-------------------------------------------------------------------------------------------------------

layout_theme = {
    "border_width": 1,
    "margin": 5,
    "border_focus": color2,
    "border_normal": color1,
    "font": "Iosevka",
    "grow_amount": 5,
}

layouts = [
    # layout.Columns(),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_theme, fair=False),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    layout.Floating(**layout_theme, fullscreen_border_width=1, max_border_width=1),
]


## Widgets-------------------------------------------------------------------------------------------------------------------------------

widget_defaults = dict(
    font='Iosevka',
    fontsize=8,
    padding=2,
    background=color0,
)
extension_defaults = widget_defaults.copy()

def icon(icon_text, fg, bg):
    return widget.TextBox(font=fonts[1],text=icon_text,foreground=fg,background=bg)

def powerline(fg, bg):
    return widget.TextBox(fontsize=24,padding=-1,text='',foreground=fg,background=bg)

group_box_settings = {
    "padding": 2,
    "borderwidth": 1,
    "active": color0,
    "inactive": color0,
    "disable_drag": True,
    "rounded": True,
    "highlight_color": color0,
    "block_highlight_text_color": color7,
    "highlight_method": "block",
    "this_current_screen_border": color5,
    "this_screen_border": color0,
    "other_current_screen_border": color0,
    "other_screen_border": color0,
    "foreground": color0,
    "background": color5,
    "urgent_border": color6,
}

# Mouse Callbacks Functions
def runscript(script):
    return lambda:qtile.cmd_spawn(script)

screens = [
    Screen(
        #wallpaper="~/Images/Nord/underwater.png",
        #wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.TextBox(text="", font="Font Awesome 5 Free Solid", fontsize=12, padding=10,
                    foreground=color2, background=color0,
                    mouse_callbacks={"Button1": runscript(command.programmenu)},
                ),
                widget.Sep(linewidth=0, padding=10, foreground=color2),
                powerline(color1, color0),
                widget.CurrentLayout(foreground=color0, background=color1,),
                powerline(color0, color1),
                powerline(color5, color0),
                widget.GroupBox(**group_box_settings,),
                powerline(color0, color5),
                widget.Prompt(prompt = prompt, font = "Font Awesome 5 Free Solid", padding = 10, foreground = color2, background = color0),
                widget.Spacer(),
                widget.TextBox(text=" ", font="Font Awesome 5 Free Solid",
                    foreground=color2, background=color0,
                ),
                widget.WindowName(empty_group_string="Desktop", max_chars=150, width=bar.CALCULATED,
                    foreground=color2, background=color0,
                    mouse_callbacks={"Button2": runscript('xdotool getwindowfocus windowkill')},
                ),
                widget.Spacer(),
                powerline(color4, color0),
                widget.TextBox(text=" ", font="Font Awesome 5 Free Solid",
                    foreground=color0,background=color4,
                ),
                widget.PulseVolume(limit_max_volume="True",
                    foreground=color0, background=color4,
                    mouse_callbacks={"Button3": runscript('pavucontrol')},
                ),
                powerline(color0, color4),
                powerline(color3, color0),
                widget.TextBox(text=" ", font="Font Awesome 5 Free Solid",
                    foreground=color0, background=color3,
                    mouse_callbacks={"Button1": runscript('networkmanager_dmenu')},
                ),
                widget.Net(interface = "wlo1", format = '{essid}',
                    foreground = color0, background = color3,
                    mouse_callbacks={"Button1": runscript('networkmanager_dmenu')},
                ),
                powerline(color0, color3),
                powerline(color2, color0),
                widget.TextBox(text=" ", font="Font Awesome 5 Free Solid",
                    foreground=color0, background=color2,
                ),
                widget.Clock(format="%a %d %b",
                    foreground=color0, background=color2,
                    mouse_callbacks={"Button1": runscript(command.script('calender')) }
                ),
                powerline(color0, color2),
                powerline(color1, color0),
                widget.TextBox(text=" ", font="Font Awesome 5 Free Solid",
                    foreground=color0, background=color1,
                ),
                widget.Clock(format="%H:%M",
                    foreground=color0, background=color1,
                ),
                powerline(color0, color1),
                widget.Systray(),
                #widget.QuickExit(),
                widget.TextBox(text="⏻", font="Font Awesome 5 Free Solid", fontsize=12, padding=10,
                    foreground=color6,
                    mouse_callbacks={"Button1": runscript(command.script('powermenu'))},
                ),
            ],
            24,
            margin=[0, 0, 0, 0],
        ),
        # top=bar.Gap(0),
        # bottom=bar.Gap(0),
        # left=bar.Gap(0),
        # right=bar.Gap(0),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='termite'),
    Match(wm_class='xfce4-terminal'),
    Match(wm_class='Gnome-terminal'),
    Match(wm_class='mpv'),
    Match(wm_class='Ristretto'),
    Match(wm_class='Evince'),
    Match(wm_class='Lxappearance'),
    Match(wm_class='Pavucontrol'),
    Match(wm_class='GParted'),
    Match(wm_class='Fsearch'),
    Match(wm_class='Galculator'),
    Match(wm_class='xdman-Main'),
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
