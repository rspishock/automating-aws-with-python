from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Ryan Spishock',
    author_email='ryan.spishock@gmail.com',
    description='Webotron is a tool to deploy static websites to AWS.',
    license='GVLv3+',
    packages=['webotron'],
    url='https://github.com/rspishock/automating-aws-with-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [cosnole_scripts]
        webotron=webotron.webotrol:cli
    '''
)