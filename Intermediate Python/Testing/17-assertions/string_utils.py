#Assertions

import unittest
def reverse_string(s):
  return s[::-1]

def capitalize_string(s):
  return s.capitalize()

def is_capitalized(s):
  return s[0].isupper()

if __name__ == '__main__':
    unittest.main()