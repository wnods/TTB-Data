from setuptools import setup, find_packages

setup(
    name='ttb-data',
    version='0.1',
    description='Pacote para manipulação e análise de dados meteorológico em Tatuoca.',
    author='Wilson Weliton Oliveira de Souza',
    author_email='not-email-available',
    url='https://github.com/wnods/TTB-Data',
    packages=find_packages(),
    install_requires=[
        pandas
        matplotlib
        
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
