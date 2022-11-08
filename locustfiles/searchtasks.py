import os
import sys
import random
sys.path.append(os.getcwd())
import common.testdatagenerator as test_data
import common.articlefinder as article_finder
from locust import TaskSet, task, HttpLocust


class SearchTasks(TaskSet):

    search_terms = test_data.extract_search_terms(test_data.retrieve_data())

    def on_start(self):
        self.client.get("/")

    @task(100)
    def search_results(self):
        r = self.client.get("/search/?query=" + random.choice(self.search_terms))
        article_url = article_finder.get_article(r)
        self.client.get(article_url)


class WebsiteUser(HttpLocust):
    task_set = SearchTasks
    min_wait = 5000
    max_wait = 5000
