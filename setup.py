from __future__ import absolute_import
from setuptools import setup

setup(
    name='dvpp',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='An application',
    long_description=__doc__,
    author='redacted',
    author_email='redacted',
    url='https://ourredactedgitlab.example/secops/dvpp',
    packages=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Private :: Do Not Upload',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=[],
    install_requires=[
        'apscheduler',
        'flask',
        'flask-sqlalchemy',
        'lxml',
        'pycryptodome',
        'fpdf'
    ],
    extras_require={
        'dev': [
            'pytest==6.2.1',
            'pytest-env',
            'tavern==1.12.2',
            'selenium'
        ]
    },
    package_data={
        "": [
            "insecure.pem",
            "insecure.pubkey"
        ]
    }
)
