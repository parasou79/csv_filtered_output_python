# csv_filtered_output_python
To output csv in terminal filtered by field values and output specific columns
This is an attempt to view the CSV files in terminal by passing the necessary filter conditions and the output column numbers
The first argument is the CSV filename
Second argument is the filter conditions separated by commas (no space characters)
Supported Operators are

<, >, =, # ============> less than, greater than, equal to, not equal to
   
[, ], ~, ! ============> text length operators : len() greater than, less than, equal to, not equal to
   
*, ^, $, =, # =========> text operators: contains, startswith, endswith, equals to, not equals to

Syntax:
python u1.py CSV_FILENAME FILTER_CONDITION_ON_COLUMN_NUMBERS OUTPUT_COLUMN_NUMBERS
the filters are comma separated and considered as AND conditionals
the OUTPUT columns are also comma separated

Examples:
Lets say we have employees file and we want to print some text in terminal
Column-0 contains Employee-Code and Column-7 contains Employee-Name, Column-4 contains Employee-DOB

python u1.py skh1.csv "7=PARASOU" 0,7 -- prints empcode & empname whose name equals PARASOU
python u1.py skh1.csv "7$MAN" 7 -- prints empname whose name ends with MAN
python u1.py skh1.csv "0<15000," 7 -- prints empname whose name ends with MAN
python u1.py skh1.csv "7^JL" 0,1,2,3,4,7 -- prints columns 0 to 7 whose name begins with JL
 

