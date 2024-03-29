"Load list of plugins
source /home/s4mb4/.config/nvim/plugins.vim

let mapleader =" "
set termguicolors
set hidden
set number relativenumber
set mouse=a


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
require'lspconfig'.jdtls.setup{}
require'lspconfig'.dockerls.setup{}
require'lspconfig'.texlab.setup{}
require'lspconfig'.terraformls.setup{}
EOF
autocmd BufWritePre *.tf lua vim.lsp.buf.formatting_sync()

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
    require('lspconfig')['jdtls'].setup {
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
EOF

"TreeSitter setup
lua << EOF
require'nvim-treesitter.configs'.setup {
    highlight = { enable = true },
    incremental_selection = { enable = true },
    indent = {
        enable = true,
    },
}
EOF

"Barbar setup
lua << EOF
vim.g.bufferline = {
  animation = true,
  auto_hide = false,
  tabpages = true,
  closable = true,
  clickable = true,
  icons = true,
  icon_custom_colors = false,
  icon_separator_active = '▎',
  icon_separator_inactive = '▎',
  icon_close_tab = '',
  icon_close_tab_modified = '●',
  icon_pinned = '車',
  insert_at_end = false,
  insert_at_start = false,
  maximum_padding = 1,
  maximum_length = 30,
  semantic_letters = true,
  letters = 'asdfjkl;ghnmxcvbziowerutyqpASDFJKLGHNMXCVBZIOWERUTYQP',
  no_name_title = nil,
}
EOF

