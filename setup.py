from setuptools import setup, find_packages

from my_pip_package import __version__

setup(
    name='my_pip_package',
    version=__version__,

    url='https://github.com/richardjl1234/testpip_venv',
    author='Richard Jiang',
    author_email='jianglei50@hotmial.com',
    install_requires=[
        'pandas',
    ],

    py_modules=find_packages(),
)