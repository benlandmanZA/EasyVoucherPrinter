# EasyVoucherPrinter
A simple file formatter exercise :)

# Features

- Takes in a file with the specified header format to allow some customisation of output.
- Validates the data to ensure there are no mistakes in the file header, or data.
- FileHandler can be imported to another module.
- The following formatting data in the header: 'columns', 'column_width', 'column_spacing', 'row_spacing' can be changed in your input file and will reflect the changes in the output file.

# Demo Program Usage

1. Clone the repository using `git clone https://github.com/benlandmanZA/EasyVoucherPrinter.git`
2. Run VoucherDemoProgram.py in your terminal/IDE. 
3. You will be prompted to enter the desired input file. Enter only the name of the file, please exclude the extension. You can use the file named 'demo'
4. If the file meets the data validation requirements it will output a file in the same directory with the result('demo_result')!


# Test Program Usage

1. Assuming you have already cloned the repo, navigate to the child folder labelled testing.
2. Run VoucherTestingProgram.py in your respective terminal/IDE.
3. The output of the test cases will be outputted in the terminal.

# Limitations

- I have saved all header data in a customisable and reuseable format, however I only coded features allowing you to change the following formatting data:
	1. columns:5
	2. column_width:25
	3. column_spacing:5
	4. row_spacing
- The algorithm I used in my format() function, is around O(n^3) which is not optimal for very large data sets, there is a possibility for it to be optimised by removing some loops and using numpy array formatting.
- The files being accessed must be in the same directory as the program.