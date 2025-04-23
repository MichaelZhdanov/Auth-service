#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Color codes for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Find all test_*.py files in the script directory
TEST_FILES=($(find "$SCRIPT_DIR" -maxdepth 1 -name 'test_*.py' | sort))

if [ ${#TEST_FILES[@]} -eq 0 ]; then
    echo -e "${RED}No test files found in $SCRIPT_DIR${NC}"
    exit 1
fi

echo -e "${GREEN}Found ${#TEST_FILES[@]} test files to execute:${NC}"
printf '  %s\n' "${TEST_FILES[@]}"
echo ""

# Execute each test file
FAILED_TESTS=()
for test_file in "${TEST_FILES[@]}"; do
    echo -e "${GREEN}=== Running $(basename "$test_file") ===${NC}"
    
    # Execute the test script and capture its exit code
    python3 "$test_file"
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -ne 0 ]; then
        echo -e "${RED}✗ Test failed: $(basename "$test_file")${NC}"
        FAILED_TESTS+=("$test_file")
    else
        echo -e "${GREEN}✓ Test passed: $(basename "$test_file")${NC}"
    fi
    echo ""
done

# Print summary
if [ ${#FAILED_TESTS[@]} -eq 0 ]; then
    echo -e "${GREEN}All tests passed successfully!${NC}"
    exit 0
else
    echo -e "${RED}${#FAILED_TESTS[@]} test(s) failed:${NC}"
    printf '  %s\n' "${FAILED_TESTS[@]}"
    exit 1
fi