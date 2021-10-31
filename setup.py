"""Setup file for PyPI"""

import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="eodhistoricaldata",
    version="0.1.0",
    description="EOD Historical Data Python Library (Unofficial)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/whittlem/eodhistoricaldata",
    author="Michael Whittle",
    author_email="michael@lifecycle-ps.com",
    license="MIT",
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(include=["eodhistoricaldata"]),
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "whittlem=eodhistoricaldata.__main__:main",
        ]
    },
    setup_requires=["pytest-runner"],
    tests_require=["pytest==6.2.5"],
    test_suite="tests"
)
