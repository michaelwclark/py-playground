import sys
from setuptools import find_packages, setup

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name='pygain-job',
    packages=find_packages(
        exclude=["*.test", "*.test.*", "test.*", "test"]
    ),
    install_requires=[
        'pygain-internal-core>=1.0,<1.2'
    ],
    extras_require={
        'tests': [
            'pygain-dev~=0.0.1',
            'pytest==4.5.0',
            'pytest-cov==2.7.1',
            'mock==3.0.5',
            'python-semantic-release==3.10.0; python_version <= \'2.7\'',
            'python-semantic-release==4.1.1; python_version >= \'3.7\'',
            'flake8==3.7.7',
        ],
    },
    entry_points={'console_scripts': ['semantic-release = semantic_release.cli:main']},
    version_format='{tag}',
    setup_requires=['setuptools-git-version==1.0.3'],
    description='Gain Compliance library for defining and interacting with the job resource.',
    author='Gain Compliance',
    author_email='development-public@gaincompliance.com',
    url='https://github.com/GainCompliance/pygain-job',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python'
    ]
)
