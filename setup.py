try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Broadcaster project to help post messages to different sites','author': ['Gorbin', 'Niyas', 'Vinayak'],'url':'','download_url':'','author_email':'','version':'','install_requires':[],'packages':['Broadcaster'],'scripts':[], 'name':'Broadcaster'
}

setup(**config)
