from os.path import abspath, dirname, join
from setuptools import find_packages, setup


with open('README.md') as f:
    DESCRIPTION = f.read()


setup(
    name='mailme',
    version='1.0.0',
    description='email module',
    long_description=DESCRIPTION,
    author='Salah Ahmed',
    author_email='salahs.email@pm.me',
    url='https://github.com/salah93/mailme',
    keywords='mail python',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
