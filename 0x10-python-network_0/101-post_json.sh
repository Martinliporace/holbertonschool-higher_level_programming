#!/bin/bash
# Task 7. cURL a JSON file
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
