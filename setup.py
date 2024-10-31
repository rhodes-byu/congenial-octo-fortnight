from setuptools import setup, find_packages


# with open('requirements.txt') as f:
#     requirements = f.readlines()


setup(
    name = 'fortnight',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = ['numpy', 'pandas']
)