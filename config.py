from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os

mod = "mod4"
terminal = "kitty"
browser = "firefox"

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", 
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", 
        lazy.layout.grow(), 
        lazy.layout.increase_nmaster(),
        desc="Grow window to the right"),

    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
   
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # My keybinds 🗿🗿🗿🗿
    Key([mod],"Return",             lazy.spawn(terminal),           desc="Launch terminal"),
    Key([mod, "shift"], "Return",   lazy.spawn("rofi -show drun"),  desc="Application Launcher"),
    Key([mod, "shift"], "c",        lazy.spawn("rofi -show calc"),  desc="Launch calculator"),
    Key([mod, "shift"], "e",        lazy.spawn("emoji-picker"),     desc="Launch emojis"),
    Key([mod, "shift"], "s",        lazy.spawn("signal-desktop"),   desc="Launch signal"),
    Key([mod]         , "b",        lazy.spawn(browser),            desc="Launch firefox"),
    Key([mod]         , "e",        lazy.spawn("thunderbird"),      desc="Launch thunderbird"),
    Key([mod]         , "f",        lazy.spawn("pcmanfm"),          desc="Launch thunderbird"),
    Key([mod]         , "q",        lazy.window.kill(),             desc="Kill focused window"),
    Key([mod, "shift"], "f",        lazy.window.toggle_floating(),  desc="float focused window"),
    Key([mod, "shift"], "r",        lazy.reload_config(),           desc="Reload the config"),
    Key([mod, "shift"], "x",        lazy.shutdown(),                desc="Shutdown Qtile"),
    
    # Media keys
    Key([ ], 'XF86AudioMicMute',    lazy.spawn('pactl set-source-mute @DEFAULT_SOURCE@ toggle')),
    Key([ ], 'XF86AudioMute',       lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
    Key([ ], 'XF86AudioLowerVolume',lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ -1000')),
    Key([ ], 'XF86AudioRaiseVolume',lazy.spawn('pactl set-sink-volume @DEFAULT_SINK@ +1000')),
    Key([ ], 'XF86AudioPlay',       lazy.spawn('playerctl play-pause')),
    Key([ ], 'XF86AudioPrev',       lazy.spawn('playerctl previous')),
    Key([ ], 'XF86AudioNext',       lazy.spawn('playerctl next')),
    Key([ ], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%')),
    Key([],  'XF86MonBrightnessDown',lazy.spawn('brightnessctl set 5%-')),

    # Caps lock indicator
    Key([ ], 'Caps_Lock',           lazy.spawn('notify-send "🤓🤓🤓🤓" "<u><b>CAPS</b></u>" -u critical')),

    # Screenshot
    Key([ ], 'Print',               lazy.spawn('ksnip')),

]

group_names = '        '.split()
groups = [Group(name, layout='monadtall') for name in group_names]
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))]

colors = [["#282828", "#282828"],
          ["#1d2021", "#1d2021"],
          ["#ebdbb2", "#ebdbb2"],
          ["#fb4934", "#fb4934"],
          ["#b8bb26", "#b8bb26"],
          ["#fe8019", "#fe8019"],
          ["#458588", "#458588"],
          ["#b16286", "#b16286"],
          ["#83a598", "#83a598"],
          ["#d3869b", "#d3869b"],
          ["#a89984", "#a89984"]]

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors[6],
                "border_normal": colors[0]
                }
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(),
    layout.Floating(**layout_theme)
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=14,
    margin_y = 4,
    background=colors[1]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [

        widget.GroupBox(
            font = "JetBrains Mono",
            fontsize = 25,
            disable_drag = True,
            margin_y = 3,
            margin_x = 0,
            padding_y = 0,
            padding_x = 6,
            borderwidth = 3,
            active = colors[2],
            inactive = colors[10],
            rounded = False,
            highlight_color = colors[1],
            highlight_method = "block",
            this_current_screen_border = colors[8],
            this_screen_border = colors [4],
            other_current_screen_border = colors[6],
            other_screen_border = colors[4],
            foreground = colors[2],
            background = colors[0]
        ),
        
        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.TextBox(
            text = '|',
            background = colors[0],
            foreground = colors[2],
            padding = 2,
            fontsize = 14
        ), 
        
        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.WindowName(
            foreground = colors[2],
            background = colors[0],
            padding = 0,
            fontsize = 14,
            margin_y = 4,
            margin_x = 0,
            padding_y = 0,
            padding_x = 6,
            borderwidth = 3,
        ),
        
        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.CurrentLayoutIcon(
            custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
            foreground = colors[2],
            background = colors[0],
            padding = 0,
            scale = 0.7
        ),
        
        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.TextBox(
            text = '|',
            background = colors[0],
            foreground = colors[2],
            padding = 2,
            fontsize = 14
        ),
         
        widget.PulseVolume(
            background = colors[0],
            foreground = colors[2],
            volume_app = "pamixer",
            update_interval = 0.01,
            fmt = "🔊 {}",
        ),

        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.TextBox(
            text = '|',
            background = colors[0],
            foreground = colors[2],
            padding = 2,
            fontsize = 14
        ),


        widget.CPU(
            background = colors[0],
            foreground = colors[2],
            fmt = "💻 {}",
            format = "{load_percent}%"
        ),

        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.TextBox(
            text = '|',
            background = colors[0],
            foreground = colors[2],
            padding = 2,
            fontsize = 14
        ),

        widget.ThermalZone(
            background = colors[0],
            fgcolor_normal = colors[2],
            fgcolor_high = colors[5],
            fgcolor_crit = colors[3],
            update_interval = 1,
            zone = '/sys/class/thermal/thermal_zone1/temp',
            fmt = "🔥 {}"
        ),

        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.TextBox(
            text = '|',
            background = colors[0],
            foreground = colors[2],
            padding = 2,
            fontsize = 14
        ),

        
        widget.Memory(
            background = colors[0],
            foreground = colors[2],
            fmt = "🧠 {}",
            measure_mem='G',
            format = "{MemUsed: .1f}{mm}"
        ),

        widget.Sep(
            linewidth = 5, padding = 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.TextBox(
            text = '|',
            background = colors[0],
            foreground = colors[2],
            padding = 2,
            fontsize = 14
        ),

        widget.Sep(
            linewidth = 5, paddi= 0,
            foreground = colors[0], background = colors[0]
        ),

        widget.Clock(
            format="📆 %Y-%m-%d %a | 🕒 %H:%M:%S %p",
            foreground = colors[2],
            background = colors[0],
        ),

        widget.Systray(
            background = colors[0],
        ),
    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    del widgets_screen2[23:24]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=23, margin=5)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=23, margin=5))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Autostarts
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


