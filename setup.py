from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in apcc/__init__.py
from apcc import __version__ as version

setup(
	name="apcc",
	version=version,
	description="apcc",
	author="jabir",
	author_email="jabir@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
