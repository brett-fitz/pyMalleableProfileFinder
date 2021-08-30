from setuptools import setup

setup(
    name="Malleable-C2-Profile-Finder",
    description="Attempts to find a corresponding Malleable C2 Profile for a given beacon config",
    author="Brett Fitzpatrick",
    version="0.1",
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
            'mc2pf = __main__:main'
        ]
    }
)
