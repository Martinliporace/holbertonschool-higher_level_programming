#!/bin/bash
# Task 6. Only status code

curl -o /dev/null -s -w "%{http_code}" $1
