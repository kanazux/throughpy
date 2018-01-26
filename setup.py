from setuptools import setup, find_packages

setup(
    name="throughpy"
    version="0.1",
    license="BSD2CLAUSE",
    packages=find_packages(),
    keywords="net python iperf3",
    url="https://github.com/kanazux/throughpy",
    author='Silvio AS a.k.a kanazuchi',
    author_email='contato@kanazuchi.com',
    description="A script to test throughput of the main interface with a formatted output using iperf3.",
)
