from setuptools import setup, find_packages

def get_requirements(filepath):
    requirements = []
    with open(filepath, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    return requirements
setup(

    author_name = "Zahid Hussain",
    author_email = "zahid.dsu@gmail.com",
    version = "0.0.1",
    packages = find_packages(),
    environments = get_requirements("Requirements.txt")
)