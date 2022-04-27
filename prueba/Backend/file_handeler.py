import pandas as pd 
import re

def fileWriter(direccion, data, columns = None):
    # esta funcion escribe todos los tipos de archivos que soporta AcelMov
    # se introduce la direccion (con la extension que queremos)
    # y la informacion (preferiblemente diccionarios o ndarrays con sus columnas)
    try:
        if columns == None:
            df = pd.DataFrame(data)
        else:
            df = pd.DataFrame(data, columns = columns)
    except:
        print("something went wrong")
        return False
    
    if re.search(r".csv$", direccion):
        df.to_csv(direccion)
        print("csv file saved")
        
    elif re.search(r".json$", direccion):
        df.to_json(direccion)
        print("json file saved")
        
    elif re.search(r".xml$", direccion):
        df.to_xml(direccion)
        print("xml file saved")
    
    else:
        print("file type error")


def fileReader(direccion):
    # esta funcion escribe todos los tipos de archivos que soporta AcelMov
    # se introduce la direccion y te devuelve un DataFrame de pandas
    # si esta funcion falla, imprime el problema y devuelve None
    try:
        # ATENCION: solo funciona en csv si los separadores son "," y el decimal es "."
        if re.search(r".csv$", direccion):
            df = pd.read_csv(direccion)
            print("csv read")
            return df
        
        elif re.search(r".json$", direccion):
            df = pd.read_json(direccion)
            print("json read")
            return df
        
        elif re.search(r".xml$", direccion):
            df = pd.read_xml(direccion)
            print("xml read")
            return df
        
        else:
            print("file type error")
            return None
            
    except FileNotFoundError:
        print("file not found")
        return None
    
    except:
        print("read error")
        return None