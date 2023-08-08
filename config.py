from libqtile import bar, layout, widget, hook
import libqtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
import os

mod = "mod1"
terminal = "kitty"
browser = "brave"
home = os.path.expanduser('~/.config/qtile/')

# BAR SETTINGS
BAR_OPACITY = 1.0
BAR_SIZE    = 22
BAR_MARGIN  = 4

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
        lazy.layout.grow(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", 
        lazy.layout.shrink(), 
        desc="Grow window to the right"),

    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
   
    # My keybinds 🗿🗿🗿🗿
    Key([mod],"Return",             lazy.spawn(terminal),           desc="Launch terminal"),
    Key([mod, "shift"], "Return",   lazy.spawn("rofi -show drun"),  desc="Application Launcher"),
    Key([mod, "shift"], "c",        lazy.spawn("rofi -show calc"),  desc="Launch calculator"),
    Key([mod],          "e",        lazy.spawn("rofimoji"),         desc="Launch emojis"),
    Key([mod],          "s",        lazy.spawn("signal-desktop"),   desc="Launch signal"),
    Key([mod]         , "b",        lazy.spawn(browser),            desc="Launch browser"),
    Key([mod, "shift"], "e",        lazy.spawn("thunderbird"),      desc="Launch thunderbird"),
    Key([mod]         , "f",        lazy.spawn("pcmanfm"),          desc="Launch filemanager"),
    Key([mod]         , "q",        lazy.window.kill(),             desc="Kill focused window"),
    Key([mod, "shift"], "f",        lazy.window.toggle_floating(),  desc="float focused window"),
    Key([mod, "shift"], "r",        lazy.reload_config(),           desc="Reload the config"),
    Key([mod, "shift"], "x",        lazy.shutdown(),                desc="Shutdown Qtile"),
    Key([mod, "shift"], "Tab",      lazy.next_layout()),
    Key([mod],          "Tab",      lazy.spawn("rofi -show")),

    Key([mod, "mod1"], "k",          lazy.to_screen(0)),
    Key([mod, "mod1"], "j",          lazy.to_screen(1)),

    # Media keys
    Key([ ], 'XF86AudioMicMute',    lazy.spawn('pactl set-source-mute @DEFAULT_SOURCE@ toggle')),
    Key([ ], 'XF86AudioMute',       lazy.spawn(f'{home}volume.sh mute')),
    Key([ ], 'XF86AudioLowerVolume',lazy.spawn(f'{home}volume.sh down')),
    Key([ ], 'XF86AudioRaiseVolume',lazy.spawn(f'{home}volume.sh up')),
    Key([ ], 'XF86AudioPlay',       lazy.spawn('playerctl play-pause')),
    Key([ ], 'XF86AudioPrev',       lazy.spawn('playerctl previous')),
    Key([ ], 'XF86AudioNext',       lazy.spawn('playerctl next')),
    Key([ ], 'XF86MonBrightnessUp', lazy.spawn('brightnessctl set +5%')),
    Key([],  'XF86MonBrightnessDown',lazy.spawn('brightnessctl set 5%-')),

    # Screenshot
    Key([ ], 'Print',               lazy.spawn('ksnip')),

    # German "umlaute": ä, ö, ü, ß and key layout switching
    Key([mod, "shift"], "Space",    lazy.spawn(f'{home}german_umlaute.sh')),
    Key([mod, "mod1"], "k",        lazy.spawn(f'{home}changelayout.sh')),
]

group_names = '1 2 3 4 5 6 7 8 9'.split()
# group_names = '        '.split()
groups = [Group(name, layout='monadtall') for name in group_names]
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))
    ]

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
          ["#a89984", "#a89984"],
          ["#bbbbbb", "#bbbbbb"],
          ["#ffffff", "#ffffff"]]

layout_theme = {"border_width": 2,
                "margin": 15,
                "border_focus": colors[8],
                "border_normal": colors[0]
                }
layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(),
    layout.Floating(**layout_theme),
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
    font = "JetBrains Mono",
    fontsize = 14,
    margin_y = 3,
    foreground=colors[11],
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            font = "JetBrains Mono",
            fontsize = 14,
            disable_drag = True,
            hide_unused = True,
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
            # this_screen_border = colors [4],
            # other_current_screen_border = colors[6],
            # other_screen_border = colors[4],
            foreground = colors[11],
            background = colors[0]
        ),
        
        widget.TextBox(
            text = '|',
            **widget_defaults
        ), 

        widget.WindowName(
            padding = 0,
            margin_x = 0,
            padding_y = 0,
            padding_x = 6,
            borderwidth = 3,
            **widget_defaults
        ),

        widget.TextBox(
            text = '|',
            **widget_defaults
        ), 

        widget.PulseVolume(
            volume_app = "pamixer",
            update_interval = 0.001,
            emoji = True,
            fmt = "{}",
            **widget_defaults
        ),

        widget.PulseVolume(
            volume_app = "pamixer",
            update_interval = 0.001,
            fmt = "{} ",
            **widget_defaults
        ),

        widget.TextBox(
            text = '|',
            **widget_defaults
        ), 

        widget.CPU(
            fmt = "💻 {}",
            format = "{load_percent}%",
            update_interval = 3.0,
            mouse_callbacks = {'Button1': lazy.spawn(f"{terminal} btop"),},
            **widget_defaults
        ),

        widget.TextBox(
            text = '|',
            **widget_defaults
        ), 

        widget.ThermalZone(
            fgcolor_normal = colors[11],
            fgcolor_high = colors[5],
            fgcolor_crit = colors[3],
            update_interval = 3.0,
            zone = '/sys/class/thermal/thermal_zone1/temp',
            fmt = "🔥 {}",
            mouse_callbacks = {'Button1': lazy.spawn(f"{terminal} btop"),},
            **widget_defaults
        ),

        widget.TextBox(
            text = '|',
            **widget_defaults
        ), 
        
        widget.Memory(
            fmt = "🧠 {}",
            measure_mem='G',
            format = "{MemUsed: .2f}{mm}",
            update_interval = 3.0,
            mouse_callbacks = {'Button1': lazy.spawn(f"{terminal} btop"),},
            **widget_defaults
        ),

        widget.TextBox(
            text = '|',
            **widget_defaults
        ), 

        widget.Clock(
            format="📆 %d.%m.%Y(%a) | 🕒 %H:%M:%S",
            **widget_defaults
        ),

        widget.Systray(
            **widget_defaults
        ),
    ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    widgets_screen2_len = len(widgets_screen2)
    del widgets_screen2[widgets_screen2_len-1:widgets_screen2_len]              # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=BAR_OPACITY, size=BAR_SIZE, margin=BAR_MARGIN)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=BAR_OPACITY, size=BAR_SIZE, margin=BAR_MARGIN))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

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
focus_on_window_activation = "focus"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

# Autostarts
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])
