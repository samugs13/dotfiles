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
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'} "Highlighting.
Plug 'neovim/nvim-lspconfig', "Configurations for Neovim's built-in language server client.
Plug 'hrsh7th/nvim-compe', "Auto completion
Plug 'nvim-lua/plenary.nvim', "Lua functions.
Plug 'nvim-telescope/telescope.nvim', "Fuzzy finder.
call plug#end()

let mapleader =","

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

"NERDTree
map <leader>t :NERDTreeToggle<CR>
"Start NERDTree when Vim starts with a directory argument.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists('s:std_in') |
    \ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif

"Vim-compe remaps
inoremap <silent><expr> <C-Space> compe#complete()
inoremap <silent><expr> <CR>      compe#confirm('<CR>')
inoremap <silent><expr> <C-e>     compe#close('<C-e>')
inoremap <silent><expr> <C-f>     compe#scroll({ 'delta': +4 })
inoremap <silent><expr> <C-d>     compe#scroll({ 'delta': -4 })

"Find files using Telescope command-line sugar.
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

"Language server setup
lua << EOF
require'lspconfig'.pyright.setup{}
require'lspconfig'.bashls.setup{}
require'lspconfig'.cmake.setup{}
require'lspconfig'.java_language_server.setup{}
require'lspconfig'.html.setup{}
EOF
