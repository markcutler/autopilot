#!/bin/bash

# move to the top level of the git repo
cd $(git rev-parse --show-toplevel)

FILES_TO_FORMAT=$(find . -regex  '.*\.\(c\|cpp\|cc\|cxx\|h\|hpp\|hxx\)')

CHANGED_FILES=$(git diff-index --cached --diff-filter=ACMR --name-only HEAD)

echo $FILES_TO_FORMAT

echo $CHANGED_FILES