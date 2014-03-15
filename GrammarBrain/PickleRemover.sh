#!/bin/sh
# Pickle remover

find . -name '*.p' | while read line; do
    echo "$line"
    rm "$line"
done
