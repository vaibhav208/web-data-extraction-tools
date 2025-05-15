#!/bin/bash

# Download and parse NAV data
curl -s https://www.amfiindia.com/spages/NAVAll.txt | \
awk -F ';' 'NF > 1 && $1 ~ /^[0-9]+$/ { print $3 "\t" $5 }' > nav_data.tsv

echo "Saved Scheme Name and NAV to nav_data.tsv"
