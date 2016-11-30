from os.path import abspath, dirname, join
from setuptools import find_packages, setup


FOLDER = dirname(abspath(__file__))
DESCRIPTION = '\n\n'.join(open(join(FOLDER, x)).read().strip() for x in [
    'README.rst'])

setup(
    name='mailme',
    version='0.0.2',
    description='email module',
    long_description=DESCRIPTION,
    classifiers=[
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    author='Salah Ahmed',
    author_email='salah.ahmed.hslc@gmail.com',
    url='https://twitter.com/saloohimon',
    keywords='mail gmail python',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    tests_require=[])
