"                                 ___     
"        ___        ___          /__/\    
"       /__/\      /  /\        |  |::\   
"       \  \:\    /  /:/        |  |:|:\  
"        \  \:\  /__/::\      __|__|:|\:\ 
"    ___  \__\:\ \__\/\:\__  /__/::::| \:\
"   /__/\ |  |:|    \  \:\/\ \  \:\~~\__\/
"   \  \:\|  |:|     \__\::/  \  \:\      
"    \  \:\__|:|     /__/:/    \  \:\     
"     \__\::::/      \__\/      \  \:\    
"         ~~~~                   \__\/    

" Set compatibility to Vim only.
set nocompatible

" Turn on syntax highlighting and plugins.
syntax on
filetype on
filetype plugin indent on

" Encoding
set encoding=utf-8

" Show line numbers
set relativenumber
highlight LineNr ctermfg=white

" Always show current position
set ruler

" Highlight matching search patterns
set hlsearch

" Enable incremental search
set incsearch

" Ignore case when searching
set ignorecase

" When searching try to be smart about cases 
set smartcase

" Uncomment below to set the max textwidth. Use a value corresponding to the width of your screen.
" set textwidth=80
set formatoptions=tcqrn1
set tabstop=4
set shiftwidth=4
set softtabstop=4
set expandtab
set noshiftround

" Search down into subfolders
" Provides tab-completion for all file-related tasks
set path+=**

" Display all matching files when we tab complete
set wildmenu

" Turn off modelines
set modelines=0

" Don't redraw while executing macros (good performance config)
set lazyredraw

" For regular expressions turn magic on
set magic

" Display 5 lines above/below the cursor when scrolling with a mouse.
set scrolloff=5

" Fixes common backspace problems
set backspace=indent,eol,start

" Display options
set showmode
set showcmd
set cmdheight=1

" Highlight matching pairs of brackets. Use the '%' character to jump between them.
set matchpairs+=<:>

" Set status line display
set laststatus=2
hi StatusLine ctermfg=black ctermbg=gray cterm=NONE
hi StatusLineNC ctermfg=black ctermbg=gray cterm=NONE
hi User1 ctermfg=black ctermbg=white
hi User2 ctermfg=NONE ctermbg=NONE
hi User3 ctermfg=black ctermbg=gray
hi User4 ctermfg=black ctermbg=white
set statusline=\                    " Padding
set statusline+=%f                  " Path to the file
set statusline+=\ %1*\              " Padding & switch colour
set statusline+=%y                  " File type
set statusline+=\ %2*\              " Padding & switch colour
set statusline+=%=                  " Switch to right-side
set statusline+=\ %3*\              " Padding & switch colour
set statusline+=line                " of Text
set statusline+=\                   " Padding
set statusline+=%l                  " Current line
set statusline+=\ %4*\              " Padding & switch colour
set statusline+=of                  " of Text
set statusline+=\                   " Padding
set statusline+=%L                  " Total line
set statusline+=\                   " Padding

" Tweaks for browser
let g:newtrw_banner=0           " disable annoying banner
let g:newtrw_browser_split=4    " open in prior window
let g:newtrw_altv=1             " open splits to the right
let g:newtrw_liststyle=3        " tree view
let g:newtrw_list_hide=netrw_gitignore#Hide()
let g:netrw_list_hide=',\(^\|\s\s)\zs\.\S\+'

" Store info from no more than 100 files at a time, 9999 lines of text
" 100kb of data. Useful for copying large amounts of data between files.
set viminfo='100,<9999,s100
