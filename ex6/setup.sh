#!/usr/bin/bash

mkdir data

for I in {1..5};
do
    touch "./data/useless_file${I}"
done