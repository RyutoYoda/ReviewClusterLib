from setuptools import setup, find_packages

setup(
    name="ReviewClusterLib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy==1.24.0",
        "pandas==2.0.3",
        "sentence-transformers==2.2.2",
        "scikit-learn==1.3.0",
        "plotly==5.15.0",
        "snownlp==0.12.3"
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for text preprocessing, embedding generation, clustering, and sentiment analysis.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ReviewClusterLib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
