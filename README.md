[![Build Status](https://travis-ci.org/ACI-ESP/chepstow.svg?branch=dev)](https://travis-ci.org/ACI-ESP/chepstow)
[![Coverage Status](https://img.shields.io/coveralls/github/ACI-ESP/chepstow/dev.svg)](https://coveralls.io/github/ACI-ESP/chepstow?branch=dev)

Chepstow
=============
This is a test repository for setting up software processes.

Installation
----------------
Install using pip:
```bash
pip install .
```

To install in editable mode so that development is instantly reflected, install like this:
```bash
pip install -e .
```

Testing
-------------
To run the tests, use pip to install nose and then in the base directory run:

```bash
nosetests
```

To run the large graph tests, do this:
```bash
nosetests scaling_checks
```

Running
---------------
It does not do anything so why run it?

Development
-----------
The code mostly follows the [PEP8 coding standard](https://www.python.org/dev/peps/pep-0008/).
If you are using PyCharm, it will highlight PEP8 issues.

The docstrings are using the [Google standard](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
