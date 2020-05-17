""" vibhaga setup module """
import os
import setuptools
import vibhaga


def get_vibhaga_requirements() -> []:
    """ Returns a list of requirements """
    output = [] 
    lib_folder = os.path.dirname(os.path.realpath(__file__))
    requirement_path = lib_folder + '/requirements.txt'

    if os.path.isfile(requirement_path):
        with open(requirement_path) as f:
            output = f.read().splitlines()

    return output


setuptools.setup(
    name="vibhaga-keremkoseoglu",
    version=vibhaga.__version__,
    author=vibhaga.AUTHOR,
    author_email=vibhaga.EMAIL,
    description=vibhaga.DESCRIPTION,
    long_description="A dynamic Python module loader",
    long_description_content_type="text/markdown",
    url="https://github.com/keremkoseoglu/vibhaga",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=vibhaga.PYTHON_VERSION,
    install_requires=get_vibhaga_requirements(),
    include_package_data=True
)
