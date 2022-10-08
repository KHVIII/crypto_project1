import random

alphabet = ' abcdefghijklmnopqrstuvwxyz'
max_key_length = 25
'''Helper function'''
def get_dictionaries():
    d_one = open('dictionary_1.txt', 'r').readlines()
    d_two = open('dictionary_2.txt', 'r').readlines()
    
    for index,text in enumerate(d_one):
        d_one[index] = text.strip('\n\r')
    
    for index,text in enumerate(d_two):
        d_two[index] = text.strip('\n\r')
    
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
    #print(len(string_one))
    #print(len(string_two))
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
    
def do_shift(char, shift):
    new_index = alphabet.index(char) + shift
    if new_index >=27:
        new_index -= 27
    return alphabet[new_index]

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

def build_key(cipher_text, plain_text, length):
    key = []
    for i in range(length):
        key.append(calc_shift(plain_text[i], cipher_text[i]))
    return key

def decrypt(cipher_text, key):
    ret = ''
    i = 0
    for c in cipher_text:
        ret += do_shift(c, key[i])
        i+=1
        if i >= len(key):
            i = 0
    return ret

def brute_key_len(cipher_text, plain_text):
    possible_lengths = []
    for key_len in range(1, max_key_length):
        cipher_chars = get_all_i_th_chars(cipher_text, key_len)
        plain_chars = get_all_i_th_chars(plain_text, key_len)
        
        shifts = calculate_shifts(plain_chars, cipher_chars)
        #print(shifts)
        if len(list(set(shifts))) == 1:
            #print(f'Possible key length {shifts[0]}')
            possible_lengths.append(key_len)
    
    return possible_lengths

def find_pt(cipher_text, dictionary):
    for d in dictionary:
        possible_key_lengths = brute_key_len(cipher_text, d)
        if len(possible_key_lengths) > 0:
            for key_len in possible_key_lengths:
                key = build_key(cipher_text, d, key_len)
                if decrypt(cipher_text, key) == d:
                    print(f'My guess for the plaintext is: {d}')
                    return
    
    
    
dictionary_one, dictionary_two = get_dictionaries()

cipher_text = input('Input your ciphertext: ')
#print(brute_key_len(cipher_text.strip(), dictionary_one[0]))
#brute_key_len(dictionary_one[1], dictionary_one[0])
find_pt(cipher_text, dictionary_one)
