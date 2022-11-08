from locust import HttpUser, TaskSet, events, task, constant
import common.testdatagenerator as test_data
import os
import sys
sys.path.append(os.getcwd())


class ConferenceCreateUser(HttpUser):
    wait_time = constant(5)

    @task
    def create_user(self):
        email = test_data.id_generator(6) + '@example.com'
        password = test_data.id_generator(10)
        with self.client.post("/users", data={
            'access_token': 'U7n4qGNgRi2r07E5GSavjJ3MA7dqGLZj',
            'email': email,
                'password': password}, catch_response=True) as response:
            assert response.status_code == 201
