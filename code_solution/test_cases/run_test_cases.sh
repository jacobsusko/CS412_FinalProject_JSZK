# Commands to run
# in test_cases directory run:
# chmod +x run_test_cases.sh   
# to compile the shell and to run the script run
# ./run_test_cases.sh


#!/bin/bash

# Check if the filename argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Define the command to run your code
filename="$1"
code_command="python ../$filename"

# Function to compare output with expected output
check_output() {
    start_time=$(date +%s.%N)
    actual=$($code_command < "$1")
    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc)
    min_time=$(echo "$execution_time / 60.0" | bc)
    seconds=$(echo "$execution_time % 60" | bc)

    expected=$(< "$2")
    echo "Actual:" 
    echo $actual
    echo "Expected:" 
    echo $expected
    echo "Run Time:"
    echo $min_time "minutes" $seconds "seconds"

    if [ "$actual" == "$expected" ]; then
        echo "Test passed"
    else
        echo "Test Failed"
    fi
}

# Run test cases one by one
echo "Running test cases..."

if filename =="cs412_longestpath_exact.py"
then
    echo "Testing the exact solution"
else
    echo "Testing the approximate solution"
fi 

    # Test Case 1
    echo "Test case 1:"
    check_output "input1.txt" "output1.txt"
    echo ""

    # Test case 2
    echo "Test case 2:"
    check_output "input2.txt" "output2.txt"
    echo ""

    # Test case 3
    echo "Test case 3:"
    check_output "input3.txt" "output3.txt"
    echo ""

    # Test case 4
    echo "Test case 4:"
    check_output "input4.txt" "output4.txt"
    echo ""

    # Test case 5
    echo "Test case 5:"
    check_output "input5.txt" "output5.txt"
    echo ""

    # Test case 6
    echo "Test case 6:"
    check_output "input6.txt" "output6.txt"
    echo ""

    # Test case 7
    echo "Test case 7:"
    check_output "input7.txt" "output7.txt"
    echo ""

    # Test case 8
    echo "Test case 8:"
    check_output "input8.txt" "output8.txt"
    echo ""


echo "All test cases completed."
