# python-web-flask-redis-counter

## Description
A POC python flask web counter
that uses redis as a datastore.

Redis is not a database that persists data
neither is it a websocket that updates multiple
clients.

Testing frameworks: *testify* and *selenium*

## Tech stack
- python
  - flask
  - testify
  - selenium
- redis

## Docker stack
- python:latest
- redis:latest
- selenium:latest

## To run
`sudo ./install.sh -u`
Available at http://localhost

## To stop (optional)
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
- https://github.com/codefreshdemo/example_python_redis.git
