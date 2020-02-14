
# Brioche Factory TDD


# **make_bread**
#
# inputs:
# - water
# - flour
# - eggs
#
# outputs:
# - dough
#
#
# **bake**
#
#
# inputs:
# - dough
#
# outputs:
# - brioche

def make_bread(arg1, arg2, arg3):
    if arg1 == 'water' and arg2 == 'flour' and arg3 == 'eggs':
        return 'dough'
    else:
        return 'not dough'

def bake(arg1):
    if arg1 == 'dough':
        return 'brioche'
    else:
        return 'not brioche'

def run_factory(arg1, arg2, arg3):
    result_dough = make_bread(arg1, arg2, arg3)
    result_bake = bake(result_dough)
    return result_bake

# tests for make bread
print('Testing make_dough() with water, flour and eggs. Expected dough.')
print(make_bread('water', 'flour', 'eggs') == 'dough')

print('Testing make_dough() with water, cement and gravel. Expected not dough.')
print(make_bread('water', 'cement', 'gravel') == 'not dough')

# test for bake
print('Testing bake() with dough. Expected brioche.')
print(bake('dough') == 'brioche')

print('Testing bake() with concrete. Expected not brioche.')
print(bake('concrete') == 'not brioche')


## simple integration test
print('test run_factory() with water flour and eggs. Expected brioche')
print(run_factory('water', 'flour', 'eggs') == 'brioche')

print('test run_factory() with water, cement and gravel. Expected not dough.')
print(run_factory('water', 'cement', 'gravel') == 'not brioche')



