#!/bin/bash

# Define your test cases here
test_case_1_input="input1.txt"
test_case_1_output="output1.txt"

# Add more test cases as needed

# Define the command to run your code
code_command="python ../exact_solution.py"

# Function to compare output with expected output
check_output() {
    actual=$(echo "$1" | $code_command)
    expected=$(< "$2")

    if [ "$actual" == "$expected" ]; then
        echo "Test passed"
    else
        echo "Test Failed"
    fi
}

# Run test cases one by one
echo "Running test cases..."

# Test case 1
echo "Test case 1:"
check_output "$test_case_1_input" "$test_case_1_output"

# # Test case 2
# echo "Test case 2:"
# $code_command < $test_case_2

# Add more test cases as needed

echo "All test cases completed."
