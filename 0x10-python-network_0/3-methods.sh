#!/bin/bash
# Task 3. cURL only methods


curl -Is OPTIONS $1 | grep 'Allow'| cut -d " " -f 2-