import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='MITS_CSN1',
    version='2024.07.25',
    author='M Suryaveera ,Mujahid, Yoshitha',
    author_email='suryaveera0427@gmail.com',
    description='This software is being developed at Madanapalle Institute of Technology and sciences,Madanapalle, Andhra Pradesh,India',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Suryaveera04/MITS_CSN1.git',
    license='GPLv3',
    packages=setuptools.find_packages(),
    install_requires=[
        'psutil',
        'pandas',
        'plotly',
        'matplotlib',
        'resource',
        'validators',
        'urllib3',
        'Pillow',
        'numpy'
    ],
    extras_require={
        'gpu': ['cupy', 'pycuda'],
        'spark': ['pyspark'],
        'dev': ['twine', 'setuptools', 'build'],
        'all': ['cupy', 'pycuda', 'pyspark', 'twine', 'setuptools', 'build']
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.5',
)