# updates asdfRubyVersion user variable.
# if you already have a iterm2_print_user_vars function in your
# .*shrc just add line 6 to that

function iterm2_print_user_vars() {
    iterm2_set_user_var asdfRubyVersion $(asdf current ruby | sed 's/ .*$//')
}
