#!/bin/bash

# Store previous directory
OLD_DIR=`pwd`

# Get the current dir and switch to it
DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "${DIR}"

# Run the tests
python3 -m unittest -v test.utilities.test_print_formatter \
                       test.utilities.test_print_manager \
                       test.test_command_manager \
                       test.commands.test_help \
                       test.commands.test_version

# Restore the old directory
cd "${OLD_DIR}"

exit 0
