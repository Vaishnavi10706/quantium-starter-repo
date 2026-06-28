#!/bin/bash

# Activate virtual environment
source ./venv/Scripts/activate

# Make sure project root is in Python path
export PYTHONPATH=.

# Run tests
python -m pytest

# Return pytest exit code
exit $?