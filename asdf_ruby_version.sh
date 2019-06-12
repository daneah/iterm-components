function iterm2_print_user_vars() {
    iterm2_set_user_var asdfRubyVersion $(asdf current ruby | sed 's/ .*$//')
}
