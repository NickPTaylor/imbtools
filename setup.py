"""
Setup for IMB tools package.
"""
import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='imbtools',
    version='0.0.0',
    description="A flask app for IMB work.",
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/NickPTaylor/imbtools',
    author='Nick Taylor',
    author_email='nick.taylor@example.com',
    keywords=['imb', 'rota reports'],
    license='MIT',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Flask",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5"
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ]
)
