from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Financial and Insurance Industry',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'Programming Language :: Python :: 3'
]

setup(

    name='fibooks',
    version='1.0.3',
    description='Python library for financial statement analysis. The full documentation can be found at: https://github.com/TimoKats/fibooks',
    long_description='Python library for financial statement analysis. The full documentation can be found at: https://github.com/TimoKats/fibooks',
    author='Timo Kats',
    author_email='tpakats@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='finance',
    packages=['fibooks', 'fibooks.classes'],
    install_requires=['xlsxwriter']

)