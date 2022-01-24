import re
import setuptools

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('imgbbpy/__init__.py') as f:
    version = re.search(r"__version__ = '([\d\.]+)'", f.read(), re.MULTILINE)[1] # type: ignore

with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='imgbbpy',
    author='scrazzz',
    url='https://github.com/scrazzz/imgbbpy/',
    project_urls={
        'Documentation': 'https://github.com/scrazzz/imgbbpy/blob/main/documentation.md',
        'Issue tracker': 'https://github.com/scrazzz/imgbbpy/issues'
    },
    version=version,
    packages=['imgbbpy'],
    license='MIT',
    description='An Asynchronous and Synchronous API Wrapper for the Imgbb API.',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7.0'
)
