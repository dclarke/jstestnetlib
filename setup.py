
from setuptools import setup, find_packages

setup(
    name='jstestnetlib',
    version='0.1',
    description="",
    long_description="""""",
    author='Kumar McMillan',
    author_email='kumar.mcmillan@gmail.com',
    license="Apache License",
    packages=find_packages(exclude=['ez_setup']),
    install_requires=[r for r in open('requirements.txt')
                      if r.strip() and not r.startswith('#')],
    url='',
    include_package_data=True,
    entry_points="""
       [nose.plugins.0.10]
       jstests = jstestnetlib.noseplugins:JSTests
       django_serv = jstestnetlib.noseplugins:DjangoServPlugin
       """,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing'
        ],
    )
