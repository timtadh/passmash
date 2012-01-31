from distutils.core import setup
import passmash

setup(name='passmash',
      version=str(passmash.RELEASE),
      description=('A site specific password munger.'),
      author='Tim Henderson',
      author_email='tim.tadh@gmail.com',
      url='https://www.github.com/timtadh/passmash',
      license='GPLv2',
      provides=['passmash'],
      scripts=['pm'],
      py_modules=['passmash'],
      platforms=['unix', 'darwin', 'windows'],
      data_files=[('.', ['GPL', 'LICENSE', 'README.md'])],
)

