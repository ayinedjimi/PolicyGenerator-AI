"""Setup for PolicyGenerator-AI

Author: Ayi NEDJIMI
"""

from setuptools import setup, find_packages

setup(
    name="policygenerator-ai",
    version="1.0.0",
    author="Ayi NEDJIMI",
    author_email="contact@ayinedjimi-consultants.fr",
    description="AI-Powered Security Policy Generator",
    url="https://github.com/ayinedjimi/PolicyGenerator-AI",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=["openai>=1.3.0", "python-docx>=1.1.0", "reportlab>=4.0.7"],
)
