#!/bin/sh

echo "waiting for application to be ready"
sleep 15
echo "run the test now"
python test.py 2>&1

