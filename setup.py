import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='test_package',
    version='0.0.1',
    author='Peter Redshaw',
    author_email='peter.redshaw@bx-earth.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/PR-Bx/test_deploy',
    project_urls = {
        "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
    },
    license='MIT',
    packages=['test_package'],
    install_requires=['numpy'],
)