# Golang Version of the Elevator Server
This doc should give you links to everything you need to know to develop
the elevator-server code in Go (currently only tested in Go 1.5.3).

# Generate
We are using the [`go-swagger`](github.com/go-swagger/go-swagger/cmd/swagger)
tool to build the generic scaffolding for our project.

First, let's get the repo, and put it in the correct location:
```
$ mkdir -p $GOPATH/src/github.com/onbeep/
$ cd $GOPATH/src/github.com/onbeep/
$ git clone git@github.com:OnBeep/elevator-server.git
```
At this point we're reference `$GOPATH/src/github.com/onbeep/elevator-server`
as `$REPO_ROOT`.

Now, install the code generation tool:
```
$ go get -u github.com/go-swagger/go-swagger/cmd/swagger
```

Let's generate the server code, and run it:
```
$ cd $REPO_ROOT/go-ele
$ swagger generate server -f ../elevator.yml --include-main
$ go install ./...
$ $GOPATH/bin/lifty-server --port 5000
>> serving lifty at http://127.0.0.1:5000
```

You should be able to see the server responding:
```
$ curl http://127.0.0.1:5000/v1/welcome
>>
```

To run the unit tests:
```
$ cd $REPO_ROOT/go-ele
$ go test ./...
```
