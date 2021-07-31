# Enable colors and change prompt:
autoload -U colors && colors # Load colors

PROMPT="%B%{$fg[magenta]%}%~%b "

PROMPT+="%{$fg_bold[blue]%}%(! %{$fg_bold[red]%} )❯%{$fg_bold[cyan]%}%(1j %{$fg_bold[green]%} )❯%{$fg_bold[yellow]%}%(?  %{$fg_bold[yellow]%})❯%{$reset_color%} "

# Define history
HISTSIZE=10000000
SAVEHIST=10000000
HISTFILE=~/.cache/zsh/history
#HIST_STAMPS="dd/mm/yyyy"
setopt appendhistory

# Auto/tab
autoload -Uz compinit
zstyle ':completion:*' menu select
compinit
_comp_options+=(globdots)               # Include hidden files.

# Use lf to switch directories and bind it to ctrl-f
lfcd () {
     tmp="$(mktemp)"
     lf -last-dir-path="$tmp" "$@"
     if [ -f "$tmp" ]; then
         dir="$(cat "$tmp")"
         rm -f "$tmp"
        [ -d "$dir" ] && [ "$dir" != "$(pwd)" ] && cd "$dir"
      fi
 }
bindkey -s '^f' 'lfcd\n'

# my aliases 
 alias az="cp $HOME/.zshrc $HOME/Escritorio/dotfiles/zsh/"
 alias aa="cp $HOME/.config/alacritty/alacritty.yml $HOME/Escritorio/dotfiles/alacritty/"
 alias aq="cp $HOME/.config/qtile/config.py $HOME/Escritorio/dotfiles/qtile/ && cp -r $HOME/.config/qtile/wallpapers $HOME/Escritorio/dotfiles/qtile/ && cp $HOME/.config/qtile/autostart.sh $HOME/Escritorio/dotfiles/qtile/"

# Load plugins
source /home/s4mb4/.config/zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source /home/s4mb4/.config/zsh/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

######DEFAULT#########

# Path to oh-my-zsh installation.
export ZSH=/usr/share/oh-my-zsh/

#ZSH_THEME="random"

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

source $ZSH/oh-my-zsh.sh

setopt GLOB_DOTS

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export HISTCONTROL=ignoreboth:erasedups

# Make nvim the default editor
export EDITOR='nvim'
export VISUAL='nvim'

#PS1='[\u@\h \W]\$ '

if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

#list
alias ls='ls --color=auto'
alias la='ls -a'
alias ll='ls -la'
alias l='ls'
alias l.="ls -A | egrep '^\.'"

#fix obvious typo's
alias cd..='cd ..'
alias pdw="pwd"
alias udpate='sudo pacman -Syyu'
alias upate='sudo pacman -Syyu'
alias updte='sudo pacman -Syyu'
alias updqte='sudo pacman -Syyu'
alias upqll="paru -Syu --noconfirm"
alias upal="paru -Syu --noconfirm"

## Colorize the grep command output for ease of use (good for log files)##
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'

#pacman unlock
alias unlock="sudo rm /var/lib/pacman/db.lck"
alias rmpacmanlock="sudo rm /var/lib/pacman/db.lck"

#arcolinux logout unlock
alias rmlogoutlock="sudo rm /tmp/arcologout.lock"

#free
alias free="free -mt"

#use all cores
alias uac="sh ~/.bin/main/000*"

#continue download
alias wget="wget -c"

#userlist
alias userlist="cut -d: -f1 /etc/passwd"

#merge new settings
alias merge="xrdb -merge ~/.Xresources"

# Aliases for software managment
# pacman or pm
alias pacman='sudo pacman --color auto'
alias update='sudo pacman -Syyu'

# yay as aur helper - updates everything
alias pksyua="paru -Syu --noconfirm"
alias upall="paru -Syu --noconfirm"

#ps
alias psa="ps auxf"
alias psgrep="ps aux | grep -v grep | grep -i -e VSZ -e"

#grub update
alias update-grub="sudo grub-mkconfig -o /boot/grub/grub.cfg"

#add new fonts
alias update-fc='sudo fc-cache -fv'

#switch between bash and zsh
alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"
alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"

#switch between lightdm and sddm
alias tolightdm="sudo pacman -S lightdm lightdm-gtk-greeter lightdm-gtk-greeter-settings --noconfirm --needed ; sudo systemctl enable lightdm.service -f ; echo 'Lightm is active - reboot now'"
alias tosddm="sudo pacman -S sddm --noconfirm --needed ; sudo systemctl enable sddm.service -f ; echo 'Sddm is active - reboot now'"

#quickly kill conkies
alias kc='killall conky'

#hardware info --short
alias hw="hwinfo --short"

#mounting the folder Public for exchange between host and guest on virtualbox
alias vbm="sudo /usr/local/bin/arcolinux-vbox-share"

#iso and version used to install ArcoLinux
alias iso="cat /etc/dev-rel | awk -F '=' '/ISO/ {print $2}'"

#nvim for important configuration files
alias vlightdm="sudo $EDITOR /etc/lightdm/lightdm.conf"
alias vpacman="sudo $EDITOR /etc/pacman.conf"
alias vgrub="sudo $EDITOR /etc/default/grub"
alias vconfgrub="sudo $EDITOR /boot/grub/grub.cfg"
alias vmkinitcpio="sudo $EDITOR /etc/mkinitcpio.conf"
alias vmirrorlist="sudo $EDITOR /etc/pacman.d/mirrorlist"
alias vsddm="sudo $EDITOR /etc/sddm.conf"
alias vfstab="sudo $EDITOR /etc/fstab"
alias vnsswitch="sudo $EDITOR /etc/nsswitch.conf"
alias vsamba="sudo $EDITOR /etc/samba/smb.conf"
alias vb="$EDITOR ~/.bashrc"
alias vz="$EDITOR ~/.zshrc"
alias vq="$EDITOR ~/.config/qtile/config.py"
alias va="$EDITOR ~/.config/alacritty/alacritty.yml"

#systeminfo
alias probe="sudo -E hw-probe -all -upload"

#shutdown or reboot
alias ssn="sudo shutdown now"
alias sr="sudo reboot"

#give the list of all installed desktops - xsessions desktops
alias xd="ls /usr/share/xsessions"

# # ex = EXtractor for all kinds of archives
# # usage: ex <file>
ex ()
{
  if [ -f $1 ] ; then
    case $1 in
      *.tar.bz2)   tar xjf $1   ;;
      *.tar.gz)    tar xzf $1   ;;
      *.bz2)       bunzip2 $1   ;;
      *.rar)       unrar x $1   ;;
      *.gz)        gunzip $1    ;;
      *.tar)       tar xf $1    ;;
      *.tbz2)      tar xjf $1   ;;
      *.tgz)       tar xzf $1   ;;
      *.zip)       unzip $1     ;;
      *.Z)         uncompress $1;;
      *.7z)        7z x $1      ;;
      *.deb)       ar x $1      ;;
      *.tar.xz)    tar xf $1    ;;
      *.tar.zst)   tar xf $1    ;;
      *)           echo "'$1' cannot be extracted via ex()" ;;
    esac
  else
    echo "'$1' is not a valid file"
  fi
}

#create a file called .zshrc-personal and put all your personal aliases
#in there. They will not be overwritten by skel.

[[ -f ~/.zshrc-personal ]] && . ~/.zshrc-personal

# reporting tools - install when not installed
# install neofetch
#neofetch
# install screenfetch
#screenfetch
# install ufetch-git
ufetch
# install ufetch-arco-git
#ufetch-arco
# install arcolinux-paleofetch-git
#paleofetch
# install alsi
#alsi
# install arcolinux-bin-git - standard on ArcoLinux isos (or sfetch - smaller)
#hfetch
# install lolcat
#sfetch | lolcat
