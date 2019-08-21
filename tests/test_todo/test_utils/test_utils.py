
from todocli.todo.utils.utils import clean_object_none_values, combine_two_objects
class TestUtils(object):

    def test_CleanObjectNoneValues(self):
        obj_with_none_values = dict(first_name='John',age=None,last_name=None)
        cleaned_obj = clean_object_none_values(obj_with_none_values)
        
        assert 'age' not in cleaned_obj
        assert 'last_name' not in cleaned_obj
        assert 'first_name' in cleaned_obj

    def test_CombineTwoObjects(self):
        obj1 = dict(first_name='John', age=None, last_name=None)
        obj2 = dict(first_name=None, age=54, last_name='Smith')

        combined_obj = combine_two_objects(obj1, obj2)

        assert 'age' in combined_obj
        assert combined_obj['age'] == 54

        assert 'last_name' in combined_obj
        assert combined_obj['last_name'] == 'Smith'

        assert 'first_name' in combined_obj
        assert combined_obj['first_name'] == None