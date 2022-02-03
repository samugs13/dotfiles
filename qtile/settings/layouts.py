################################
#            LAYOUTS           #
################################

from libqtile import layout 
from .colors import colors, onedark 
from libqtile.config import Match

layout_theme = {
    "border_width":3,
    "border_focus": onedark[5],
    "border_normal": onedark[0],
    "single_border_width": 0,
    "margin":8,
}

layouts = [
    layout.MonadTall(**layout_theme),

    layout.MonadWide(**layout_theme),

    layout.Max(),
]

floating_layout = layout.Floating(float_rules=[     
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='confirm'),
    Match(title='dialog'),
    Match(title='download'),
    Match(title='error'),
    Match(title='file_progress'),
    Match(title='notification'),
    Match(title='splash'),
    Match(title='toolbar'),
    Match(title='arandr'),
    Match(title='feh'),
    Match(title='Open File'),
    Match(title='Qalculate!'),
], **layout_theme)
