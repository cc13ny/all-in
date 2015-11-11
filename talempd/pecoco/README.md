# Project Description

This is a brief document to illustrate this small project. 

The project is used to parse entries of personal information and write them as the formatted & valid JSON into an output file.

# File Organization

The structure of the file & folder organization is as follows.

+ README.md: Give you a brief introduction what the project does, what files are included, and how to run it.
+ src: Store the source codes of this project.
  + entry2json.py: the only source code for implementing all functions of this project.
  + test_ent2json.py: used to test 'entry2json.py'
  + test: it concludes 3 kinds of files: Input files with suffix '.in'/ Output files with suffix '.out' generated by 'entry2json.py' / Truth files with suffix '.truth' for comparison with output files
+ doc: documents for this project
  + entry2json.html: the API manual for entry2json.py
  + test_ent2json.html:  the API manual for test_entry2json.py
+ data: store the input file we'd like to turn into valid JSON files where the output file are stored in the same directory of input files.

# Run
Firstly, you need to enter the directory of the src code. Otherwise, you should run 'python <absoult_path_src>' where <absoult_path_src> is the absoulte path of the src code.
+ Test Code
  > python test_ent2json.py

  Then the test results will be showned on the console.

+ Parse input files into JSON output files (on command line)
  > python entry2json.py

  > Please input the absoulte path of the input file
  
  > ../data/data.in

  Then you can find the output file 'data.out' in the same directory of 'data.in'.