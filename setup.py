from distutils.core import setup

setup(name='smtools',
      version='0.1dev',
      description='NEIC ShakeMap Strong Motion Tools',
      author='Mike Hearne',
      author_email='mhearne@usgs.gov',
      url='',
      packages=['smtools'],
      install_requires=['numpy', 'matplotlib', 'scipy'],
      scripts = ['getstrong.py','smcheck.py'],
)
