# ConfigReader

## Usage

##### Virtual environment

If virtualenv isn't already installed:

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

##### Unit tests

From the `crawlers/utils/config-reader` directory, run the following command:

```sh
python src/test/model_tests.py
```
