'''
PS: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.
'''

#Solution:
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res=''
       
        if len(word1)>len(word2): #check the lenght of words
            for pos in range(len(word2)): #execute loop based on shorter word length
                res+=word1[pos] #alternatively append characters
                res+=word2[pos] 
            res+=word1[pos+1:] #append remaining characters from word1
            print
        else:
            for pos in range(len(word1)):  #execute loop based on shorter word length
                res+=word1[pos]  #alternatively append characters
                res+=word2[pos]
            res+=word2[pos+1:] #append remaining characters from word2
        return res
      
      '''
      Complexities:
      Space complexity: O(1)
      Time complexity: O(n)
      '''
