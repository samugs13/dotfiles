from qtile_extras.widget.decorations import RectDecoration, BorderDecoration 
from .colors import onedark

rect = {
    "decorations": [
        RectDecoration(colour=onedark[7], radius=5, filled=True, padding_y=6)
    ],
    "padding": 8,
}

redb = {
    "decorations": [
        BorderDecoration(colour=onedark[1], border_width=2, padding_y=0, padding_x=0, padding=15)
    ],
}

greenb = {
    "decorations": [
        BorderDecoration(colour=onedark[2], border_width=2, padding_y=0, padding_x=0, padding=15)
    ],
}

purpleb = {
    "decorations": [
        BorderDecoration(colour=onedark[5], border_width=2, padding_y=0, padding_x=0, padding=15)
    ],
}

yellowb = {
    "decorations": [
        BorderDecoration(colour=onedark[3], border_width=2, padding_y=0, padding_x=0, padding=15)
    ],
}

cyanb = {
    "decorations": [
        BorderDecoration(colour=onedark[6], border_width=2, padding_y=0, padding_x=0, padding=15)
    ],
}
