from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='example-locustfiles',
    version='0.0.1',
    description='Load locustfiles for training',
    long_description=readme,
    author='Ash Winter',
    author_email='ash@diagramindustries.com',
    url='https://docs.locust.io/en/stable/index.html',
    license=license,
    packages=find_packages
)