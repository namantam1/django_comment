import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_comment-namantam1", # Replace with your own username
    version="0.0.1",
    author="Naman Tamrakar",
    author_email="namantam1@gmail.com",
    description="A django app which help in implementing comments in your posts model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/namantam1/django_comment",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)