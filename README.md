# Party Invitation Tool

This is a program that parses a file (by default customer.txt), calculates the customers to be invited based on their distance to the company's office (by default 100), and prints the invites, one per line, to a file (by default output.txt).

# Installation

This program was developed using Python 3.7.3, but uses no features specific to that version and should be able to run on any Python 3 installation.
It also requires pytest to be installed for unit testing.

To install pytest, use the following command:
```
pip3 install pytest
```

# Commands
```
python3 main.py [distance] [input_file] [output_file]
```
Executes the program. This program produces no output to stdout, only writing the results to file.

```
pytest
```
Runs all unit tests 
