# dbt documentation generator
Automatically generate dbt yml file to document tables using the informations stored in excel file.

## Excel file requirement

In order to be functional, the excel file must have this shape : 

| Table Name | Table Description | Column Name | Column description   | Col2 | col3... |
|------------|-------------------|-------------|----------------------|------|---------|
| Table1     | description table | col1        | description column 1 |      |         |
| Table1     | description table | col2        | description column 2 |      |         |
| Table1     | description table | col3        | description column 3 |      |         |

Note that the name of the sheet must also be the name of the table
i.e : **one sheet per table**

## How to use it 

a) Clone the repo, create a venv and download required packages from requirements.txt

```
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

b) run the following using your own variables : 
```
python main.py --excel <here> --table_list <here> --table_desc < here > --col_name <here> --col_desc <here>

```

with : 
- --excel : the path of the excel file used to document the project
- --table_list : list of table (or excel sheet) to parse ex : "table1" "table2"
- --table_desc : the name of the excel field used to store table description
- --col_name : the name of the excel field used to store column name
- --col_desc : the name of the excel field used to store column description

c) This will create a yml file called "result.yml" in the root of the project. 
You will then be able to copy/past its content to your dbt file in the project you are working on. 

