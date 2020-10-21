from coderunner.coderunner import code
import os

source_code = "./pyt.py"
language = "Python3"
expected_output = "11"
standard_input = "11"

# use this if you have a standard input to Program
r = code(source_code, language, expected_output, standard_input)