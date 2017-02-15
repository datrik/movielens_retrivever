from setuptools import setup, find_packages

setup(name='movielens',
      version='0.1',
      description='A package to download movielens dataset and create interactions matrices',
      author='Datrik Intelligence, S.A.',
      author_email='info@datrik.com',
      url='https://github.com/datrik/movielens_retrivever',
      download_url='https://github.com/datrik/movielens_retrivever',
      packages=find_packages(),
      license='MIT',
      keywords='datrik movielens dataset interaction matrix',
      classifiers=["Development Status :: 1 - Beta",
                   "Intended Audience :: Developers",
                   "Intended Audience :: Science/Research",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Software Development :: Libraries :: Python Modules"
                   ],
     )
