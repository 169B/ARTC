"""
ARTC-LITE - Lightweight IoT Tensor Encoding
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="artc-lite",
    version="1.0.0",
    author="169B",
    author_email="your.email@example.com",
    description="Lightweight IoT Tensor Encoding for sensor data compression",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/169B/ARTC",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
    keywords="compression iot sensor data regression lossy embedded arduino",
    project_urls={
        "Bug Reports": "https://github.com/169B/ARTC/issues",
        "Source": "https://github.com/169B/ARTC",
    },
)
