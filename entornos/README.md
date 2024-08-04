# A Simple boiler plate project using Poetry, Tox, Ruff & Coverage
==================================================================


The code inside my_project & tests is auto generated from ChatGPT, and uses NumPy & Requests.
The purpose of that is to show how those dependencies are handled by Poetry, these can be removed!
Remove them with:
`poetry remove numpy`

`poetry remove requests`

To use this as your own base repository, you'll need to do the following.

1. Remove the code in main.py
2. Remove the tests in test_main.py
3. Make a new virtual environment & activate it
4. Install Poetry and tox into your new virtual environment.
5. Update the text in pyproject.toml to correct the name, description & email-etc.
6. As i've called this 'my_project', if you use a new name you'll need to reflect this in the folder name, tox file and pyproject.toml file

Then to use tox to run your tests, linting & building you can do the following:
`tox -e py311`

`tox -e lint`

`tox -e build`

Or simply run: `tox` to run all 3.


Linting rules
=============
The linting rules are held inside the ruff.toml file check the ruff docs for the full usage.


Adding new dependencies
=======================
To add new dependencies you can do:
`poetry add <package>`





