from pathlib import Path
from setuptools import setup, find_packages

BASE_DIR = Path(__file__).parent

setup(
    name="funcbygpt",
    version="0.0.2",
    description="Describe a function and let GPT generate the code",
    long_description=(BASE_DIR / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="emresvd",
    url="https://github.com/Nabeel-Farooq/funcbygpt",
    license="MIT",

    packages=find_packages(exclude=("tests", "docs")),
    include_package_data=True,

    python_requires=">=3.8",

    install_requires=[
        "openai>=0.27,<1.0",
        "python-dotenv>=0.21",
    ],

    keywords=["gpt", "openai", "codegen", "automation"],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
    ],

    project_urls={
        "Source": "https://github.com/emresvd/funcbygpt",
        "Tracker": "https://github.com/emresvd/funcbygpt/issues",
    },
)
