# ORION LABS

## Environment
- Linux Ubuntu 16.04 (Virtual Box)
- Python3.5.2
- Python3 unittest
- Pip3


## Generate
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

To see admin page with the list of cars:

```
$ curl http://127.0.0.1:5000/v1/admin/inventory/p4ssw3rd
```

## Challenge
To move the closest car to a designated floor:

- floor_id is the id associated with the floor letter
- Can be found as an admin using the route above
- You can also comment out the printing statements in the `v1/api/__init__.py` file to get a full detailed list of the car map and floor ids.

```
$ curl http://127.0.0.1:5000/v1/callcar/<floor_id>/
```

You can find the updated `find_closest_car` and `call_car` methods in the `__init__.py` file in the `v1/api` directory.

## Tests

I've added two new tests in the `v1/api/tests_vator.py` file  that use the same Elevator initialization array in the `__init__.py` file to make sure that regardless of the items in the array, as long as the items are passed in sequential desc to asc order as it relates to the floor map, the tests will pass.

Currenty breaking with Python3 and pytest

```
$ cd $REPO_ROOT/py-ele/py_ele
```

```
$ pytest v1/api/tests/
```


To validate tests, I used python3 unittests. Get to the `v1/api/tests/` directory and enter:

```
$ python3 test2_validator.py
```



