from jinja2 import Environment, FileSystemLoader
import argparse
import pandas as pd
import utils

def main() : 
     
    # Define input arguments
    parser = argparse.ArgumentParser(description='Add arguments to create yml file')
    parser.add_argument('--excel',required=True, type=str, nargs='?',help='the excel file path')
    parser.add_argument('--table_list',required=True, type=str, nargs='+',help='list of table to document')
    parser.add_argument('--table_desc',required=True, type=str, nargs='?',help='Name of the field used to store table description')
    parser.add_argument('--col_name',required=True, type=str, nargs='?',help='Name of the field used to store column name')
    parser.add_argument('--col_desc',required=True, type=str, nargs='?',help='Name of the field used to store column description')

    # Parse and get input arguments
    args = parser.parse_args()
    excel_path = args.excel
    table_list = args.table_list
    table_description_field = args.table_desc
    column_name_field = args.col_name
    column_description_field = args.col_desc

    tables_informations = [] 
    
    # Loop over tables/Excel sheets
    for table in table_list : 
        
        # Read excel sheet 
        df = pd.read_excel(excel_path,table)
        
        # delete new line
        df = df.replace(r'\n',' ', regex=True) 

        # Get table definition
        table_description = list(df[table_description_field])[0]
        # select only columns informations
        columns_infos =  df[[column_name_field,column_description_field ]].to_dict('records')
        # rename fields
        renamed_colums_infos = utils.rename_informations_columns(list_of_infos=columns_infos,
                                                                column_name= column_name_field,
                                                                column_description= column_description_field)

        tables_informations.append( {
            "table_name" : table, 
            "table_description" : table_description,
            "columns_infos" : renamed_colums_infos 
        })
        
    # get template file
    env = Environment(loader = FileSystemLoader('./template'),   
                    trim_blocks=True, lstrip_blocks=True)

    template = env.get_template('src.j2')


    f = open('result.yml','a')

    # Append generated text from template
    f.write(
        
        template.render(
            tables_informations = tables_informations
            )
)

if __name__ == '__main__':
  main()