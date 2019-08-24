from setuptools import setup, find_packages

with open('README.md', 'r') as ld:
    long_description = ld.read()

setup(
    name="",
    version="0.0,1",
    author="BalenD",
    author_email="Balen1996@hotmail.com",
    description="CLI that shows all TODO comments in your files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BalenD/TODO-cli",
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

