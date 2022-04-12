from setuptools import setup

setup(
    install_requires=[

    ],
    extras_require={
        "vulkan": [
            "cffi",
        ],
    },
    tests_require=[
        "tox",
    ],
)
