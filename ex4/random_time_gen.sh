#!/usr/bin/bash

for FILE in $(ls);
do
    RNG_DATE=$(date -d @$(shuf -i "0-$(date +%s)" -n 1) +%Y%m%d%H%M.%S)
    touch -mt ${RNG_DATE} ${FILE}
done