" Enable syntax highlighting
syntax on

" Set line numbers
set number

" Enable mouse support
set mouse=a

" Enable clipboard support
set clipboard=unnamedplus

" Show matching parentheses
set showmatch

" Set the tab width
set tabstop=4
set shiftwidth=4
set expandtab

" Enable incremental search
set incsearch

" Highlight search results
set hlsearch

" Disable bell sound
set noerrorbells
set visualbell

" Plugin section
call plug#begin('~/.vim/plugged')

" Color scheme plugin
Plug 'dylanaraps/wal.vim'

call plug#end()

" Set the color scheme
colorscheme wal
