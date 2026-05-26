from setuptools import find_packages,setup
HYPEN_E_DOT='_e.'
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> list[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Tanveer',
    author_email='tanveerchougule1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)