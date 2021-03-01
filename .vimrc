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

" General
set relativenumber		    " Show line numbers
set linebreak			    " Break lines at word (requires Wrap lines)
set showbreak=+++		    " Wrap-broken line prefix
set textwidth=1000		    " Line wrap (number of cols)
set showmatch			    " Highlight matching brace
set visualbell			    " Use visual bell (no beeping)
 
set hlsearch			    " Highlight all search results
set smartcase			    " Enable smart-case search
set ignorecase			    " Always case-insensitive
set incsearch			    " Searches for strings incrementally
 
set autoindent			    " Auto-indent new lines
set shiftwidth=4		    " Number of auto-indent spaces
set smartindent			    " Enable smart-indent
set smarttab			    " Enable smart-tabs
set softtabstop=4		    " Number of spaces per Tab
 
" Advanced
set ruler			    " Show row and column ruler information
 
set undolevels=1000		    " Number of undo levels
set backspace=indent,eol,start	    " Backspace behaviour

syntax on			    " Turn on syntax highlighting
filetype plugin indent on		    " and plugins
set nocompatible		    " Set compatibility to Vim only
set encoding=utf-8		    " Encoding
set wildmenu			    " Display all matching files when we tab complete
set path+=**			    " Search down into subfolders and provide tab-completion for all file-related tasks

" Set status line display
set laststatus=2
set statusline=\                    " Padding
set statusline+=%f                  " Path to the file
set statusline+=\ %2*\              " Padding & switch colour
set statusline+=%y                  " File type
set statusline+=\ %1*\              " Padding & switch colour
set statusline+=%=                  " Switch to right-side
set statusline+=\ %3*\              " Padding & switch colour
set statusline+=line                " of Text
set statusline+=\                   " Padding
set statusline+=%l                  " Current line
set statusline+=\ %2*\              " Padding & switch colour
set statusline+=of                  " of Text
set statusline+=\                   " Padding
set statusline+=%L                  " Total line
set statusline+=\                   " Padding

" Colors
colorscheme wal

hi StatusLine ctermfg=white ctermbg=gray cterm=NONE
hi StatusLineNC ctermfg=white ctermbg=gray cterm=NONE
hi User1 ctermfg=NONE ctermbg=NONE
hi User2 ctermfg=black ctermbg=white
hi User3 ctermfg=white ctermbg=gray
