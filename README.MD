use pip to install virtualenv

    $ sudo pip install virtualenv

Once you have virtualenv installed, just fire up a shell and create your own environment. I usually create a project folder and a venv folder within:

    $ mkdir myproject
    $ cd myproject
    $ virtualenv venv
    New python executable in venv/bin/python
    Installing setuptools, pip............done.

Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:

    $ . venv/bin/activate

If you are a Windows user, the following command is for you:

    $ venv\Scripts\activate

install dependency package:
    
    $ pip install -r requirement.txt