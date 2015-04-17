import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages
from clamp.commands import clamp_command

setup(
    name = "coffeefilter",
    version = "0.1",
    packages = find_packages(),
    install_requires = ["clamp"],
    clamp = {
        "modules": ["coffeefilter"]
    },
    cmdclass = { "install": clamp_command }
)
