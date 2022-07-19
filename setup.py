from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Financial and Insurance Industry',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'Programming Language :: Python :: 3'
]

setup(
    name='fibooks',
    version='2.0.2',
    packages=['fibooks'],
    include_package_data=True,
    url='https://github.com/TimoKats/fibooks/',
    license='MIT',
    author ='Timo Kats',
    author_email='tpakats@gmail.com',
    description='Python library for financial statement analysis. More information availible at: https://github.com/TimoKats/fibooks/',
    long_description='Python library for financial statement analysis. More information availible at: https://github.com/TimoKats/fibooks/',
    install_requires=['openpyxl','pandas','setuptools'],
    keywords=['finance', 'data','valuation','excel']
)
