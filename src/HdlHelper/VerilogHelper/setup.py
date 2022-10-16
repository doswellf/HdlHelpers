import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VerilogHelper",
    version="1.0.0",
    author="jfd",
    author_email="jfd@hdlhelper.com",
    description="Verilog Generator In HdlHelper Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages()
)