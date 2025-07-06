import json
import pickle
import numpy as np

__locations = None
__data__columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data__columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data__columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data__columns
    global __locations
    global __model

    with open("artifacts/columns.json",'r') as f:
        data = json.load(f)
        print("loaded raw JSON data")
        __data__columns = data["data_columns"]
        print("extracted data columns:",__data__columns)
        __locations = __data__columns[3:]

    with open("artifacts/bangalore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2))
    print(get_estimated_price('Kalhalli',1000, 2, 2))
    print(get_estimated_price('Ejipura',1000, 2, 2))
    print("Loaded locations from JSON:", __locations[:5])
