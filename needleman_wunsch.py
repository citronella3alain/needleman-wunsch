#!/usr/bin/python3
#needleman_wunsch.py

import numpy as np

#scores
gamma = -2 # gap penalty
tau = -1 # mismatch penalty
mu = 1 # match reward

#example sentences
#sent1 = "a b c d e f g"
#sent2 = "b b c e g g h i"
sent1 = input("Enter your first sentence:\n")
sent2 = input("Enter your second sentence:\n")
print(sent1 + "\n" + sent2)
set1 = sent1.split()
set2 = sent2.split()

def score(r, c):
    if (score_matrix[1, r, c] != 0):
        return [score_matrix[0, r, c]]
    n_score = score(r-1, c)[0] + gamma
    w_score = score(r, c-1)[0] + gamma
    nw_score = score(r-1, c-1)[0]
    if (set1[r-1] == set2[c-1]):
        nw_score += mu
    else:
        nw_score += tau
    score_vector = (n_score, w_score, nw_score)
    s = max(score_vector)
    s_loc = score_vector.index(s)
    score_matrix[0, r, c] = s
    score_matrix[1, r, c] = 1 + s_loc
    return s, n_score, w_score, nw_score

def align(r, c, side1, side2):
    if (r == 0 or c == 0):
        return (side1, side2)
    s = score(r,c)
    if (score_matrix[1, r, c] == 1):
        side1.insert(0, set1[r-1])
        side2.insert(0, '')
        #side1.insert(0, '')
        #side2.insert(0, set2[c-1])
        return align(r-1, c, side1, side2)

    elif (score_matrix[1, r, c] == 2):
        #side1.insert(0, set1[r-1])
        #side2.insert(0, '')
        side1.insert(0, '')
        side2.insert(0, set2[c-1])
        return align(r, c-1, side1, side2)
    else:
        # directional score == 3
        side1.insert(0, set1[r-1])
        side2.insert(0, set2[c-1])
        return align(r-1, c-1, side1, side2)
    
# Initialize the score matrix.
score_matrix = np.zeros((2, len(set1)+1, len(set2)+1))

for i in list(range(len(set1)+1)):
    score_matrix[0, i, 0] = i * gamma
    score_matrix[1, i, 0] = 1
for i in list(range(len(set2)+1)):
    score_matrix[0, 0, i] = i * gamma
    score_matrix[1, 0, i] = 2
score(len(set1), len(set2))
print(score_matrix)
side1, side2 = [], []
side1, side2 = align(len(set1), len(set2), side1, side2)
print(side1)
print(side2)
