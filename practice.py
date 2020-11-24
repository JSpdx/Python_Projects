
print("test")

num_list = [1,34,5,32,5,765]
target = 5

def binary_search(num_list, target):
    
    max = len(num_list) - 1
    min = 0
    guess = 0
    while guess != target:
        guess = max / 2 
        if guess > min:
            min = guess
        if guess < max:
            max = guess
    print(guess)
    return guess

print(binary_search(num_list, target))