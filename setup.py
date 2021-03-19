from setuptools import setup, find_packages

setup(
    name='torch-semantic-segmentation',
    version='0.0.0',
    author='erniogi',
    description='Pytorch implementation for semantic segmentation',
    url='https://github.com/erniogi/torch-semantic-segmentation',
    packages = find_packages(exclude=("configs", "tests*")),
    python_requires="==3.6.9",
)
