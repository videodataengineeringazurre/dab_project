from setuptools import setup,find_packages

setup(
    name="dab_project",
    version="0.0.2",
    description="This contains the code in the ./src directory of the project",
    author="Gaurav Padole",
    packages=find_packages(where="./src"),
    package_dir={"":"./src"},
    install_requires=["setuptools"]
)