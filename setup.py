from setuptools import find_packages,setup
def get_requirements(file_path:str)->list[str]
    """ This function will require the list of requirements"""
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    if "-e ." in requirements:
        requirements.remove("-e .")
setup(
        name= "MLProject",
        version="0.0.1",
        author = "Ravi Teja",
        author_email="kurakulavenkataraviteja@gmail.com",
        packages=find_packages(),
        install_requires = get_requirements("requirements.txt")


)