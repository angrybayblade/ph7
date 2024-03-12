"""Setup module for ph7"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")
setup(
    name="ph7",
    version="0.1.0-rc3",
    description="Python native HTML rendering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/angrybayblade/ph7",
    author="Viraj Patel",
    author_email="vptl185@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",  # 3-Alpha, 4-Beta, 5-Production/Stable
        "Intended Audience :: Developers",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="html, css, js, templates, django",
    packages=find_packages(include=["ph7*"]),
    python_requires=">=3.9, <4",
    install_requires=[],
    package_data={
        "ph7": [
            "py.typed",
        ],
    },
    project_urls={
        "Documentation": "http://ph7.angrybayblade.me",
        "Changelog": "https://github.com/angrybayblade/ph7/blob/main/docs/CHANGELOG",
        "Issue Tracker": "https://github.com/angrybayblade/ph7/issues",
    },
)
