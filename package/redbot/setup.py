from setuptools import setup

setup(name='redBot',
      version='0.1',
      description='Reddit chatbot framework',
      url='http://github.com/griffinpuc/redBot',
      author='Griffin Puc',
      license='MIT',
      packages=['redBot'],
      zip_safe=False)

entry_points={
        "console_scripts": [
            "redBot=redBot.__main__:main",
        ]
    },