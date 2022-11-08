from locust import HttpUser, events, task, constant
import common.testdatagenerator as test_data
import os
import sys
import logging
sys.path.append(os.getcwd())


class ConferenceCreateUser(HttpUser):

    wait_time = constant(5.0)

    @events.test_start.add_listener
    def on_test_start(environment, **kwargs):
        logging.info("Conference Create User Test Starting")

    def on_start(self):
        logging.info("New user spawned")

    @task
    def create_user(self):
        email = test_data.id_generator(6) + '@example.com'
        password = test_data.id_generator(10)
        logging.info('Creating user with email: ' + email)
        with self.client.post("/users", data={
            'access_token': 'U7n4qGNgRi2r07E5GSavjJ3MA7dqGLZj',
                'email': email, 'password': password}, catch_response=True) as response:
            if str(response.status_code) != '201':
                logging.error(
                    'Incorrect status code indicating failure: ' + str(response.status_code))
                response.failure(
                    'Incorrect status code indicating failure: ' + str(response.status_code))
            elif response.elapsed.total_seconds() > 0.05:
                logging.warn(
                    'Request was beyond total seconds elapsed tolerance: Total seconds was: ' + str(response.elapsed.total_seconds()))
                response.failure(
                    'Request was beyond total seconds elapsed tolerance: Total seconds was: ' + str(response.elapsed.total_seconds()))

    def on_stop(self):
        logging.info("User has completed their task")

    @events.test_stop.add_listener
    def on_test_stop(environment, **kwargs):
        logging.info("Conference Create User Test Starting")
