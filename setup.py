from distutils.core import setup

setup(
    name='youplay',
    version='0.1',
    author='Alexandre Passant',
    author_email='alex@passant.org',
    packages=['youplay'],
    scripts=['bin/youplay'],
    url='http://pypi.python.org/pypi/youplay',
    license='LICENSE.txt',
    description='Extract who's and what's playing - artist(s) and track(s) - from a YouTube music video.',
    long_description=open('README.txt').read(),
    install_requires=[
        "google-api-python-client >= 1.2",
        "httplib2 >= 0.9",
        "requests >= 2.3.0",
        "wsgiref >= 0.1.2"
    ],
)
