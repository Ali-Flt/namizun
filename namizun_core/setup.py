from setuptools import setup

setup(name='namizun_core',
      version='2.0.0',
      description='namizun main functions',
      author='Aflt',
      author_email='aflt1998@gmail.com',
      url='https://github.com/Ali-Flt/namizun',
      setup_requires=['wheel'],
      install_requires=['psutil==5.9.4',
                        'redis==4.3.5',
                        'pytz==2022.6',
                        'numpy==1.24.2',
                        'python-crontab==3.0.0']
      )