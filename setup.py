'''
Important for packaging and distribution


'''
from setuptools import find_packages,setup


def get_requirements()->list[str]:
    '''
    This function returns list of requirements
    '''
    requirement_list:list[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ## ignore empty line and -e .
                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    auther="Tushar Patil",
    author_email="tushpatilv4631@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)