from setuptools import setup, find_packages

setup(
    name='bf4py',
    version='0.1.0',
    url='https://github.com/joh-nnyS/bf4py',
    author='joqueka',
    author_email='',
    description='A Python Package for retrieving data from boerse-frankfurt.de',
    packages=find_packages(),
    install_requires=[
        'requests',
        'sseclient',
    ],
)