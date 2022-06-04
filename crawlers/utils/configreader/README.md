# configreader

## Usage

### Virtual environment

If `virtualenv` isn't already installed:

```sh
python3 -m pip install virtualenv
```

Create and activate a new virtual environment:

```sh
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

To deactivate the virtual environment at the end of a working session:

```sh
deactivate
```

### Unit tests

From the `crawlers/utils/configreader` directory, run the following command:

```sh
python src/test/model_tests.py
```

### Build

If `build` isn't already installed:

```sh
python3 -m pip install build
```

From the `crawlers/utils/configreader` directory, run the following command:

```sh
python3 -m build
```

If the build is successful, you should see an output similar to the one below (some line have been omitted for brevity):

```
* Creating virtualenv isolated environment...
* Installing packages in isolated environment... (setuptools)
* Getting dependencies for sdist...
[...]
* Building sdist...
[...]
* Building wheel from sdist
* Creating virtualenv isolated environment...
* Installing packages in isolated environment... (setuptools)
* Getting dependencies for wheel...
[...]
* Installing packages in isolated environment... (wheel)
* Building wheel...
[...]
Successfully built configreader-0.0.1.tar.gz and configreader-0.0.1-py3-none-any.whl
```

You'll also find the following files under `crawlers/utils/configreader/dist`:
  * `configreader-{version_number}-py3-none-any.whl`
  * `configreader-{version_number}.tar.gz`

### Adding a dependency on ConfigReader to another project

To install `configreader` in another project run:

```sh
python3 -m pip install /path/to/configreader/dist/configreader-{version_number}-py3-none-any.whl
```

For instance, to install `configreader` version `0.0.1` from the `crawlers/buyee` directory, run:

```sh
python3 -m pip install ../utils/configreader/dist/configreader-0.0.1-py3-none-any.whl
```
