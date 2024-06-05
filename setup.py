from setuptools import find_packages,setup
from typing import List
HYP_E = '-e .'
def get_requirements(file_path:str)->List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYP_E in requirements:
            requirements.remove(HYP_E)
            
    return requirements
        
setup(
    name='mlop_prac',
    version='0.0.1',
    author='viyas52',
    author_email='vyas.illusionist@gmail.com',
    packages=find_packages(),
    install_requirements = get_requirements('requirements.txt')
)