from setuptools import setup

setup(
    name='diff',
    version='0.1.0',
    py_modules=['diff'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'diff = diff:hello',
        ],
    },
)
