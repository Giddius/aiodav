import re

from setuptools import setup, find_packages
# from setuptools.command.install import install as InstallCommand
# from setuptools.command.test import test as TestCommand

with open('aiodav/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)
                        
with open('requirements.txt', 'r') as file:                        
    INSTALL_REQUIRES = file.readlines()

with open('README.md', 'r') as readme:
    setup(
        name='aiodav',
        version=version,
        description="A Python Async WebDAV Client",
        long_description=ascii(readme.read()),
        long_description_content_type='text/markdown',
        license="MIT License",
        author="Jorge Alejandro Jimenez Luna",
        author_email="jorgeajimenezl17@gmail.com",
        url="https://github.com/jorgeajimenezl/aiodav",
        classifiers=[
            "Intended Audience :: Developers",
            "License :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Topic :: Internet :: Downloader",
        ],
        keywords="webdav, client, files, internet, download, upload",
        install_requires=INSTALL_REQUIRES,
        packages=find_packages(),
    )