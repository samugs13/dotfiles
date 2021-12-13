"Plugins
call plug#begin('~/.config/nvim/plugged')

"autocompletion
Plug 'chun-yang/auto-pairs', "Pairs autocompletion.
Plug 'hrsh7th/nvim-cmp',
Plug 'hrsh7th/cmp-nvim-lsp',
Plug 'hrsh7th/cmp-buffer',
Plug 'hrsh7th/cmp-path',
Plug 'hrsh7th/cmp-cmdline',

"style
Plug 'itchyny/lightline.vim', "Status bar.
Plug 'ap/vim-css-color', "Hex colors.
Plug 'ryanoasis/vim-devicons', "Icons for NERDTree.
Plug 'kyazdani42/nvim-web-devicons', "Icons for barbar
Plug 'tiagofumo/vim-nerdtree-syntax-highlight', "Syntax highlighting for NERDTree
Plug 'joshdick/onedark.vim', "Theme
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'} "Highlighting.
Plug 'onsails/lspkind-nvim', "Lsp icons

"git
Plug 'airblade/vim-gitgutter', "Shows a git diff in the sign column.
Plug 'Xuyuanp/nerdtree-git-plugin', "Shows git diffs in NERDTree.
Plug 'tpope/vim-fugitive', "A complement to command line git.

"tools
Plug 'tpope/vim-surround', "Mappings to easily delete, change and add such surroundings in pairs.
Plug 'tpope/vim-commentary', "Comment stuff out.
Plug 'preservim/nerdtree', "Tree explorer for vim.
Plug 'ptzz/lf.vim', "File manager.
Plug 'voldikss/vim-floaterm', "Floating window for lf.
Plug 'neovim/nvim-lspconfig', "Configurations for Neovim's built-in language server client.
Plug 'nvim-lua/plenary.nvim', "Lua functions.
Plug 'nvim-telescope/telescope.nvim', "Fuzzy finder.
Plug 'github/copilot.vim',
Plug 'romgrk/barbar.nvim',

"snippets
Plug 'hrsh7th/cmp-vsnip', "Snippet
Plug 'hrsh7th/vim-vsnip', "snippets
call plug#end()

