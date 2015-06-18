try :
    from setuptools import setup
except ImportError :
    from distutils.core import setup

config = {
    'description': 'Simple log file analysis tool',
    'author': 'David Reeve',
    'url': '',
    'download_url': '',
    'author_email': 'lancey@lancey.space',
    'version': '1.0',
    'install_requires': [],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind',
    }

setup(**config)
