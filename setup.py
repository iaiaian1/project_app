from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project_app/__init__.py
from project_app import __version__ as version

setup(
	name="project_app",
	version=version,
	description="Project App",
	author="iaiaian1",
	author_email="iaiaian1",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
