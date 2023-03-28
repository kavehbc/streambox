import pathlib
import pkg_resources
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', "r") as f:
    install_requires = f.read().splitlines()

# with pathlib.Path('requirements.txt').open() as requirements_txt:
#     install_requires = [
#         str(requirement)
#         for requirement
#         in pkg_resources.parse_requirements(requirements_txt)
#     ]

setuptools.setup(
    name="streambox",
    version="0.0.1",
    author="Kaveh Bakhtiyari",
    author_email="",
    description="A package for generic data science utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kavehbc/streambox",
    packages=setuptools.find_packages(),
    install_requires=install_requires
)
