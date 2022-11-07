import os
import sys
import random
sys.path.append(os.getcwd())
import common.testdatagenerator as test_data
import common.articlefinder as article_finder
from locust import TaskSet, task, HttpLocust


class CategoryTasks(TaskSet):

    category_paths = test_data.extract_category_paths(test_data.retrieve_data())

    def on_start(self):
        self.client.get("/")

    @task(100)
    def category(self):
        r = self.client.get(random.choice(self.category_paths))
        article_url = article_finder.get_article(r)
        self.client.get(article_url)


class WebsiteUser(HttpLocust):
    task_set = CategoryTasks
    min_wait = 5000
    max_wait = 5000
