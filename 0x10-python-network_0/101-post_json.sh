#!/bin/bash
# Task 7. cURL a JSON file

curl -X POST -H "Content-Type: application/json" -d @$2 $1
