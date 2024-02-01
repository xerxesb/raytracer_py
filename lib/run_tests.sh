#!/bin/bash

# Run all tests in the current directory
# Usage: ./run_tests.sh

FILES=$(find *.py -type f -exec echo '{}' \;)

for f in $FILES
do
  echo -----------------------
  echo $f
  python3 "$f"
  if [ $? -eq 0 ]; then
    echo "OK"
  else
    echo "FAIL"
    break
  fi
  echo ""
done

echo -----------------------
echo "Test Files Passed: $(echo $FILES | wc -w)"