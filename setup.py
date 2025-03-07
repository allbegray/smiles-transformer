import setuptools
from setuptools import setup, find_packages

setup(name='smiles_transformer',
      version='1.0.0',
      description='Original implementation of the paper "SMILES Transformer: Pre-trained Molecular Fingerprint for Low Data Drug Discovery"',
      long_description=open('README.md').read(),
      author='Shion Honda',
      author_email='https://twitter.com/shion_honda',
      url='https://github.com/DSPsleeporg/smiles-transformer',
      license='MIT',
      install_requires=[
          'numpy',
          'pandas',
          'torch',
          'tqdm',
      ],
      python_requires='>=3',
      packages=['smiles_transformer']
      )
