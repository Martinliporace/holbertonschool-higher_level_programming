#!/bin/bash
# Task 5. cURL POST parameters
curl -s -F "email=test@gmail.com" -F "subject=I will always be here for PLD" $1
