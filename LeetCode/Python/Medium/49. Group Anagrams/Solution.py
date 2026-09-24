class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        seen={}

        for i in strs:
            key=''.join(sorted(i))
            if key not in seen:
                seen[key]=[]
            seen[key].append(i)

        return list(seen.values())