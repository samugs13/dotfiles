# Enable colors and change prompt:
autoload -U colors && colors # Load colors

# Autoload info function
autoload -Uz vcs_info

# Enable substitution in the prompt.
setopt prompt_subst

# Automatically cd into typed directory.
setopt autocd 

# Run vcs_info just before a prompt is displayed (precmd)
zstyle ':vcs_info:*' enable git svn
precmd() {
    vcs_info
}

# Format the vcs_info_msg_0_ variable
zstyle ':vcs_info:*' check-for-changes true
zstyle ':vcs_info:*' unstagedstr ' ●' #changes not added 
zstyle ':vcs_info:*' stagedstr ' ✚' #added changes but not commited
zstyle ':vcs_info:git:*' formats       '%F{#61afef}(%F{#e5c07b}%b%F{#e06c75}%u%F{#98c379}%c%F{#61afef})'
zstyle ':vcs_info:git:*' actionformats '(%b|%a%u%c)'

# Add path to the prompt
PROMPT="%{$fg[magenta]%}%(4~|.../%3~|%~) " 
# Checks if the path is at least 4 elements long %(4~|true|false) and, if true, prints some dots with the last 3 elements (.../%3~), otherwise the full path is printed %~

# Add the arrows to the prompt, which works as follows:
# First arrow: is this a root shell? (true=red, false=blue)
# Second arrow: are there any running background jobs? (true=red, false=cyan)
# Third arrow: did the last command fail to execute? (true=red, false=green)
PROMPT+="%{$fg_bold[blue]%}%(! %{$fg_bold[red]%} )❱%{$fg_bold[cyan]%}%(1j %{$fg_bold[red]%} )❱%{$fg_bold[green]%}%(?  %{$fg_bold[red]%})❱%{$reset_color%} "

# Show git info
RPROMPT=\$vcs_info_msg_0_

# Define history
HISTSIZE=10000000
SAVEHIST=10000000
HISTFILE=~/.cache/zsh/history
HIST_STAMPS="dd.mm.yyyy"
setopt appendhistory

# Auto/tab
autoload -U compinit
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion::complete:*' gain-privileges 1
zmodload zsh/complist
compinit
_comp_options+=(globdots)               # Include hidden files.

# vi mode
bindkey -v
export KEYTIMEOUT=1

# Use vim keys in tab complete menu:
bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'j' vi-down-line-or-history
bindkey -v '^?' backward-delete-char

# reverse search
bindkey '^R' history-incremental-search-backward

# Change cursor shape for different vi modes.
function zle-keymap-select {
  if [[ ${KEYMAP} == vicmd ]] ||
     [[ $1 = 'block' ]]; then
    echo -ne '\e[1 q'
  elif [[ ${KEYMAP} == main ]] ||
       [[ ${KEYMAP} == viins ]] ||
       [[ ${KEYMAP} = '' ]] ||
       [[ $1 = 'beam' ]]; then
    echo -ne '\e[5 q'
  fi
}
zle -N zle-keymap-select
zle-line-init() {
    zle -K viins # initiate `vi insert` as keymap (can be removed if `bindkey -V` has been set elsewhere)
    echo -ne "\e[5 q"
}
zle -N zle-line-init
echo -ne '\e[5 q' # Use beam shape cursor on startup.
preexec() { echo -ne '\e[5 q' ;} # Use beam shape cursor for each new prompt.

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

# Dotfiles aliases 
alias aq="cp $HOME/.config/qtile/config.py $HOME/Escritorio/dotfiles/qtile/ && cp -r $HOME/.config/qtile/settings $HOME/Escritorio/dotfiles/qtile/ && cp $HOME/.config/qtile/autostart.sh $HOME/Escritorio/dotfiles/qtile/" 
alias an="cp -r $HOME/.config/nvim $HOME/Escritorio/dotfiles/"

# Docker aliases 
alias ldi="docker images"
alias ldc="docker container ls -a"
alias ldv="docker volume ls"
alias ldf="docker system df"
alias rmva="docker volume ls | awk 'NR>1 {print $2}' | xargs docker volume rm" # Remove all volumes
alias rmi="docker rmi"
alias rmia="ldi | awk 'NR>1 {print $3}'| xargs docker rmi 2>/dev/null" # Remove all images
alias rmc="docker container rm"
alias rmca="ldc | awk 'NR>1 {print $1}' | xargs docker container rm 2>/dev/null" # Remove all containers
alias dc="docker-compose"

# Kitty kittens aliases
alias ki="kitty +kitten icat"
alias kssh="kitty +kitten ssh"

# Terraform settings
alias tf="terraform"
autoload -U +X bashcompinit && bashcompinit
complete -o nospace -C /usr/bin/terraform terraform

# Apply pywal colors to new terminal instances
# (cat ~/.cache/wal/sequences &)

# Load plugins
source $HOME/.config/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source $HOME/.config/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

######DEFAULT#########

# Uncomment the following line if pasting URLs and other text is messed up.
 DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

setopt GLOB_DOTS

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export HISTCONTROL=ignoreboth:erasedups

# Make nvim the default editor
export EDITOR='nvim'
export VISUAL='nvim'

alias vim='nvim'

#PS1='[\u@\h \W]\$ '

if [ -d "$HOME/.bin" ] ;
  then PATH="$HOME/.bin:$PATH"
fi

if [ -d "$HOME/.local/bin" ] ;
  then PATH="$HOME/.local/bin:$PATH"
fi

#list
alias ls='ls --color=auto'
alias ls='lsd'
alias la='ls -a'
alias ll='ls -la'
alias l='ls'
alias lt='ls --tree'
alias l.="ls -A | egrep '^\.'"

#bat as cat
alias cat='bat'

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
alias vn="$EDITOR ~/.config/nvim/init.vim"

#systeminfo
alias probe="sudo -E hw-probe -all -upload"

#shutdown or reboot
alias ssn="sudo shutdown now"
alias sr="sudo reboot"

#give the list of all installed desktops - xsessions desktops
alias xd="ls /usr/share/xsessions"

#other
alias dia="setsid -f dia --integrated" 
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

#figlet s4mb4

# reporting tools
#neofetch
#ufetch
