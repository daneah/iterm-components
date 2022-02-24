#!/bin/bash

set -e

iterm_scripts_dir="$HOME/Library/Application Support/iTerm2/Scripts"
autolaunch_dir="$iterm_scripts_dir/AutoLaunch"

mkdir -p "$autolaunch_dir"

echo Linking scripts to AutoLaunch folder $autolaunch_dir

for script in $(ls *.py); do
    echo Linking $script...
    chmod +x $script
    cp $script "$autolaunch_dir/$script"
done
