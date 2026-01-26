"""
Setup script for the Cognitive Fortress Framework: Sovereign Edition.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cognitive-fortress-framework",
    version="1.0.0",
    author="Cognitive Fortress Team",
    author_email="info@cognitivefortress.example.com",
    description="A comprehensive security framework designed to protect cognitive processes and mental sovereignty against various forms of manipulation and influence.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/cognitive-fortress-framework",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Core dependencies would be listed here
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
        ],
        "ml": [
            # Machine learning dependencies would go here if needed
        ]
    },
    entry_points={
        "console_scripts": [
            "cff=cff.main:main",  # Example entry point
        ],
    },
)