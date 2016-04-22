#!/usr/bin/python

import subprocess
import humanhash

# get the last commit SHA and print it after humanizing it
# https://github.com/zacharyvoase/humanhash
print humanhash.humanize(
    subprocess.check_output(
        ['git','rev-parse','HEAD']))