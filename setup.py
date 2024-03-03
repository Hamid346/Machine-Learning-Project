from setuptools import find_packages, setup
from typing import List


Hiphen_E = '-e .'


def get_req(file_path: str) -> List[str]:
    '''
    This is the function for getting the requirments.
    '''
    requirments = []
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [line.replace('\n', '') for line in requirments]

        if Hiphen_E in requirments:
            requirments.remove(Hiphen_E)
    return requirments


setup(

    name="Machine-Learning-Project",
    version='0.0.1',
    author='Hamid Naeem',
    author_email='prx.hamid00@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirments.txt')

)
