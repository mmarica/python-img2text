from setuptools import setup

config = {
    'name': 'img2text.py',
    'description': 'Convert images into ascii art',
    'url': 'https://github.com/mmarica/python-img2text',
    'download_url': '',
    'version': '0.1',
    'author': '"Mihai Marica',
    'author_email': 'mihai.marica82@yahoo.com',
    'install_requires': ['Pillow'],
    'license': 'MIT',
    'scripts': ['img2text.py'],
}

setup(**config)