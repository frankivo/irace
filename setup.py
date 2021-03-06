"""iRace's setup.py"""


import io
import os
from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """TestCommand subclass to use pytest with setup.py test."""

    def finalize_options(self):
        """Find our package name and test options to fill out test_args."""

        TestCommand.finalize_options(self)
        self.test_args = ["-v", "-rx", "--cov-report", "term-missing", "--cov",
                          "irace", "test"]
        self.test_suite = True

    def run_tests(self):
        """pytest discovery and test execution."""

        import pytest
        raise SystemExit(pytest.main(self.test_args))


def long_description(filename="README.md", encoding="utf-8"):
    """Return the contents of the README.md file."""

    with io.open(filename, "r", encoding=encoding) as readme:
        return readme.read()


setup(
    name="iRace",
    version="0.0.1",
    author="Adam Talsma",
    author_email="adam@talsma.ca",
    url="https://github.com/a-tal/irace",
    download_url="https://github.com/a-tal/irace",
    description="iRacing web frontend for league stats",
    long_description=long_description(),
    include_package_data=True,
    zip_safe=False,
    package_data={"iRace": [
        os.path.join("irace", "templates", f) for f in
        os.listdir(os.path.join("irace", "templates"))
    ]},
    packages=find_packages(exclude=["test"]),
    python_requires=">= 3.7.4",
    install_requires=[
        "RequestsThrottler >= 0.2.5",
        "requests >= 2.2.0",
        "docopt >= 0.6.1",
        "jinja2 >= 2.10.3",
    ],
    cmdclass={"test": PyTest},
    tests_require=["mock", "pytest", "pytest-cov"],
    entry_points={"console_scripts": [
        "irace-populate = irace.populate:main",
        "irace-lap = irace.parse_laps:main",
        "irace-generate = irace.generate:main",
        "irace-league = irace.leagues:main",
        "irace-results = irace.parse_race:main",
    ]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
