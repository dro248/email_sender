from setuptools import setup, find_packages

setup(name='email_sender',
      version='0.1.0',
      description='A simple email sender written in Python.',
      url='https://github.com/dro248/email_sender',
      author='David Ostler',
      author_email='david.ostler001@gmail.com',
      license=None,
      packages=find_packages(exclude=['tests', '.idea', '.cache', '__pycache__']),
      include_package_data=True,
      zip_safe=False)
