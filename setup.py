from setuptools import setup

setup(name='Mosaic',
      version='1.1',
      author='Mandeep Bhutani',
      packages=['player', 'player.images'],
      package_data={"player.images": '*.png',
                    "player": '*.toml'},
      install_requires=[
        'mutagen==1.34',
        'pytoml==0.1.10',
        'appdirs==1.4.0'
      ],
      entry_points='''
        [console_scripts]
        mosaic=player.mosaic:main
        ''',
      )
