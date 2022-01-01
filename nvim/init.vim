"Load list of plugins
source /home/s4mb4/.config/nvim/plugins.vim

let mapleader =" "
set termguicolors
set hidden
set number relativenumber

"Set colorscheme
syntax on
colorscheme onedark
set background=dark

"Set lightline theme
let g:lightline = { 'colorscheme': 'one', }

"Enable autocompletion:
set wildmode=longest,list,full

"NERDTree
map <leader>t :NERDTreeToggle<CR>

"Start NERDTree when Vim starts with a directory argument.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists('s:std_in') |
    \ execute 'NERDTree' argv()[0] | wincmd p | enew | execute 'cd '.argv()[0] | endif

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
require'lspconfig'.html.setup{}
require'lspconfig'.cssls.setup{}
require'lspconfig'.java_language_server.setup{}
require'lspconfig'.dockerls.setup{}
require'lspconfig'.terraformls.setup{}
require'lspconfig'.texlab.setup{}
require'lspconfig'.vimls.setup{}
EOF

"CMP setup
lua << EOF
    local cmp = require'cmp'

    cmp.setup({
        snippet = {
        expand = function(args)
            vim.fn["vsnip#anonymous"](args.body)
        end,
        },

        mapping = {
        ['<C-b>'] = cmp.mapping(cmp.mapping.scroll_docs(-4), { 'i', 'c' }),
        ['<C-f>'] = cmp.mapping(cmp.mapping.scroll_docs(4), { 'i', 'c' }),
        ['<C-Space>'] = cmp.mapping(cmp.mapping.complete(), { 'i', 'c' }),
        ['<C-y>'] = cmp.config.disable,
        ['<C-e>'] = cmp.mapping({
            i = cmp.mapping.abort(),
            c = cmp.mapping.close(),
        }),
        ['<CR>'] = cmp.mapping.confirm({ select = true }),
        },

	sources = cmp.config.sources({
		{ name = 'nvim_lsp' },
		{ name = 'vsnip' },
		{ name = 'copilot' },
		{ name = 'buffer' },
	}),

	experimental = {
		ghost_text = true,
	},

	formatting = {
		format = require("lspkind").cmp_format({with_text = true, menu = ({
			buffer = "[buf]",
			nvim_lsp = "[LSP]",
			vsnip = "[snip]",
			path = "[path]",
			copilot = "[co]",
		})}),
	},
    })

    cmp.setup.cmdline('/', {
        sources = {
        { name = 'buffer' }
        }
    })

    -- Use cmdline & path source for ':' (if you enabled `native_menu`, this won't work anymore).
    cmp.setup.cmdline(':', {
        sources = cmp.config.sources({
        { name = 'path' }
        }, {
        { name = 'cmdline' }
        })
    })

    -- Setup lspconfig.
    local capabilities = require('cmp_nvim_lsp').update_capabilities(vim.lsp.protocol.make_client_capabilities())
    require('lspconfig')['pyright'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['bashls'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['cmake'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['html'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['cssls'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['java_language_server'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['dockerls'].setup {
        capabilities = capabilities
    }    
    require('lspconfig')['terraformls'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['texlab'].setup {
        capabilities = capabilities
    }
    require('lspconfig')['vimls'].setup {
        capabilities = capabilities
    }
EOF
