from setuptools import find_packages,setup
from typing import List
s='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if s in requirements:
            requirements.remove(s)
    return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Aravind',
    author_email='aravindbobbala@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)