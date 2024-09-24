from setuptools import setup, find_packages

setup(
    name="facesinthings",  # Package name
    version="0.1.0",  # Initial version
    description="A PyTorch dataset for the FacesInThings dataset",
    author="Mark Hamilton, Simon Stent, Vasha DuTell, Anne Harrington, Jennifer Corbett, Ruth Rosenholtz, William T. Freeman",  # Your name as the author
    author_email="markth@mit.edu",  # Replace with your email
    url="https://github.com/mhamilton723/FacesInThings",  # GitHub or project URL if applicable
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),  # Automatically finds the package directories
    install_requires=[  # External dependencies
        "torch>=1.7",  # Requires PyTorch, version 1.7 or higher
        "torchvision>=0.8",  # Requires torchvision, version 0.8 or higher
        "pandas>=1.1",  # Requires pandas for CSV handling
        "requests>=2.24",  # Requests library to download the dataset
        "Pillow>=8.0",  # Pillow for image processing
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",
    ],
    include_package_data=True,  # Include non-Python files like data, CSVs, etc.
)
