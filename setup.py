from setuptools import setup, find_packages

from mc2pf import __author__, __version__, __license__

try:
    with open("README.md", encoding="utf8") as readme_file:
        readme = readme_file.read()
except TypeError:
    with open("README.md") as readme_file:
        readme = readme_file.read()

setup(
    name="Malleable-C2-Profile-Finder",
    author=__author__,
    version=__version__,
    description="Attempts to find a corresponding Malleable C2 Profile for a given beacon config",
    long_description=readme,
    long_description_content_type="text/markdown",
    license=__license__,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='~=3.5',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mc2pf = mc2pf.cli:run'
        ]
    }
)
