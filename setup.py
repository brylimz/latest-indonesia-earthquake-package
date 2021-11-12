import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="latestearthquake-indonesia",
    version="0.1",
    author="Bryan Y. Limz",
    author_email="superuser@brylimz.com",
    description="This package will get the latest earthquake from Indonesia | BMKG | Meteorological, Climatological, and Geophysical Agency",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brylimz/latest-indonesia-earthquake",
    project_urls={
        "Website": "https://brylimz.com",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)