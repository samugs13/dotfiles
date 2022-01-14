#######################################################################################################
#                                         GROUPS                                                      #
#######################################################################################################

import fontawesome as fa
from libqtile.config import Group, Key
from libqtile.lazy import lazy 
from .keys import keys, mod

__groups = {
        1: Group(name=fa.icons['terminal'], layout='bsp'),
        2: Group(name=fa.icons['globe'], layout='monadtall'),
        3: Group(name=fa.icons['folder-open'], layout='monadwide'),
        4: Group(name=fa.icons['code'], layout='monadtall'),
        5: Group(name=fa.icons['video'], layout='max'),
        6: Group(name=fa.icons['edit'], layout='max'),
        7: Group(name=fa.icons['music'], layout='max'),
        8: Group(name=fa.icons['comment-dots'], layout='max'),
        9: Group(name=fa.icons['skull-crossbones'], layout='monadwide'),
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name),
        #    desc="move focused window to group {}".format(i.name)),
    ])
