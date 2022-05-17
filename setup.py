from setuptools import setup, find_packages

setup(
    name="geo_transformer",
    version="1.0.0",
    description="Test challenge for Stuart",
    url="https://github.com/StuartHiring/python-test-sebastienhoarau",
    author="Sebastien Hoarau",
    author_email="sebastien.h.data.eng@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(),
    python_requires=">=3.9, <3.10",
    package_data={
        "geo_transformer": [
            "data/test_points.txt.gz",
        ],
    },
)
