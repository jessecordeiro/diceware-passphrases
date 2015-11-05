# Jesse Cordeiro
# November 04, 2015
# Diceware is a trademark of A G Reinhold

import random
required_number_count = 5
lower_bound = 1
upper_bound = 6

def main():
    """
    Main function responsible for user input and output
    """
    word_count = int(input('How many words would you like your passphrase to contain: '))
    
    passphrase = passphrase_generator(number_generator(word_count))
    
    print("Your passphrase is %r, with a word count of %r." % (passphrase, word_count))

def number_generator(word_count):
    """ (int) -> list of int
    
    Precondition: The parameter word_count is assumed to be >= 1
    """
    
    number_sequence = ''
    generated_number_count = 0
    generated_number_list = []
    
    while len(generated_number_list) < word_count:
        
        while generated_number_count < required_number_count:
            number = random.randint(lower_bound, upper_bound)
            number_sequence += str(number)
            generated_number_count += 1
        
        generated_number_list.append(number_sequence)
        generated_number_count = 0
        number_sequence = ''

    return generated_number_list

    
def passphrase_generator(generated_number_list):
    """ (list of int) -> str
    
    Precondition: The parameter generated_number_list refers to a list of int
    with one or more elements.
    """
    
    file = open('diceware.wordlist.asc')
    word_list = []
    passphrase_elements = []
    passphrase = ""

    for element in generated_number_list:
        
        file = open('diceware.wordlist.asc')
        for line in file:
            
            if element in line:
                word_list.extend(line.split())
    
    passphrase_elements.extend(word_list[1::2]) 
    
    # concatenates elements from list to string to form the passphrase    
    passphrase = ''.join(passphrase_elements)
    
    return passphrase

main()
