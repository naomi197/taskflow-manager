"""Setup configuration for TaskFlow"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="taskflow-manager",
    version="1.0.0",
    author="TaskFlow Team",
    description="Professional task and project management library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/naomi197/taskflow-manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8+",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.8",
)
