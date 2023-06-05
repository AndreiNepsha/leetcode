class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        grps: dict[str, list[str]] = {}
        for s in strs:
            ss = str(sorted(s))
            if ss in grps:
                grps[ss].append(s)
            else:
                grps[ss] = grps[ss] = [s]
        return list(grps.values())