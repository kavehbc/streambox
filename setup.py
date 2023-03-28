import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', "r") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="streambox",
    version="0.0.1",
    author="Kaveh Bakhtiyari",
    author_email="",
    description="A package for generic data science utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kavehbc/streamkit",
    packages=setuptools.find_packages(),
    install_requires=requirements
)
