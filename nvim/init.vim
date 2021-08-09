let mapleader =","

set number
set termguicolors
set hidden

"Set colorscheme
syntax enable
set background=dark
colorscheme material-theme

"Set lightline theme
let g:lightline = { 'colorscheme': 'material', }

"Enable autocompletion:
set wildmode=longest,list,full

"Plugins
call plug#begin('~/.config/nvim/plugged')
Plug 'chun-yang/auto-pairs',
Plug 'itchyny/lightline.vim',
Plug 'ap/vim-css-color',
Plug 'tpope/vim-surround',
Plug 'tpope/vim-commentary',
Plug 'airblade/vim-gitgutter',
Plug 'preservim/nerdtree',
Plug 'Xuyuanp/nerdtree-git-plugin',
Plug 'ryanoasis/vim-devicons',
Plug 'tiagofumo/vim-nerdtree-syntax-highlight',
Plug 'ptzz/lf.vim',
Plug 'voldikss/vim-floaterm'
call plug#end()

"Key maps
map <leader>t :NERDTreeToggle<CR>

"NERD TREE
"Show clean status in nerdtree-git-plugin
let g:NERDTreeGitStatusShowClean = 1

"Start NERDTree when Vim starts with a directory argument.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists('s:std_in') |
    \ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif




