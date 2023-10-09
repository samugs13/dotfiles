---------------------------
-- s4mb4 awesome theme --
---------------------------

local theme_assets = require("beautiful.theme_assets")
local xresources = require("beautiful.xresources")
local dpi = xresources.apply_dpi

local gfs = require("gears.filesystem")
local themes_path = gfs.get_themes_dir()

local theme = {}

theme.font          = "Hack Nerd Font 12"
theme.taglist_font  = "Font Awesome 6 Free Solid 12"
theme.wallpaper     = "/home/s4mb4/.config/awesome/themes/mynord/wallpapers/wpp1.png"
theme.tasklist_disable_icon = false

theme.bg_normal     = "#282c34"
theme.bg_focus      = "#535d6c"
theme.bg_urgent     = "#bf616a"
theme.bg_minimize   = "#444444"
theme.bg_systray    = theme.bg_normal

theme.fg_normal     = "#e5e9f0"
theme.fg_focus      = "#e5e9f0"
theme.fg_urgent     = "#e5e9f0"
theme.fg_minimize   = "#e5e9f0"

theme.useless_gap   = dpi(2)
theme.border_width  = dpi(2)
theme.border_normal = "#282c34"
theme.border_focus  = "#b48ead"
theme.border_marked = "#91231c"

theme.red = "#bf616a"
theme.green = "#a3be8c"
theme.yellow = "#ebcb8b"
theme.blue = "#81a1c1"
theme.magenta = "#b48ead"
theme.cyan = "#88c0d0"

-- There are other variable sets
-- overriding the default one when
-- defined, the sets are:
-- taglist_[bg|fg]_[focus|urgent|occupied|empty|volatile]
-- tasklist_[bg|fg]_[focus|urgent]
-- titlebar_[bg|fg]_[normal|focus]
-- tooltip_[font|opacity|fg_color|bg_color|border_width|border_color]
-- mouse_finder_[color|timeout|animate_timeout|radius|factor]
-- prompt_[fg|bg|fg_cursor|bg_cursor|font]
-- hotkeys_[bg|fg|border_width|border_color|shape|opacity|modifiers_fg|label_bg|label_fg|group_margin|font|description_font]
-- Example:
-- theme.taglist_bg_focus = "#ff0000"

-- Generate taglist squares:
local taglist_square_size = dpi(4)
theme.taglist_squares_sel = theme_assets.taglist_squares_sel(
    taglist_square_size, theme.fg_normal
)
theme.taglist_squares_unsel = theme_assets.taglist_squares_unsel(
    taglist_square_size, theme.fg_normal
)

-- Variables set for theming notifications:
local naughty = require("naughty")
local gears = require("gears")
naughty.config.defaults.icon_size = dpi(100)
naughty.config.defaults.ontop = true
naughty.config.defaults.timeout = 10
naughty.config.defaults.hover_timeout = 300
naughty.config.defaults.title = 'Notification'
naughty.config.defaults.margin = dpi(14)
naughty.config.defaults.border_width = 2
naughty.config.defaults.border_color = "#a3be8c"
naughty.config.defaults.opacity = 0.9
naughty.config.defaults.position = 'top_middle'
naughty.config.defaults.spacing = dpi(30)
naughty.config.defaults.shape = function(cr, w, h)
    gears.shape.rounded_rect(cr, w, h, dpi(6))
end
theme.notification_font = "Hack Nerd Font 10"
theme.notification_bg = "#535d60"
theme.notification_fg = "#e5e9f0"

-- Variables set for theming the menu:
theme.menu_height = dpi(25)
theme.menu_width  = dpi(175)
theme.menu_bg_normal = "#282c34"
theme.menu_bg_focus =   "#535d6c"
theme.menu_border_width = 2
theme.menu_border_color = "#a3be8c"

-- You can add as many variables as
-- you wish and access them by using
-- beautiful.variable in your rc.lua
--theme.bg_widget = "#cc0000"

-- theme.wallpaper = themes_path.."default/background.png"

-- You can use your own layout icons like this:
theme.layout_fairh = themes_path.."default/layouts/fairhw.png"
theme.layout_fairv = themes_path.."default/layouts/fairvw.png"
theme.layout_floating  = themes_path.."default/layouts/floatingw.png"
theme.layout_magnifier = themes_path.."default/layouts/magnifierw.png"
theme.layout_max = themes_path.."default/layouts/maxw.png"
theme.layout_fullscreen = themes_path.."default/layouts/fullscreenw.png"
theme.layout_tilebottom = themes_path.."default/layouts/tilebottomw.png"
theme.layout_tileleft   = themes_path.."default/layouts/tileleftw.png"
theme.layout_tile = themes_path.."default/layouts/tilew.png"
theme.layout_tiletop = themes_path.."default/layouts/tiletopw.png"
theme.layout_spiral  = themes_path.."default/layouts/spiralw.png"
theme.layout_dwindle = themes_path.."default/layouts/dwindlew.png"
theme.layout_cornernw = themes_path.."default/layouts/cornernww.png"
theme.layout_cornerne = themes_path.."default/layouts/cornernew.png"
theme.layout_cornersw = themes_path.."default/layouts/cornersww.png"
theme.layout_cornerse = themes_path.."default/layouts/cornersew.png"

-- Generate Awesome icon:
theme.awesome_icon = theme_assets.awesome_icon(
    theme.menu_height, theme.bg_focus, theme.fg_focus
)

-- Define the icon theme for application icons. If not set then the icons
-- from /usr/share/icons and /usr/share/icons/hicolor will be used.
theme.icon_theme = nil

return theme

-- vim: filetype=lua:expandtab:shiftwidth=4:tabstop=8:softtabstop=4:textwidth=80
