import os
import subprocess
import sys

from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

# Find swift compiler
result = subprocess.run(["whereis", "swiftc"], capture_output=True, text=True)
try:
    swiftc_dir = os.path.dirname(result.stdout.strip().split()[1])
    swiftc = os.path.join(swiftc_dir, "swiftc")
    if not os.path.exists(swiftc_dir):
        raise Exception()
except:
    raise AssertionError("swiftc compiler not found!")

cmd =[swiftc, "implementation.swift", "-emit-library", "-static-stdlib"]
result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    raise AssertionError(f"Failed to compile swift: {result.stderr}")

ext_modules = [
    Pybind11Extension(
        "mymodule",
        ["bindings.cpp"],
        extra_compile_args=['-std=c++11'],  # add '-g' for debug symbols
        library_dirs=['.', f'{swiftc_dir}/../../usr/lib/swift/linux'],
        libraries=['implementation'],
    ),
]

setup(
    name="mymodule",
    ext_modules=ext_modules,
)
