# csv_filtered_output_python
To output csv in terminal filtered by field values and output specific columns
This is an attempt to view the CSV files in terminal by passing the necessary filter conditions and the output column numbers
The first argument is the CSV filename
Second argument is the filter conditions separated by commas (no space characters)
Supported Operators are

<, >, =, # ============> less than, greater than, equal to, not equal to
   
[, ], ~, ! ============> text length operators : len() greater than, less than, equal to, not equal to
   
*, ^, $, =, # =========> text operators: contains, startswith, endswith, equals to, not equals to
