from setuptools import setup, find_packages

setup(
    name='GitWise',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List of dependencies, e.g., 'requests', 'GitPython', etc.
    ],
    entry_points={
        'console_scripts': [
            'gitwise=gitwise:main',
        ],
    },
    # Metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='An AI-enhanced Git assistant tool.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/gitwise',
    project_urls={
        'Bug Tracker': 'https://github.com/yourusername/gitwise/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)