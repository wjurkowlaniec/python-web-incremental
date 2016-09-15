# python-web-incremental
The idea was is to create simple applications in Python on the web. So I found Transcrypt and it works just fine.

Proof of concept working incremental game from python



Installation
------------
Create venv for python 3.5:

    $ virtualenv --python=/usr/bin/python3.5 venv

Install requirements

.. code-block:: bash

    $ pip install -r requirements.txt


How to make it work
------------
To compile from python to javascript, run

    $ transcrypt inc.py

or use watchdog script

    $ python watch.py
