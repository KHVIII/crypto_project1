import random

alphabet = ' abcdefghijklmnopqrstuvwxyz'
max_key_length = 25
'''Helper function'''
def get_dictionaries():
    d_one = open('dictionary_1.txt', 'r').readlines()
    d_two = open('dictionary_2.txt', 'r').readlines()
    
    for index,text in enumerate(d_one):
        d_one[index] = text.strip()
    
    for index,text in enumerate(d_two):
        d_two[index] = text.strip()
    
    return d_one, d_two
'''
def find_character_indexes(text):
    indexes = {}
    for char in alphabet:
       indexes[char] = [idx for idx,c in enumerate(text) if char == c]
    return indexes
'''
'''Calculate the shifts between two equal length strings'''
def calculate_shifts(string_one, string_two):
    all_differences = []
    for i in range(len(string_one)):
        difference = calc_shift(string_one[i], string_two[i])
        all_differences.append(difference)
    return all_differences

'''Calculate the amount x must be shifted by to reach y'''
def calc_shift(x,y):
    diff = alphabet.index(x) - alphabet.index(y)
    if diff < 0:
        diff = 27+diff
    return diff
     
'''Given a list of indexes, return the characters at those indexes'''
def get_chars_at_indexes(indexes, text):
    return [text[i] for i in indexes]

'''Get every i_th character e.g. Get every 5th character
'''
def get_all_i_th_chars(text, i, start=0):
    ret = ''
    x = start
    while x < len(text):
        ret = ret+text[x]
        x+=i 
    return ret

'''
def find_same_shifts(plain_text, cipher_text):
    #cipher_indexes = find_character_indexes(cipher_text)
    pt_indexes = find_character_indexes(plain_text)
    same_shifts = []
    for char, indexes in pt_indexes.items():
        for i in range(len(indexes)):
            for j in range(i+1, len(indexes)):
                if cipher_text[indexes[i]] == cipher_text[indexes[j]]:
                    same_shifts.append((indexes[j]-indexes[i])%27)
    print(same_shifts)
'''

def brute_key_len(cipher_text, plain_text):
    possible_lengths = []
    for key_len in range(1, max_key_length):
        cipher_chars = get_all_i_th_chars(cipher_text, key_len)
        plain_chars = get_all_i_th_chars(plain_text, key_len)
        
        shifts = calculate_shifts(cipher_chars, plain_chars)
        if len(list(set(shifts))) == 1:
            #print(f'Possible key length {shifts[0]}')
            possible_lengths.append(key_len)
    
    return possible_lengths

def find_pt(cipher_text, dictionary):
    for d in dictionary:
        if len(brute_key_len(cipher_text, d)) > 0:
            print(f'My guess for the plaintext is: {d}')
        #print(brute_key_len(cipher_text, d))
    
    
    
dictionary_one, dictionary_two = get_dictionaries()

cipher_text = input('Input your ciphertext: ')
#brute_key_len(cipher_text.strip(), dictionary_one[0])
#brute_key_len(dictionary_one[1], dictionary_one[0])
find_pt(cipher_text, dictionary_one)