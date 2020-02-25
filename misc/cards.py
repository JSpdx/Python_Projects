
#list of suits and values for testing

suits = ['H', 'D', 'S', 'C', 'C', 'H', 'D', 'S', 'C', 'H', 'D', 'S', 'H']

values = [8, 'K', 'Q', 4, 10, 9, 'A', 7, 2, 5, 'J', 3, 8]


#dictionary used to attribute absolute values to face cards
# and calculate and compare value of face cards with number cards
dictionary = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2}

print(dictionary['A'])





#this function combines the suits and values, and returns a list of lists
def combine_suits_and_values():
    deck = []
    count = 0
    for i in values:
        deck.append([(i)])
    for i in suits:
        deck[count].append(i)
        count += 1
        
    return(deck)


#gets user input and returns requested card. calls to sort
def get_card(num):

    deck = combine_suits_and_values()
    card = []
    card.append(deck[num])
    user_input = input("\nWould you like to sort the deck? (Y/N)\n>>>")
    if user_input.upper() == 'N':
        for i in card:
            print("your card is the:\n" + ' of '.join(i))
    else:
        sort_by_value(deck)

# converts values of deck to their absolute values in the dictionary then does a bubble sort
# the bubble sort isn't working. Just outputs the same unsorted list of values.
def sort_by_value(deck):
    absolute_values = []
    length = len(absolute_values)
    for i in deck:
        absolute_values.append(dictionary[i[0]])

    for i in range(length):
        for j in range(0, length - i - 1):
            if absolute_values[j] > absolute_values[j+1]:
                absolute_values[j], absolute_values[j+1] = absolute_values[j+1], absolute_values[j]
    print(absolute_values)
    
                                                    
                                                
        
        
       
if __name__ == "__main__":
    get_card(10)



