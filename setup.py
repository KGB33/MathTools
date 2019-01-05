from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_disc = fh.read()

setup(
    name='MtTools',
    version='0.1.2',
    author='Kelton Bassingthwaite',
    author_email='MtTools@bassingthwaite.org',
    packages=find_packages(exclude=['docs', 'tests*']),
    url='https://github.com/KGB33/MathTools',
    license='LICENSE.txt',
    description='Tools for mathematical operations',
    long_description=long_disc,
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires=['numpy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
