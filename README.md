# dotfiles
## General Information :gear:
- OS: Endeavour OS (previously ArcoLinux)
- Font: Hack Nerd Font
- Session Manager: LightDM
- WM: Awesome (previously Qtile)
- Terminal emulator: Alacritty
- Shell: ZSH
- Launcher/Scripts: Dmenu
- Browser: Brave

## LightDM :closed_lock_with_key:
- Greeter: lightdm-mini-greeter

## Window Managers :window:
### AwesomeWM
- Notifications: Naughty
- Color theme: Nord

![awesome2](https://github.com/samugs13/dotfiles/assets/78796980/0b2de37f-55b3-4e5f-98a0-7328af15dfab)
![awesome1](https://github.com/samugs13/dotfiles/assets/78796980/64e94a53-6a85-45d8-98f4-3f8c67063924)

### Qtile - Environment 1

- Widgets: [decorwidgets.py](qtile/settings/decorwidgets.py)
- Notifications: Dunst
- Color theme: OneDark

![env2](https://user-images.githubusercontent.com/78796980/160302432-31409682-b74b-4c40-9772-473ae5bd00a7.png)
![env2-2](https://user-images.githubusercontent.com/78796980/160302441-a291dcc6-8d43-43f9-970a-b7ec6b899e71.png)

When an extra monitor is used, GroupBox widget is splitted (5 groups in one screen, 5 in the other) and some extra widgets are added in the second screen:

![monitor](https://user-images.githubusercontent.com/78796980/160303845-bb93488e-e04b-42b7-9424-89d84898176f.png)

### Qtile - Environment 2

- Widgets: [widgets.py](qtile/widgets/widgets.py)

- Notifications: Dunst

This environment uses pywal to match wallpaper colors with qtile and terminal colors. All the wallpapers are available in `qtile/settings/wallpapers` and they were obtained from different sources, I am   not the author. To enable this feature:
  1. Add the line `wal -R` to autostart.sh to restore the last colorscheme and wallpaper that was in use
  2. Import the script [pywal_colors.py](qtile/settings/scripts/pywal_colors.py) to use wallpaper colors in qtile widgets

![rice2](https://user-images.githubusercontent.com/78796980/160302779-88043e49-3ce6-46e8-85aa-057dc32d6b72.png)
![rice1](https://user-images.githubusercontent.com/78796980/160302783-5a5e3f1b-e3fc-4f02-9d0c-a0ed7aa8bf87.png)
![rice3](https://user-images.githubusercontent.com/78796980/160302784-eee5199d-117c-4cbe-a36c-ceb715e459c3.png)
![rice4](https://user-images.githubusercontent.com/78796980/160302788-df1eecd6-9118-478d-9db7-e4b3a8e87602.png)

## ZSH :desktop_computer:
![zsh](https://user-images.githubusercontent.com/78796980/160304165-92d263b5-4ec0-45ce-ae2c-777be76e6e75.png)

### Prompt
It work as follows:
- Working directory path (it is shortened if it is at least 4 elements long)
- First arrow: is this a root shell? (true=red, false=blue)
- Second arrow: are there any running background jobs? (true=red, false=cyan)
- Third arrow: did the last command fail to execute? (true=red, false=green)
- Git status indicator

It also has vi mode and a functionality that allows switching directories using LF (lfcd), both developed by @LukeSmithxyz.

## Launcher/Scripts :rocket:

### Preview:
https://user-images.githubusercontent.com/78796980/160442924-8bc14796-691b-4fd0-bd15-2ecee7c2a3fb.mp4

### Scripts
<ul>
  <li>powersettings -> lock & suspend, logout, shutdown or reboot the system  </li>
  <li>togglescreenlayout -> available layouts: show desktop only on pc, show desktop only on HDMI output, duplicate or extend screen.</li>
  <li>audiosettings -> change audio source output between HDMI and analog </li>
</ul>

