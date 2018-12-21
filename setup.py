from setuptools import setup, find_packages

setup(name='leviafunc',
      version='0.1',
      description='NLP for legal texts',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='keywords, key phrases, legal act, date, country, organization',
      url='http://github.com/alissiawells/Leviafunc',
      author='alissiawells',
      author_email='alissiagood@yandex.ru',
      license='MIT',
      test_suite='tests',
      packages=find_packages(),
      install_requires=[
      'jupyter',
      'numpy',
      'pymorphy2==0.8',
      'nltk==3.2.1',
      'scikit-learn==0.20.1',
      'dateparser==0.7.0',
      'natasha==0.10.0',
      'yargy==0.11.0',
      'yake==0.3.7',
      'python-docx==0.8.7',    
      ],
      include_package_data=True,
      zip_safe=False)
