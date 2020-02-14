#  Brioche Factory TDD

## Unit Test
Tests singular and unitary pieces of code

## Integration test
Tests code from end to end

## TDD - Test Driven Development
It does what it says.
You first write a test, then you code.

Code the minimum amount to pass the test.


## Basics of a test
Known inputs, and known outputs.
All you do is an assertion.

Then you have testing frameworks that help you do this.

## Our Factory known inputs and outputs

## make_bread

Make a function that takes in two arguments.
It should make 'dough' when given water, flour and eggs.

inputs:
- water
- flour
- eggs

outputs:
- dough


## bake


inputs:
- dough

outputs:
- brioche

## Integration test

### run_factory
As a user, I want to be able to run a factory function. Give it flour, water and
eggs. I want to receive brioche.


### Usage/Documentation

make_bread(arg1, arg2, arg3)

bake(arg1)

run_factory(arg1, arg2, arg3)


## _name_ and _main_ in Python


## breakpoint()
useful for figuring out which block of code
is broken, can test variables etc.