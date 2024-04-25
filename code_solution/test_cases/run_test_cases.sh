# Commands to run
# in test_cases directory run:
# chmod +x run_test_cases.sh   
# to compile the shell and to run the script run
# ./run_test_cases.sh


#!/bin/bash

# Define your test cases here
test_case_1_input="input2.txt"
test_case_1_output="output2.txt"

# Add more test cases as needed

# Define the command to run your code
code_command="python ../cs412_longestpath_exact.py"

# Function to compare output with expected output
check_output() {
    actual=$($code_command < "$1")
    expected=$(< "$2")
    echo "Actual:" 
    echo $actual
    echo "Expected:" 
    echo $expected

    if [ "$actual" == "$expected" ]; then
        echo "Test passed"
    else
        echo "Test Failed"
    fi
}

# Run test cases one by one
echo "Running test cases..."

# Test Case 1
echo "Test case 1:"
check_output "input1.txt" "output1.txt"
echo ""


# Test case 2
echo "Test case 2:"
check_output "input2.txt" "output2.txt"
echo ""

# Add more test cases as needed

echo "All test cases completed."
