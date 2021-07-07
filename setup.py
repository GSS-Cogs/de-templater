import setuptools

setuptools.setup(
    name = 'detemplater',
    packages = ['detemplater'],
    version = '0.0.1',
    description = 'A transform templating utilities for idp dissemination data engineers to use',
    author = 'Michael Adams',
    author_email = 'michael.adams@ons.gov.uk',
    url = 'https://github.com/GSS-Cogs/de-templater',
    download_url = 'https://github.com/GSS-Cogs/de-templater/archive/0.1.tar.gz',
    keywords = ['template', 'transform', 'pandas', 'databaker'],
    install_requires=[
        'gssutils @ git+git://github.com/GSS-Cogs/gss-utils.git#egg=gssutils',
        'PyYAML==5.4.1'
    ],
    entry_points={
        'console_scripts': [
            'detemplate = detemplater.cli:run_cli'
            ]
    },
    dependency_links = [
        'http://github.com/GSS-Cogs/gss-utils/tarball/master#egg=gssutils'
        ],
    package_data={'detemplater': ['detemplater/journey.yaml']}
)