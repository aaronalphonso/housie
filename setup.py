import os
import setuptools

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "README.MD"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="housie",
    version="0.1.7",
    author="Aaron Alphonso",
    author_email="alphonsoaaron1993@gmail.com",
    description="All the core logic for playing/simulating the popular game 'Housie' "
                "(also known as 'Bingo' or 'Tambola')",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aaronalphonso/housie",
    packages=['housie', 'housie.models'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='python housie core tambola bingo ticket generator board game',
    project_urls={
        'Source': "https://github.com/aaronalphonso/housie"
    },
)
