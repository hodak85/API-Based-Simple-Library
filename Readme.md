# iTranslate assignment
Create a docker container that can be used to start up a fastAPI server. The
API should contain 2-4 endpoints that interact with a MySQL table*. The design of the endpoints is completely up to you.


# Solution
The solution is provided via docker-compose.

Create a directory and add all the provided folders except pytest to it.
Run the commands as bellow:
- docker-compose build
- docker-compose up -d db (wait for a few seconds for initialization)
- docker-compose up -d
 

The pre-defined user/password is admin/admin.

The documentation about endpoints are in documentation folder.

# Pytest
Install pytest for python3:
- pip3 install -U pytest requests pytest-html jsonschema

Run command:
- py.test

