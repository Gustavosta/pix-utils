import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pix-utils",
    version="1.0.0",
    author="Gustavo Santana",
    author_email="sowlfie@gmail.com",
    description="A module for useful functions related to the Brazilian payment system PIX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gustavosta/pix-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


