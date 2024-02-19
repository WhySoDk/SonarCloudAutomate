from setuptools import Extension, setup

setup(
    name="extension.dist",
    version="0.1",
    description="A testing distribution \N{SNOWMAN}",
    ext_modules=[
        Extension(name="extension", sources=["extension.c"], py_limited_api=True)
    ],
)
