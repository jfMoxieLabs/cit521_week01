############################################################
# CIS 521: Homework 1
############################################################

student_name = "John Farrell"

# This is where your grade report will be sent.
student_email = "johnfar@seas.upenn.edu" 

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """Python is strongly typed as an objects does not change unless explicity casted.  For instance, the number 11 can not be added with the string "1" as one could in Javascript without first casting one of them into the same type.  When we say Pyhton is dynamically typed we are referring to the fact that we do not need to explicity define the type for a variable.  Variables in Python are able to udpate at runtime based on what is being assigned.  For example, we can set the variable test = 4 and then later set it to test = "this is a test" """

python_concepts_question_2 = """We cannot use a list for a dictionary key and therefore this will fail.  Practically speaking, the point of a dictionary is to make it easier to refernce data and therefore the names make more sense as the key in this case.  We would then have names_to_points = {"home": [0, 0], "school": [1, 2], "market": [-1, 1]}"""

python_concepts_question_3 = """With the for loop we will need to continually add the next string to result and then loop back over it again and again allocating memory each time.  With join we are allowing Python to determine the number of strings to be combined and allocates that space.  Join ends up being significantly faster and cleaner written code."""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    pass

def transpose(matrix):
    pass

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    pass

def all_but_last(seq):
    pass

def every_other(seq):
    pass

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    pass

def suffixes(seq):
    pass

def slices(seq):
    pass

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    pass

def no_vowels(text):
    pass

def digits_to_words(text):
    pass

def to_mixed_case(name):
    pass

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        pass

    def get_polynomial(self):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __call__(self, x):
        pass

    def simplify(self):
        pass

    def __str__(self):
        pass

############################################################
# Section 7: Python Packages
############################################################
import numpy
def sort_array(list_of_matrices):
	pass

import nltk
def POS_tag(sentence):
	pass

############################################################
# Section 8: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""