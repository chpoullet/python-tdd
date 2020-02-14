from brioche import *

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
