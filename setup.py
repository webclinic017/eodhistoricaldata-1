"""Setup file for PyPI"""

# To use a consistent encoding
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="eodhistoricaldata",
    version="0.4.1",
    description="EOD Historical Data Python Library (Unofficial)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://whittle.medium.com",
    author="Michael Whittle",
    author_email="michael@lifecycle-ps.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(include=["eodhistoricaldata"]),
    include_package_data=True,
    install_requires=["websockets==10.0","websocket-client==1.2.1","rich==10.14.0"],
    entry_points={
        "console_scripts": [
            "whittlem=eodhistoricaldata.__main__:main",
        ]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest==6.2.5"],
    test_suite="tests"
)
