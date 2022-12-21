# Usage
- Run `pyenv local 3.8.8` to setup the local python version in your repo
- Run `pipenv install --python 3.8.8` to init the Pipfile and its lock file
- Run `pipenv shell` to activate the virtual env
- Run `pipenv install <package name>` to install the dependency needed, add --dev for development need (testing) only
- Run `exit` to deactivate the virtual env

# pyenv
`pyenv install --list` to see the available Python versions you can install

`pyenv versions` to see the installed Python versions

`pyenv global <Python version>` to set an installed Python version as global

`pyenv local <Python version>` to set an installed Python version file .python-version for a given project folder

`pyenv uninstall <Python version>` to uninstall an already installed Python version

# pipenv
`pipenv install` to create a virtual environment

`pipenv install --python <Python version>` to create a virtual environment indicating the desired Python version (that you have installed using Pyenv)

`pipenv --rm` to delete the current virtual environment

`pipenv shell` to activate the created virtual environment

`exit` to deactivate an already activated virtual environment

Now let’s take a look at the summary of the commands after the virtual environment has been activated:

`pipenv install <package name>` to install the latest version of the package under the [packages] section. Adding --dev to the previous commands, Pipenv will do the same but under the [dev-packages] section

`pipenv install <package name>==<package version>` to install a specified version of a package, under the [packages] section

`pipenv update <package name>` to update a version of a package(upgrade or downgrade) to the one that you have previously specified in the Pipfile

`pipenv uninstall <package name>` to uninstall a package