# iterm-components
Custom status bar components for use with iTerm2


## Components

### GitHub stars

Shows the current number of stars for the specified repository. You can add a personal access token in order to minimize rate limiting or to keep tabs on a private repository.

### `kubectl` context

Shows the active `kubectl` context.

### `pyenv` (work in progress)

Shows the active Python version or virtual environment.

### `rvm` gemset (work in progress)

Shows the active gemset.


## Installation

At the moment, I don't know a better way to do this.
If you know one, I would happily review a pull request!

### Auto-loading the components

iTerm2 expects the custom status bar components that act as long-running processes to be in its `AutoLaunch` folder:

```shell
$ git clone git@github.com:daneah/iterm-components.git
$ cd ${HOME}/Library/Application\ Support/iTerm2/Scripts
$ mkdir -p AutoLaunch && cd AutoLaunch
$ ln -s /path/to/iterm-components/some_component.py .  # For each component you want to install; cp them if preferred
```

### Configuring the components

After the components you want are present in the `AutoLaunch` folder, iTerm2 should make them available to use.

Read [the instructions for using status bar components](https://www.iterm2.com/3.3/documentation-status-bar.html) and drag them where you like.
