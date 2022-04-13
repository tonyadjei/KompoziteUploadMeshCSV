import csv

permitted_fields = ['id', 'name', 'trame', 'mass_surf', 
        'is_compat_interior_wall', 'mesh_height', 
        'mesh_width', 'mass_comb', 'roll_pallet', 'color_names']

def checkNumber(value):
    try:
        numb = float(value)
    except:
        return False
    else:
        return True

def checkColorNames(value):
    if value == '':
        return False
    else:
        return True

def checkBooleanValue(value):
    if value.lower() in ['true', 'false']:
        return True
    else:
        return False
def checkGreaterThanZero(value):

    if float(value) <= 0:
        return False
    else:
        return True

def makeInteger(value):
    return int(value)

def makeFloat(value):
    return float(value)

def checkTrame(value):
    value_lower = value.lower()
    if value_lower in ['T2 Ra1 M2 E2'.lower(), 'T2 Ra1 M4 E2'.lower(), 'T2 Ra1 M4 E3'.lower()]:
        return True
    else:
        return False


# parse csv file and store as a dictionary, return errors if there are errors otherwise return dictionary
def parse_csv_file(filename):
    errors = []
    mesh_list = []
    with open(filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        headers = next(csv_reader)
        for mesh in csv_reader:
            mesh_dict = {}
            encountered_error = False
            for i in range(10):
                if headers[i] == "\ufeffid":
                    mesh_dict.update({'id': mesh[i]})
                elif headers[i] == 'name':
                    if mesh[i] == '-':
                        mesh_dict.update({headers[i]: ''})
                    else:
                        mesh_dict.update({headers[i]: mesh[i].upper()})
                elif headers[i] == 'is_compat_interior_wall':
                    if mesh[i] == '':
                        errors.append[f'Please set a True or False value for the field: <{headers[i]}> for mesh item {csv_reader.line_num -1 }']
                        encountered_error = True
                    elif checkBooleanValue(mesh[i]):
                        if mesh[i].lower() == 'true':
                            mesh_dict.update({headers[i]: True})
                        else:
                            mesh_dict.update({headers[i]: False})
                    else:
                        errors.append[f'Please set a True or False value for the field: <{headers[i]}> for mesh item {csv_reader.line_num -1 }']
                        encountered_error = True
                elif headers[i] in ['mass_surf', 'mesh_height', 'mesh_width']:
                    if checkNumber(mesh[i]) and checkGreaterThanZero(mesh[i]):
                        mesh_dict.update({headers[i]: makeFloat(mesh[i])})
                    else:
                        errors.append(f'Please set an integer or decimal value greater than zero for the field: <{headers[i]}> for mesh item {csv_reader.line_num -1 }')
                        encountered_error = True
                elif headers[i] == 'mass_comb':
                    if mesh[i] == '':
                        mesh_dict.update({headers[i]: ''})
                    elif checkNumber(mesh[i]):
                        mesh_dict.update({headers[i]: makeFloat(mesh[i])})
                    else:
                        errors.append(f'Please set an integer or decimal value for the field <{headers[i]}> for mesh item {csv_reader.line_num -1 }')
                        encountered_error = True
                elif headers[i] == 'roll_pallet':
                    if mesh[i] == '':
                        mesh_dict.update({headers[i]: ''})
                    elif checkNumber(mesh[i]):
                        mesh_dict.update({headers[i]: makeInteger(mesh[i])})
                    else:
                        errors.append(f'Please set an integer value for the field <{headers[i]}> for mesh item {csv_reader.line_num -1 }')
                        encountered_error = True
                elif headers[i] == 'trame':
                    if checkTrame(mesh[i]):
                        if mesh[i].lower() == 'T2 Ra1 M2 E2'.lower():
                            mesh_dict.update({headers[i]: '1'})
                        if mesh[i].lower() == 'T2 Ra1 M2 E2'.lower():
                            mesh_dict.update({headers[i]: '2'})
                        else:
                            mesh_dict.update({headers[i]: '3'})
                    else:
                        value_list = ['T2 Ra1 M2 E2', 'T2 Ra1 M4 E2', 'T2 Ra1 M4 E3']
                        errors.append(f'Allowed values for field <{headers[i]}> are: {value_list} for mesh item {csv_reader.line_num -1 }')
                        encountered_error = True
                elif headers[i] == 'color_names':
                    if checkColorNames(mesh[i]):
                        mesh_dict.update({headers[i]: mesh[i]})
                    else:
                        errors.append(f'Please enter at least one color name for the field <{headers[i]}> for mesh item {csv_reader.line_num -1 }')
                        encountered_error = True
                else:
                    errors.append(f'Cannot parse field <{headers[i]}>. Permitted fields are : {permitted_fields}')
                    encountered_error = True
            if not encountered_error:
                mesh_list.append(mesh_dict)
    return mesh_list, errors