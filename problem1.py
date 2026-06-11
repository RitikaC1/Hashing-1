# LEETCODE PROBLEM 49. GROUP ANAGRAMS
# TIME COMPLEXITY: 
#   Approach 1: O(N * Klog K) where N is the number of elements and K is the length of a string
#   Approach 2: 
# SPACE COMPLEXITY: O (1)
# Any problem you faced while coding this:  

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Approach 1
        #Hashing Approach
        hashmap={}
        for string in strs:
            sorted_string=''.join(sorted(string))
            if sorted_string not in hashmap:
                hashmap[sorted_string]=[]
            hashmap[sorted_string].append(string)
        return list(hashmap.values())

        