``python-template-repo`` README
=============================

All of the following doc is WIP

How to use
----------
WIP


Reproduce step-by-step
----------------------

First, install ``poetry`` using following the online doc.
Then, create a poetry repo:

.. code-block::

    poetry new <my-python-repo>

Add the python ``.gitignore`` file.

Create a virtual env in the same folder (especially for *Visual Studio Code* users) and
install some basics:

.. code-block::

    python -m venv .venv
    poetry add pylint pre-commit black isort commitizen
    poetry add sphinx sphinx-rtd-theme sphinx_copybutton numpydoc

pre-commit
^^^^^^^^^^

Copy past the ``.pre-commit-config.yaml`` file and install the pre-commit by running:

.. code-block::

    pre-commit install

Or create your own following the `official pre-commit documentation 
<https://pre-commit.com/>`_

black
^^^^^

bla bla

pylint
^^^^^^
bla bla

sphinx
^^^^^^

Create the basic sphinx files by executing:

.. code-block::

    mkdir doc
    cd doc
    sphinx-quickstart

Visual Studio Code
^^^^^^^^^^^^^^^^^^

If you're using VSCode, you could use this settings file:

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