import json
import random
import string


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def retrieve_data():
    with open('testdata/testdata.json') as data_file:
        data = json.load(data_file)
        return data


def extract_search_terms(testdata):
    search_terms = testdata["search_terms"]
    results = []
    for term in search_terms:
        results.append(term)
    return results


def extract_empty_search_terms(testdata):
    empty_search_terms = testdata["empty_search_terms"]
    results = []
    for term in empty_search_terms:
        results.append(term)
    return results


def extract_category_paths(testdata):
    category_paths = testdata["category_paths"]
    results = []
    for category in category_paths:
        results.append(category)
    return results


def extract_error_paths(testdata):
    error_paths = testdata["error_paths"]
    results = []
    for error in error_paths:
        results.append(error)
    return results
