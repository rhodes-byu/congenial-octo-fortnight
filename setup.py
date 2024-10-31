from setuptools import setup, find_packages


# with open('requirements.txt') as f:
#     requirements = f.readlines()


setup(
    name = 'fortnight',
    version = '0.0.4',
    packages = find_packages(),
    install_requires = ['numpy', 'pandas'],
    author = 'Jake Rhodes',
    author_email = 'rhodes@stat.byu.edu',
    description = 'A package for fortnight',
    data_files = {'fortnight': ['datasets/weather.csv']}
)