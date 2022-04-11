README
======

This template is for any beginner/intermediate level python coder. It does not pretend to be perfect.
Some cool tools are missing (auto-versionning, ...) but it is, I think, a solid start for one who
wants to start a fresh python repo using basic tools for proper code **and** proper documentation.

Please feel free to give any comment or feedback.


Development tools
-----------------

In order to create a new well-designed python repo, here are some basic tools that you could
use.

poetry
^^^^^^

``poetry`` is a nice python management packages. Of course there are 
`other alternatives <https://ahmed-nafies.medium.com/pip-pipenv-poetry-or-conda-7d2398adbac9>`_
like ``conda``, ``pipenv``,... It is mandatory to work in a virtual environment with ``python``,
so you don't have version package issues between your multiple ``python`` projects.

First, install ``poetry`` following the `poetry official doc <https://python-poetry.org/docs/>`_.
Then, create a poetry repo:

.. code-block:: bash

    poetry new <my-python-repo>

Create a virtual env in the same folder (especially for *Visual Studio Code* users) and activate it:

.. code-block::

    python -m venv .venv
    source .venv/bin/Activate # Linux
    .\.venv\Scripts\activate # Windows


Add the python ``.gitignore`` file. Copy paste the one ine the current repo or find one 
on ``github``. Install some basics:

.. code-block::

    poetry add pylint pre-commit black isort commitizen
    poetry add sphinx sphinx-rtd-theme sphinx_copybutton numpydoc

Let see what they are.


pre-commit
^^^^^^^^^^

``pre-commit`` allows you to execute a set of actions before commiting your code.
You could check your code format, check that your notebooks are clean,...

As it is told in the `pre-commit official doc <https://pre-commit.com/>`_:

    *Git hook scripts are useful for identifying simple issues before submission 
    to code review. We run our hooks on every commit to automatically point out 
    issues in code such as missing semicolons, trailing whitespace, and debug statements. 
    By pointing these issues out before code review, this allows a code reviewer to focus on 
    the architecture of a change while not wasting time with trivial style nitpicks.*


Copy past the ``.pre-commit-config.yaml`` file and install the pre-commit by running:

.. code-block::

    pre-commit install

Or create your own following the `pre-commit official doc <https://pre-commit.com/>`_


black
^^^^^

``black`` is a code formatter. As it is told in
`black official doc <https://github.com/psf/black>`_:

    *Black is the uncompromising Python code formatter. By using it, you agree to
    cede control over minutiae of hand-formatting. In return, Black gives you speed,
    determinism, and freedom from pycodestyle nagging about formatting. You will save 
    time and mental energy for more important matters.*

pylint
^^^^^^

``pylint`` is a code checker. As it is told in 
`pylint official doc <https://pylint.pycqa.org/en/latest/>`_: 

    *Pylint is a tool that checks for errors in Python code, tries to enforce a coding
    standard and looks for code smells. It can also look for certain type errors, it
    can recommend suggestions about how particular blocks can be refactored and can offer
    you details about the code's complexity.*

The ``pylint`` settings are loaded from the ``.pylintrc`` file. You can see many options there.
Feel free to change some of them to fit your code guidelines. For example, I have made somes 
changes:

*ignore-patterns*
    now it ignores the files ending with ``_no_pylint.py``

*variable-rgx*
    I have updated the accepted variable names as in data science, ``X`` is a common name


isort
^^^^^
As it is told in the `isort official doc <https://pycqa.github.io/isort/>`_, *isort your 
imports, so you don't have to*.

    *isort is a Python utility / library to sort imports alphabetically, and automatically 
    separated into sections and by type. It provides a command line utility, Python library
    and plugins for various editors to quickly sort all your imports. It requires Python 3.6+
    to run but supports formatting Python 2 code too.*


commitizen
^^^^^^^^^^
As it is told in the `commitizen official doc <https://commitizen-tools.github.io/commitizen/>`_:

    *Commitizen is a tool designed for teams.
    Its main purpose is to define a standard way of committing rules and communicating it.
    The reasoning behind it is that it is easier to read, and enforces writing descriptive commits.
    Besides that, having a convention on your commits makes it possible to parse them and use 
    them for something else, like generating automatically the version or a changelog.*

You can customize it by modifying the ``.cz.toml`` file, especially the ``schema`` and 
``schema_pattern`` entries. For more details, see their documentation.

Documentation tools
-------------------

I won't get into too much details here, but still some that I find useful. A common tool to build
and create doc in python is ``sphinx``. We will set up everything so we have to write the less
into the doc, the more into the code.

sphinx
^^^^^^

Sphinx is a tool that makes it easy to create intelligent and beautiful documentation.
See more details on the `sphinx official doc <https://www.sphinx-doc.org/en/master/>`_.

To create the basic sphinx files, execute in your root directory:

.. code-block::

    mkdir docs
    cd docs
    sphinx-quickstart

To build your documentation, just make it:

.. code-block::

    cd docs
    make html # Linux
    make.bat html  # Windows

All the configurations are set up in the ``conf.py`` file. Copy/paste the one from this repo and
change the *Path setup* and *Project information* sections. 

Now what are the options I added ?


autodoc, autosummary, numpydoc
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These are the **developers best friends** as it allows to automatically parse the doc from the code.
Just add an ``api.rst`` file as in this repo, and put the names of your python module
from your code. The extensions will create an ``autosummary_`` folder that include the
doc for your modules based on what is in the ``_templates`` directory. You can create other
templates or change the existing if needed.

As for ``numpydoc``, the extension allows to use numpy docstring format, which is the one I use.
See an `example of numpy docstring <https://numpydoc.readthedocs.io/en/latest/example.html#example>`_.

In this repo, I have coded fake modules and functions for you to see the results. Explore the few python
files in this repo, and see the output automatically generated from these packages in the html doc.
You could add in your doc some pages dedicated to whatever you want, such as in *Wonderfull explaination*
from the ``doc2.rst`` file.


sphinx_rtd_theme
^^^^^^^^^^^^^^^^

Sphinx allows you to build a doc based on a theme. The repo uses the readthedocs theme,
but you can choose another one amongst the `multiple available themes 
<https://sphinx-themes.org/>`_


sphinx_copybutton
^^^^^^^^^^^^^^^^^

This is a extension that allow to easily copy/paste the code from your doc. That could be very useful,
especially for code example.



IDE tools
---------

I only cover Visual Studio Code example for now, but there are mutliple nice IDE to use.
The purpose of this section is to use nice settings to automatically perform some nice 
actions, such as ``black`` or ``isort``.


Visual Studio Code
^^^^^^^^^^^^^^^^^^

Using VSCode, you could use this settings file:

.. code-block::

    {
        "python.defaultInterpreterPath": "${workspaceRoot}\\.venv\\Scripts\\python.exe",
        "files.exclude": {
            "**/.git": true,
            "**/.svn": true,
            "**/.hg": true,
            "**/CVS": true,
            "**/.DS_Store": true,
            "**/__pycache__": true,
            "**/.mypy_cache": true,
            "**/.pytest_cache": true,
            "**/.venv": false,
            "**/cov.xml": true,
            "**/junit-unit.xml": true,
            "**/.coverage": true,
            "**/coverage-report": true,
            "**/junit.xml": true,
        },
        "python.formatting.provider": "black",
        "editor.formatOnSave": true,
        "autoDocstring.docstringFormat": "numpy",
        "python.linting.enabled": true,
        "python.linting.pylintEnabled": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": true,
        },
    }

.. note::

    The file is located in ``<my-python-repo>/.vscode/settings.json``

"editor.formatOnSave": true
    This will execute ``black`` each time you save a file.

"editor.codeActionsOnSave": {"source.organizeImports": true,}
    Organizing your import on save with ``isort``

"autoDocstring.docstringFormat": "numpy"
    If you use ``numpydoc``, you should definitely use the autodocstring extension from VSCode
    that automatically generates fromatted docstrings for your code. Just fill them !


Note also that using VSCode allows you to use very nice extentions such as:

- GitLens
- Python Extension Pack
- ...