import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git-utils-dmaahs2017", # Replace with your own username
    version="0.0.1",
    author="Dalton Maahs",
    author_email="maahs2017@gmail.com",
    description="Additional utils for git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmaahs2017/git-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "programming language :: python :: 3",
        "license :: osi approved :: mit license",
        "operating system :: os independent",
    ],
    python_requires='>=3.6',
)
