# Solution 1
##from collections import defaultdict
##
##class Solution:
##    def groupAnagram(self, strs):
##        groups = defaultdict(list)
##        for word in strs:
##            key = "".join(sorted(word))
##            groups[key].append(word)
##
##        return list(groups.values())
##obj = Solution()
##print(obj.groupAnagram(["eat","tea","tan","ate","nat","bat"]))

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord('a')] +=1

            groups[tuple(count)].append(word)

        return list(groups.values())
                
        