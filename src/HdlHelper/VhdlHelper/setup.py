import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VhdlHelper",
    version="1.0.0",
    author="jfd",
    author_email="jfd@hdlhelper.com",
    description="Vhdl Code Generator In HdlHelper Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages()
)