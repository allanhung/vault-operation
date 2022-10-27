try:
    import setuptools
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION='0.1.0'

setup(
    name='pyvaultoperation',
    packages=setuptools.find_packages(),
    install_requires=['docopt', 'hvac', 'tqdm'],
    version=VERSION,
    description='get ticket price',
    author='Allan',
    author_email='hung.allan@gmail.com',
    url='https://github.com/allanhung/pyvaultoperation',
    download_url='https://github.com/allanhung/pyvaultoperation/tarball/' + VERSION,
    keywords=['utility', 'miscellaneous', 'library'],
    classifiers=[],
    entry_points={
        'console_scripts': [
            'pyvaultoperation = pyvaultoperation.pyvaultoperation:main',
        ]
    }
)
