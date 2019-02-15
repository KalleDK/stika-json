from setuptools import setup, find_namespace_packages


with open('LICENSE') as f:
    license_ = f.read()


with open('README.md') as f:
    readme = f.read()

setup(
    name='stika_json',
    version='0.9',
    packages=find_namespace_packages(include=['stika.*']),
    url='https://github.com/KalleDK/stika-json',
    license=license_,
    author='Kalle R. Møller',
    author_email='pypi.org@k-moeller.dk',
    description='JSON for Dataclasses',
    long_description=readme,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ]
)
