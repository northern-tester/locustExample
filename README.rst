======================
How Do I Load Tests
======================

Installing 
==========

In the root directory run:

pip3 install -r requirements.txt

Introduction
============

Initial load tests using LocustIO for the How Do I site

Documentation for Locust can be found here:

https://docs.locust.io/en/latest/index.html

Creating a Model
================

In order to run with with a controlled increase in usage:

You need to control the following:

Number of Users (-c)
Hatch Rate (-r)
Duration of test expressed
Max and Min Wait (set this to a uniform value as in 1000ms for both)

locust -f example.py --csv=../results --no-web -c 50 -r 1 -t 10mins

    min_wait = 5000
    max_wait = 5000

50 users spawned 1 at a time every 5 seconds with a cap of 500 requests

Running in Multiple Environments
================================

Pass --host to run in different environments, if you specify this in the task the arg will be overwritten.