# ProjectRepo



## Setup Environment
To setup the environment you first have to install mongodb

On Linux this is as easy as
```
sudo apt-get install mongodb
```

You then need create the required virtual environment and install python packages.
Fortunately, we have a script for that.

Use either
```
./utils/setup.sh
```

or if you have [fabric](http://fabfile.org) use
```
fab setup_env
```

Congratulations, you can now edit and test.

## To run

Setup environment first then execute

```
./run.py
```

and then point your browser (navigate) to [localhost:5000](http://localhost:5000) to test (as well as to?) write unittests and then, push

## Pushing Rules

BEFORE you push:
Make sure that all requirements of the project are in requirements.txt

To do this, type these commands into the console

```
source venv/bin/activate
pip freeze > requirements.txt
```

If you were messing around inside the tool virtual environment then you should also commit those packages to the tool-requirements.txt
```
source tools-env/bin/activate
pip freeze > tool-requirements.txt
```

Make sure that all module documentation is linked in the documentation section below.

If you installed tools that are required to run the server, add them to the readme under setup environment.

Add any files that you many have created.

If there are any temporary files that have been created and that should not be included in the repository, add them to .gitignore

## Tools

Tools are launched from the tools directory. They allow you to do things like create and list users in the database, as well as delete the whole database (do this only if testing).

The tools have their own separate virtual environment for themselves and are run from there by default.

To execute a tool:

```
./tools/<toolname>.py
```

No need to enter a virtual environment

Code | Description
---- | --------------------------------
`./tools/addUsers.py` | adds users in /libs/usernames
`./tools/createPost.py` | Creates a post (The program will prompt you for a user, title, and content text)
`./tools/listUsers.py` | lists all users
`./tools/deleteDB.py` | deletes the WHOLE database (use only localy)
`./tools/deleteUsers.py` | deletes ALL the users but no other part of the database
`./tools/deletePosts.py` | deletes ALL the posts but no other part of the database

## Templates

All HTML is generated by the server and the templates are stored in the application/templates.

Static files such as images, css, and javascript go into the application/static/imgs, application/static/css and application/static/js respectively.

## Various documentation

Flask: [http://flask.pocoo.org/docs/0.10/](http://flask.pocoo.org/docs/0.10/)

Flask-mongoengine: [http://docs.mongoengine.org/](http://docs.mongoengine.org/)

Flask-WTF: [https://flask-wtf.readthedocs.org/en/latest/](https://flask-wtf.readthedocs.org/en/latest/)

Unittesting Flask: [http://flask.pocoo.org/docs/0.10/testing/](http://flask.pocoo.org/docs/0.10/testing/)
## Bugs

If you happen to find a bug, report it and then attempt to fix it. If you cannot fix it, indicate that you could not in the bug report.


The issue tracker is [here](https://github.com/BaySchoolCS2/ProjectRepo/issues/new)


## MISC

 - Documentation for usage and installing that is very verbose should go into the wiki
