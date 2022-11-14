======================
Locust Example Repo
======================

Installing 
==========

In the root directory run:

pip3 install -r requirements.txt

Introduction
============

Initial load tests using LocustIO

Documentation for Locust can be found here:

https://docs.locust.io/en/latest/index.html

Creating a Model
================

In order to run with with a controlled increase in usage:

You need to control the following:

Number of Users (-u)
Hatch Rate (-r)
Duration of test expressed
Wait set as a constant in the test example below

locust -f locustfiles/conferencecreateuser.py --csv=../results -u 1 -r 1 -t 10s --host http://localhost:9000

After running this in terminal, open http://localhost:8089/# and you should be able to run the test and see the output

Running in Multiple Environments
================================

Pass --host to run in different environments, if you specify this in the task the arg will be overwritten.