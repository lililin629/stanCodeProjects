"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def read_dictionary(s):
    dict_lst = []
    with open(FILE, "r") as f:
        for line in f:
            word = line[0:len(line)-1]   # exclude '/n' at the end of each line
            if len(word) == len(s) and word[0] in s:
                # Append only words starting with characters in original word and are the same length as original word
                dict_lst.append(word)
    return dict_lst


def main():
    """
    TODO:
    """
    print('Welcome to stanCode \"Anagram Generator\"( or -1 to quit)')
    while True:
        s = str(input('Find anagrams for: '))
        start = time.time()  # To measure time spent
        find_anagrams(s)
        ########################################################################
        # To measure time spent
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')
        ########################################################################
        if s == str(-1):
            break


def find_anagrams(s):
    """
    :param s: user input string
    :return: number and a list of anagrams found
    """
    dict_lst = read_dictionary(s)
    anagram_lst = []
    helper(s, '', len(s), dict_lst, anagram_lst, [])
    print(str(len(anagram_lst)), ' anagrams:', anagram_lst)


def helper(original_word, new_word, ans_len, dict_lst, anagram_lst, index_lst):
    if len(new_word) == ans_len:
        if new_word not in anagram_lst:
            if new_word in dict_lst:
                print('Searching...')
                print(new_word)
                anagram_lst.append(new_word)
    else:
        for i in range(len(original_word)):
            if i not in index_lst:
                # choose
                new_word += original_word[i]
                index_lst.append(i)
                if has_prefix(new_word, dict_lst):
                    # explore
                    helper(original_word, new_word, ans_len, dict_lst, anagram_lst, index_lst)
                # un-choose
                new_word = new_word[0:len(new_word)-1]
                index_lst.pop()


def has_prefix(sub_s, dict_lst):
    """
    :param dict_lst: dictionary containing words starting with the characters in the original word and are the same
    length with the original word
    :param sub_s: string, the first few characters of a new word
    :return: boolean, whether there is a word in the dictionary that starts with the sub_str
    """
    for word in dict_lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
