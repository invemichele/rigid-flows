from setuptools import find_packages, setup

setup(
    name="rigid_flows",
    version="0.1.0",
    url="https://github.com/noegroup/rigid-flows.git",
    author="Jonas Köhler",
    author_email="jonas.koehler.ks@gmail.com",
    description="flows for rigid bodies",
    python_requires=">3.10",
    packages=find_packages(),
    install_requires=[
        "flox",
        "openmm",
        "mlparams",
        "tensorflow_probability",
        "mdtraj",
        "genice2",
        "pymbar",
        "tensorflow",
        "GitPython",
    ]
)
