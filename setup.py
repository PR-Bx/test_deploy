# import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

# setuptools.setup(
#     name='test_package',
#     version='0.0.1',
#     author='Peter Redshaw',
#     author_email='peter.redshaw@bx-earth.com',
#     description='Testing installation of Package',
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url='https://github.com/PR-Bx/test_deploy',
#     project_urls = {
#         "Bug Tracker": "https://github.com/mike-huls/toolbox/issues"
#     },
#     license='None',
#     packages=['test_package'],
#     install_requires=['numpy'],
# )

from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='test_package',
    url='https://github.com/PR-Bx/test_deploy',
    author='Pete',
    author_email='peter.redshaw@bx-earth.com',
    # Needed to actually package something
    packages=['test_package'],
    # Needed for dependencies
    install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)