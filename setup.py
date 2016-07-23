import sys
from setuptools import setup, find_packages

if sys.version_info >= (3, 5):
    dependencies = ['pyqt5']
else:
    dependencies = []

setup(name='MandeepPAD',
      version='0.0.6',
      author='Mandeep Bhutani',
      packages=find_packages(),
      include_package_data=True,
      install_requires=dependencies,
      entry_points='''
        [console_scripts]
        MandeepPAD=editor.mpad:main
        ''',
      )
