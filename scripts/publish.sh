#!/bin/bash
# Exit immediately if a command exits with a non-zero status.
set -e

echo "Starting publication process..."

# Use virtual environment python if it exists
if [ -d ".venv" ]; then
  PYTHON=".venv/bin/python"
else
  PYTHON="python3"
fi

# Run the interactive compiler
$PYTHON scripts/compiler.py

# Rebuild the static site indexes
$PYTHON scripts/build.py

echo "Publishing complete!"
