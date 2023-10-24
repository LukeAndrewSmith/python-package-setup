# python-package-setup

- Just a minimal package, playing with https://github.com/pypa/sampleproject/blob/main/pyproject.toml
- Another nice site about packages: https://til.simonwillison.net/python/pyproject
- Setup tools automatic discovery: https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#automatic-discovery

##  Setup
1. Install miniconda: https://docs.conda.io/projects/miniconda/en/latest/
2. Create your env: `conda create -n a_package`
3. Choose your python version: `conda install python=3.12.0`
4. Add you're dependencies to `dependencies` in `pyproject.toml`
5. Install the package in editable mode for development: `python -m pip install -e .`
6. Run tests with `python -m unittest`

## Using the package
- You can `pip install <path>/a_package` from another env to use the package

## Documenting
- Make sure to write a nice `README.txt` explaining what the package does and how to use it

## Sharing
- If you'd like to share you exact environment: `conda env export > environment.yaml`
    - This can be shared and installed with: `conda env create -f environment.yml`