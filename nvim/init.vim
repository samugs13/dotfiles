"Plugins
call plug#begin('~/.config/nvim/plugged')
Plug 'chun-yang/auto-pairs', "Pairs autocompletion.
Plug 'itchyny/lightline.vim', "Status bar.
Plug 'ap/vim-css-color', "Hex colors.
Plug 'tpope/vim-surround', "Mappings to easily delete, change and add such surroundings in pairs.
Plug 'tpope/vim-commentary', "Comment stuff out.
Plug 'tpope/vim-fugitive', "A complement to command line git.
Plug 'airblade/vim-gitgutter', "Shows a git diff in the sign column.
Plug 'preservim/nerdtree', "Tree explorer for vim.
Plug 'Xuyuanp/nerdtree-git-plugin', "Shows git diffs in NERDTree.
Plug 'ryanoasis/vim-devicons', "Icons for NERDTree.
Plug 'tiagofumo/vim-nerdtree-syntax-highlight', "Syntax highlighting for NERDTree
Plug 'ptzz/lf.vim', "File manager.
Plug 'voldikss/vim-floaterm', "Floating window for lf.
Plug 'JamshedVesuna/vim-markdown-preview', "Allow previewing markdown files in a browser.
Plug 'Yggdroot/indentLine', "Vertical lines at each indentation level for code indented.
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }, "Asynchronous completion framework for neovim.
Plug 'sheerun/vim-polyglot', "A collection of language packs for Vim.
call plug#end()

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

"Key maps
map <leader>t :NERDTreeToggle<CR>

"NERD TREE
"Start NERDTree when Vim starts with a directory argument.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists('s:std_in') |
    \ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif

"Exclude indention on certain files and buffers
let g:indentLine_fileTypeExclude = ['text', 'sh', 'help', 'terminal']
let g:indentLine_bufNameExclude = ['NERD_tree.*', 'term:.*']

"Enable deoplete at startup
let g:deoplete#enable_at_startup = 1



