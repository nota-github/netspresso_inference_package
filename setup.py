from pathlib import Path
from setuptools import setup, find_packages

install_requires = Path("requirements.txt").read_text().split('\n')

setup(
    name="netspresso_inference_package",
    version="0.1.1",
    author="NetsPresso",
    author_email="netspresso@nota.ai",
    description="Inference module.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nota-github/netspresso_inference_package",
    install_requires=install_requires,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)