# Python Version of the Elevator Server
This doc should give you links to everything you need to know to develop
the elevator-server code in Python (currently only tested in Python 3.6).

# Generate
We are using the [`swagger_py_codegen`](https://github.com/guokr/swagger-py-codegen)
tool to build the generic [Flask](http://flask.pocoo.org/) and
[Flask-RESTful](http://flask-restful-cn.readthedocs.org/en/0.3.5/) scaffolding
for our project.

Basically, you need to install the tool:
`$ pip3 install swagger-py-codegen`

First, let's get the repo:
```
> $ git clone https://github.com/nickolasteixeira/Orion_Labs.git
```
Then, to run the generation:

```
$ cd $REPO_ROOT
$ swagger_py_codegen -s ./elevator.yml py-ele
$ cd py-ele
$ pip3 install -r requirements.txt
```

FYI: The force-overridden files have already been added to the `.gitignore` file.

To run the server:
```
$ cd $REPO_ROOT/py-ele/py_ele
$ python3 __init__.py
```

To see the welcome message from a running server:
```
$ curl http://127.0.0.1:5000/v1/welcome
```
To see admin page with list of cars:
```
$ curl http://127.0.0.1:500/v1/admin/inventory/p4ssw3rd

```


To run the unit tests:
Currenty breaking with Python3
```
$ cd $REPO_ROOT/py-ele/py_ele
$ pytest v1/api/tests/
```
