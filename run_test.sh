#!/bin/bash

declare chapter=$1

python3 -m unittest "./$chapter/test*"