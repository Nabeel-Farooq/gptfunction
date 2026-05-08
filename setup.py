from pathlib import Path
from setuptools import setup, find_packages

BASE_DIR = Path(__file__).resolve().parent

README = (BASE_DIR / "README.md").read_text(encoding="utf-8")

setup(
    name="funcbygpt",
    version="0.1.0",
    description="Generate Python functions from natural language using OpenAI",
    long_description=README,
    long_description_content_type="text/markdown",

    author="Nabeel Farooq",
    url="https://github.com/Nabeel-Farooq/funcbygpt",

    license="MIT",

    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
            "docs",
            "examples",
        ]
    ),

    include_package_data=True,

    python_requires=">=3.8",

    install_requires=[
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
    ],

    extras_require={
        "dev": [
            "black",
            "flake8",
            "pytest",
            "build",
            "twine",
        ]
    },

    keywords=[
        "openai",
        "gpt",
        "ai",
        "code-generation",
        "automation",
        "python",
    ],

    project_urls={
        "Homepage": "https://github.com/Nabeel-Farooq/funcbygpt",
        "Source": "https://github.com/Nabeel-Farooq/funcbygpt",
        "Issues": "https://github.com/Nabeel-Farooq/funcbygpt/issues",
    },

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
