from setuptools import setup

setup(
    name='Prudent',
    version='0.1.0',
    description='Elegant lazy datastructures for Python',
    long_description=open('README.rst', 'rb').read().decode('utf-8'),
    author='Eeo Jun',
    author_email='141bytes@gmail.com',
    url='https://github.com/eugene-eeo/mailthon/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    package_data={'prudent': ['LICENSE', 'README.rst']},
    packages=['prudent'],
    platforms='any',
    zip_safe=False,
)
