 #  this is the module that contains utility functions 

def clean_object_none_values(object_to_clean:dict):
        return {key: value for key, value in object_to_clean.items() if value is not None}

def combine_two_objects(obj1, object2):
    combined_objects = dict()
    combined_objects.update(obj1)
    combined_objects.update(object2)
    return combined_objects
    