import random


print("hello I am your lotto number generator")
go = input("feeling lucky?? type 'start' to generate your lotto numbers")
while go == 'start' or go == 'START':
            range_ = list(range(0, 50)) # establish value range
            value = random.sample(range_, k=6)
            print(value)
            rerun = input("go again? type 'no' to stop, type any key to continue:")
            if rerun == "no":
                print("thanks, goodbye")
                break
            else:
                pass
else:
    print("sorry, didn't catch that, type 'start' to generate your lotto numbers")