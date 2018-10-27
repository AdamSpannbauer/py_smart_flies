from setuptools import setup

version = {}
with open("smart_flies/version.py") as f:
    exec(f.read(), version)

setup(name='smart_flies',
      version=version['__version__'],
      description='Simple genetic algorithm demo/visualization.',
      author='Adam Spannbauer',
      author_email='spannbaueradam@gmail.com',
      url='https://github.com/AdamSpannbauer/py_smart_flies',
      packages=['smart_flies'],
      license='MIT',
      install_requires=[
          'numpy',
      ],
      extras_require={
          'cv2': ['opencv-contrib-python >= 3.4.0']
      },
      keywords=['genetic algorithm', 'opencv']
      )
