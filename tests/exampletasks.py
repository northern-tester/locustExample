import random
import os
import sys
sys.path.append(os.getcwd())
import common.testdatagenerator as test_data
import common.articlefinder as article_finder
from locust import HttpLocust, TaskSet, task


class ExampleTasks(TaskSet):

    data = test_data.retrieve_data()
    search_terms = test_data.extract_search_terms(data)
    empty_search_terms = test_data.extract_empty_search_terms(data)
    category_paths = test_data.extract_category_paths(data)
    error_paths = test_data.extract_error_paths(data)

    def on_start(self):
        self.client.get("/")

    @task(60)
    def search_results(self):
        r = self.client.get("/search/?query=" + random.choice(self.search_terms))
        article_url = article_finder.get_article(r)
        self.client.get(article_url)

    @task(4)
    def search_no_results(self):
        self.client.get("/search/?query=" + random.choice(self.empty_search_terms))

    @task(35)
    def category(self):
        r = self.client.get(random.choice(self.category_paths))
        article_url = article_finder.get_article(r)
        self.client.get(article_url)

    @task(1)
    def invoke_error(self):
        self.client.get(self.error_paths)


class WebsiteUser(HttpLocust):
    task_set = ExampleTasks
    # If you don't specify a min and max wait, it will default to a second, keep the same for steady spawn rate
    min_wait = 5000
    max_wait = 5000
