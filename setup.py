import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locconverter",
    version="0.0.1",
    author="EnisBaranDurmus",
    author_email="enisbaran.durmus@gmail.com",
    description="Location converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EnisBaranDurmus/LongLatPathing",
    project_urls={
        "Bug Tracker": "https://github.com/EnisBaranDurmus/LongLatPathing/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)