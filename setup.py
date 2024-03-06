from setuptools import find_packages,setup  #find all packages
from typing import List  # for a function get_requirement to return a list

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str):
    '''
    This function will return th e list of requirements
    '''
    requiremets=[]
    with open(file_path) as file_obj:
        requiremets=file_obj.readlines()
        requiremets=[req.replace("\n","") for req in requiremets]

        if HYPEN_E_DOT in requiremets:
            requiremets.remove(HYPEN_E_DOT)
    return requiremets

#Meta data information of project or setup 
setup(
    name='mlproject',
    version='0.0.1',
    author='Sagar Gawali',
    author_email='gawalisagar498@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)