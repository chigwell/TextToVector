from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TextToVector',
    version='0.1.2',
    author='Eugene Evstafev',
    author_email='ee345@cam.ac.uk',
    description='A package to convert text into embedding vectors using Hugging Face models.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/TextToVector',
    packages=find_packages(),
    install_requires=[
        'transformers>=4.0.0',
        'torch>=1.7.1'
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
