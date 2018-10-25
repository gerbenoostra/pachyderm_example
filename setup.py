from setuptools import find_packages, setup

setup(
    name='hackathon_ds_to_prod',
    packages=find_packages(),
    version='0.0.1',
    description='Example project to see how model to production platforms work',
    author='BigData Republic',
    license='Apache License 2.0',
    long_description="README.md",
    python_requires='>3.5',
    install_requires=[
        "click",
        "python-dotenv>=0.5.1",
        "NumPy>=1.6.1",
        "SciPy>=0.9",
        "scikit-learn>=0.18",
        "pandas",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)
