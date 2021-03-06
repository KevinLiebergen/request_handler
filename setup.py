# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


project_urls = {
    'Home page': 'https://github.com/KevinLiebergen/request_handler'
}

# This call to setup() does all the work
setup(
    name="request-handler",
    version="0.1.3",
    description="Request handler library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kevin van Liebergen",
    author_email="example@email.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["request_handler"],
    include_package_data=True,
    install_requires=["requests"],
    project_urls=project_urls
)

