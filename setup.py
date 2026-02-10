from setuptools import setup,find_packages
setup(name="nullsec-phantom-id",version="2.0.0",author="bad-antics",description="Network identity spoofing and phantom device creation",packages=find_packages(where="src"),package_dir={"":"src"},python_requires=">=3.8")
