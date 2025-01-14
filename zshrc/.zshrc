# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# Path to your oh-my-zsh installation
export ZSH="$HOME/.oh-my-zsh"

# Set the ZSH theme
ZSH_THEME="powerlevel10k/powerlevel10k" # set by `omz`

# Plugins to load
plugins=(
    git
    zsh-autosuggestions
    macos
    zsh-syntax-highlighting
    zsh-vi-mode
    colored-man-pages
)

# Source oh-my-zsh
source "$ZSH/oh-my-zsh.sh"

# OH MY ZSH CUSTOMIZATION using hoembrw
source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
source $HOMEBREW_PREFIX/share/zsh-autopair/autopair.zsh

# Initialize rbenv (if you use it)
if command -v rbenv >/dev/null 2>&1; then
    eval "$(rbenv init -)"
fi

# Initialize pyenv (if you use it)
if command -v pyenv >/dev/null 2>&1; then
    eval "$(pyenv init -)"
fi

# For crontab -e to work
export VISUAL=nvim


# SDKMAN initialization (must be at the end of the file)
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$SDKMAN_DIR/bin/sdkman-init.sh" ]] && source "$SDKMAN_DIR/bin/sdkman-init.sh"

# Function to add directories to PATH if not already included
path_add() {
    for dir in "$@"; do
        if [ -d "$dir" ] && [[ ":$PATH:" != *":$dir:"* ]]; then
            PATH="${dir}:$PATH"
        fi
    done
}

# Add directories to PATH
path_add \
    "/opt/homebrew/opt/llvm/bin" \
    "$HOME/Library/pnpm" \
    "/Applications/Visual Studio Code.app/Contents/Resources/app/bin" \
    "$HOME/.cargo/bin" \
    "$HOME/Library/Application\ Support/JetBrains/Toolbox/scripts"

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
