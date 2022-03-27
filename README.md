# dotfiles
<ul>
  <li>Window Manager -> qtile</li>
  <li>Shell -> zsh</li>
  <li>Terminal -> alacritty</li>
  <li>IDE -> neovim</li>
  <li>Notifications -> dunst</li>
  <li>Launcher -> dmenu</li>
  <li>File Manager -> lf</li>
</ul>

## Qtile - Environment 1
![env2](https://user-images.githubusercontent.com/78796980/160302432-31409682-b74b-4c40-9772-473ae5bd00a7.png)
![env2-2](https://user-images.githubusercontent.com/78796980/160302441-a291dcc6-8d43-43f9-970a-b7ec6b899e71.png)

This environment uses `decorwidgets.py`. When an extra monitor is used, GroupBox is splitted (5 groups in one screen, 5 in the other) and some extra widgets are added in the second screen:

![monitor](https://user-images.githubusercontent.com/78796980/160303845-bb93488e-e04b-42b7-9424-89d84898176f.png)

## Qtile - Environment 2
![rice2](https://user-images.githubusercontent.com/78796980/160302779-88043e49-3ce6-46e8-85aa-057dc32d6b72.png)
![rice1](https://user-images.githubusercontent.com/78796980/160302783-5a5e3f1b-e3fc-4f02-9d0c-a0ed7aa8bf87.png)
![rice3](https://user-images.githubusercontent.com/78796980/160302784-eee5199d-117c-4cbe-a36c-ceb715e459c3.png)
![rice4](https://user-images.githubusercontent.com/78796980/160302788-df1eecd6-9118-478d-9db7-e4b3a8e87602.png)

This environment uses pywal to match wallpaper colors with qtile and terminal colors. All the wallpapers are available in `qtile/settings/wallpapers`. To enable this feature:

    - Add the line `wall -R` to autostart.sh to restore the last colorscheme and wallpaper that was in use
    
    - Import the script [pywal_colors.py](qtile/settings/scripts/pywal_colors.py) to use wallpaper colors in qtile widgets

The widgets are the ones at `widgets.py`

## Neovim 
![nvim](https://user-images.githubusercontent.com/78796980/160302889-f3b0da4f-85fe-469a-85be-ab73e14f7091.png)

This config is setup as an IDE for multiple languajes.

## Alacritty - ZSH
![zsh](https://user-images.githubusercontent.com/78796980/160304165-92d263b5-4ec0-45ce-ae2c-777be76e6e75.png)

### ZSH
Prompt work as follows:
- Working directory path (it is shortened if it is at least 4 elements long)
- First arrow: is this a root shell? (true=red, false=blue)
- Second arrow: are there any running background jobs? (true=cyan, false=green)
- Third arrow: did the last command fail to execute? (true=red, false=yellow)
- Git status indicator

It also has vi mode and a functionality that allows switching directories using LF (lfcd).
 
### Alacritty
<ul>
  <li>Colorscheme: OneDark</li>
  <li>Font: Hack Nerd Font</li>
</ul>
