def rename_informations_columns(list_of_infos : list, column_name : str, column_description : str)-> list: 
    """
    Rename the fields designed for the name/description of a column to be used in jinja template. 

    Args:
        list_of_infos (list): the list of columns described in excel file 
        column_name (str): name of the excel column used to describe the column name
        column_description (str): name of the excel column used to describe the column description

    Returns:
        list: list for informations with renamed fields 
        
        example : 
        input = [
            {
                "Physical Column Name" : "col-name",
                "Column Definition" : "col-description",   
            }
        ]    
        output = [
            {
                "name" : "col-name",
                "description" : "col-descriptio",   
            }
        ]
    
    """
    res = list_of_infos.copy( )
    
    
    for infos in res : 
        infos['name'] = infos.pop(column_name)
        infos['description'] = infos.pop(column_description)

    return res 