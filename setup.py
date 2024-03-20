# setup.py function is to make this machine learning running as a package

# find_packages is library for automaticly finding package in directory (requirements.txt)
from setuptools import find_packages,setup
from typing import List

# (-e .) is function in requirements.txt that running automaticly this setup.py
HYPEN_E_DOT='-e .'

# function for read requirements.txt
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        # read the package as a line
        requirements=file_obj.readlines()
        
        # removing the space between the line
        requirements=[req.replace("\n","") for req in requirements]
        
        # condition to remove (-e .) after setup.py automaticly running
        # this (-e .) will causing error if read as package
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements

# information requirements of the project    
setup(
name='mlproject1',
version='0.0.1',
author='davidadityoo',
author_email='davidadityoo@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)