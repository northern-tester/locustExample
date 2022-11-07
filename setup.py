from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='how-do-i-load-locustfiles',
    version='0.0.1',
    description='Load locustfiles for the how-do-i website',
    long_description=readme,
    author='Ash Winter',
    author_email='awinter@equalexperts.com',
    url='http://gitlab.azure.digitalplatform.coop.co.uk/awinter/how-do-i-load-locustfiles',
    license=license,
    packages=find_packages
)