from setuptools import setup, find_packages

setup(
    name="orthophonic",  
    version="0.1.0",  
    author="Vincent Choqueuse",
    author_email="choqueuse@enib.fr",
    description="A research-based music composition framework using mathematical principles",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="",
    license="MIT", 
    packages=find_packages(),  # Automatically discover all packages in the project
    install_requires=[
        "numpy",       # Example dependencies, add more as needed
        "scipy",
        "matplotlib",
        "python-osc",
        "pylive"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Signal Processing",
        "Topic :: Multimedia :: Sound/Audio",
    ],
    python_requires=">=3.6",  # Specify minimum Python version
    include_package_data=True,  # Ensure package data (if any) is included
)
