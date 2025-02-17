# Swift-Python Interop Example

### Install swiftc
Get the latest version of `swiftc` from 
https://www.swift.org/install/linux/ubuntu/24_04/#latest.
This repository was tested with version 6.0.3.

### Create a Python virtual environment
Run the following command.
```bash
python3 -m venv venv
```
Source the environment.
```bash
source venv/bin/activate
```

### Build the Python binding
Run the following command.
```bash
pip install -e .
```

### Validate the build
Run the following command.
```bash
python3 validate.py
```
