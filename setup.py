from setuptools import setup, find_packages

setup(
    name='python-broadcaster',
    version='1.0.0',
    author='Gorbin, Niyas, Vinayak',
    author_email='broadcaster.thelycaeum@gmail.com',
    packages=find_packages(exclude=[]),
    scripts=['broadcast'],
    url='https://github.com/niyaspavil/Broadcaster',
    description='Broadcaster helps to post messages to different networking entities',
    long_description=open('README.md').read(),
    install_requires=[
        "argparse==1.2.1",
	"termcolor==1.1.0",
	"tweepy==2.3.0",
	"xmlrpclib==1.0.1"
	
       ],
)
