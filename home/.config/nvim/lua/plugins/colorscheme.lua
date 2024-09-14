return {
  { "shaunsingh/nord.nvim", name = "nord" },
  { "dracula/vim", name = "dracula" },
  { "morhetz/gruvbox", name = "gruvbox" },
  {
    "catppuccin/nvim",
    name = "catppuccin",
    config = function()
      require("catppuccin").setup({
        flavour = "frappe", -- latte, frappe, macchiato, mocha
      })
      vim.cmd.colorscheme("catppuccin")
    end,
  },

  -- Configure LazyVim to load colorscheme
  {
    "LazyVim/LazyVim",
    opts = {
      colorscheme = "nord",
    },
  },
}
