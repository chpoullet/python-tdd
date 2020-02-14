from brioche import *


print(__name__) # identifies where it is being called from
                # if it is being called directly, therefore not imported, __name__ will become __main__
                # if imported it will have the name of where it's coming from
while True:

    if __name__ == '__main__':  # use case would be for little demos, starting a game, running tests
        print("You're in the main file")
        user_input = input('Select 1 to Test or 2 to make some bread!')
        if user_input == '1':
            from factory_tests import *
        elif user_input == '2':
            print('Welcome to the factory')
            arg1 = input('Whats your first ingredient')
            arg2 = input('Whats your second ingredient')
            arg3 = input('Whats your third ingredient')
            result = run_factory(arg1, arg2, arg3)
            print(result)
        elif user_input == 'break':
            break
        else:
            print("Sorry, not an option")