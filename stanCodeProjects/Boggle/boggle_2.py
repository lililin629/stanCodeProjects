"""
File: boggle.py
Name: Lilian Lin
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    """
    TODO:
    """
    board = {}
    for i in range(4):
        row = input(str(i+1)+' row of letters: ')
        if check(row):
            board[i] = row.split(' ')
        else:
            print('Illegal input!')

    start = time.time()
    ####################
    all_char = get_all_char(board)
    w_dict = read_dictionary(all_char)
    cur_l = boggle(w_dict, board)
    print('There are', str(len(cur_l)), 'words in total.')
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your boggle algorithm: {end - start} seconds.')


def get_all_char(board):
    all_char = []
    for key in board:
        all_char += board[key]
    return all_char


def boggle(w_dict, board):
    cur_l = []
    for x in range(4):
        for y in range(4):
            coordinates = []
            cur_s = ''
            coordinates.append((x, y))
            cur_s += board[x][y]
            cur_l = boggle_helper(w_dict, board, x, y, coordinates, cur_s, cur_l)
    return cur_l


def boggle_helper(w_dict, board, x, y, coordinates, cur_s, cur_l):
    if len(cur_s) == 4:
        if cur_s not in cur_l:
            for key in w_dict:
                if cur_s in w_dict[key]:
                    cur_l.append(cur_s)
                    print('Found: ', cur_s)
                    for word in w_dict[cur_s[0]]:
                        if len(word) > len(cur_s):
                            if word.startswith(cur_s):
                                longer(w_dict, board, x, y, coordinates, cur_s, cur_l)
    else:
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if 0 <= i < 4 and 0 <= j < 4:
                    if (i, j) not in coordinates:
                        # Choose
                        coordinates.append((i, j))
                        cur_s += board[i][j]
                        # Explore
                        if len(cur_s) > 1:
                            if has_prefix(cur_s, w_dict):
                                boggle_helper(w_dict, board, i, j, coordinates, cur_s, cur_l)
                        # Un-choose
                        coordinates.pop()
                        cur_s = cur_s[:-1]
    return cur_l


def longer(w_dict, board, x, y, coordinates, cur_s, cur_l):
    if len(cur_s) > 4:
        if cur_s not in cur_l:
            for key in w_dict:
                if cur_s in w_dict[key]:
                    cur_l.append(cur_s)
                    print('Found: ', cur_s)
    else:
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < 4 and 0 <= j < 4:
                    if (i, j) not in coordinates:
                        # Choose
                        coordinates.append((i, j))
                        cur_s += board[i][j]
                        # Explore
                        if len(cur_s) > 1:
                            if has_prefix(cur_s, w_dict):
                                longer(w_dict, board, i, j, coordinates, cur_s, cur_l)
                        # Un-choose
                        coordinates.pop()
                        cur_s = cur_s[:-1]


def has_prefix(cur_s, w_dict):
    """
    :param cur_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :param w_dict: a dictionary of words
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    if cur_s[0] not in w_dict:
        return False
    for word in w_dict[cur_s[0]]:
        if word.startswith(cur_s):
            return True
    return False


def check(row):
    if len(row) != 7:
        return False
    for i in range(7):
        if i%2 == 1:
            if row[i] is not ' ':  # is not blank
                return False
        if i%2 == 0:
            if not row[i].isalpha():
                return False
    return True


def read_dictionary(all_char):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    """
    d = {}
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) >= 4:
                if check_others(word, all_char):
                    if word[0] in d:
                        d[word[0]].append(word)
                    else:
                        d[word[0]] = [word]
    return d


def check_others(word, all_char):
    for char in word:
        if char not in all_char:
            return False
    return True

if __name__ == '__main__':
    main()