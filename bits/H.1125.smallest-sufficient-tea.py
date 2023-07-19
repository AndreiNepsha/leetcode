# TODO editorial

class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        n = len(people)
        m = len(req_skills)
        skill_id = dict()
        for i, skill in enumerate(req_skills):
            skill_id[skill] = i
        skills_mask_of_person = [0] * n
        for i in range(n):
            for skill in people[i]:
                skills_mask_of_person[i] |= 1 << skill_id[skill]

        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0
        for skills_mask in range(1, 1 << m):
            for i in range(n):
                smaller_skills_mask = skills_mask & ~skills_mask_of_person[i]
                if smaller_skills_mask != skills_mask:
                    people_mask = dp[smaller_skills_mask] | (1 << i)
                    if people_mask.bit_count() < dp[skills_mask].bit_count():
                        dp[skills_mask] = people_mask

        answer_mask = dp[(1 << m) - 1]
        ans = []
        for i in range(n):
            if (answer_mask >> i) & 1:
                ans.append(i)
        return ans


a = Solution().smallestSufficientTeam(
    ["cpp", "python", "javascript", "kotlin", "ruby", "r", "c", "rust", "vb"],
    [["cpp", "c", "rust"], ["cpp", "python", "javascript", "c", "r", "rust"], ["cpp", "python", "javascript", "c", "r", "vb"], ["cpp", "python", "javascript", "ruby", "kotlin", "r", "c", "rust", "vb"], ["cpp", "python", "javascript", "kotlin", "ruby", "r", "c", "rust", "vb"], ["python", "r"], ["cpp", "python", "javascript", "ruby", "kotlin", "r", "c", "rust", "vb"], ["cpp", "python", "javascript", "r", "c", "rust"], ["cpp", "javascript", "rust", "vb"], ["kotlin", "ruby", "c", "vb"], ["cpp", "python", "kotlin", "ruby", "rust", "vb"], ["ruby", "c", "r", "rust"], ["python", "javascript"], ["javascript", "ruby", "rust"], ["python", "javascript", "ruby", "c", "r", "rust", "vb"], ["cpp", "javascript", "kotlin", "r", "c", "vb"], ["c", "rust"], ["cpp", "kotlin", "ruby", "c", "r", "rust", "vb"], ["cpp", "python", "javascript", "ruby", "kotlin", "rust"], ["cpp", "javascript", "ruby"], ["vb"]]
)
assert [3] == a, a

a = Solution().smallestSufficientTeam(
    ["hfkbcrslcdjq","jmhobexvmmlyyzk","fjubadocdwaygs","peaqbonzgl","brgjopmm","x","mf","pcfpppaxsxtpixd","ccwfthnjt","xtadkauiqwravo","zezdb","a","rahimgtlopffbwdg","ulqocaijhezwfr","zshbwqdhx","hyxnrujrqykzhizm"],
    [["peaqbonzgl","xtadkauiqwravo"],["peaqbonzgl","pcfpppaxsxtpixd","zshbwqdhx"],["x","a"],["a"],["jmhobexvmmlyyzk","fjubadocdwaygs","xtadkauiqwravo","zshbwqdhx"],["fjubadocdwaygs","x","zshbwqdhx"],["x","xtadkauiqwravo"],["x","hyxnrujrqykzhizm"],["peaqbonzgl","x","pcfpppaxsxtpixd","a"],["peaqbonzgl","pcfpppaxsxtpixd"],["a"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk"],["hfkbcrslcdjq","xtadkauiqwravo","a","zshbwqdhx"],["peaqbonzgl","mf","a","rahimgtlopffbwdg","zshbwqdhx"],["xtadkauiqwravo"],["fjubadocdwaygs"],["x","a","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl"],["pcfpppaxsxtpixd","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","rahimgtlopffbwdg"],["zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","brgjopmm","x"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk","a","ulqocaijhezwfr"],["peaqbonzgl","x","a","ulqocaijhezwfr","zshbwqdhx"],["mf","pcfpppaxsxtpixd"],["fjubadocdwaygs","ulqocaijhezwfr"],["fjubadocdwaygs","x","a"],["zezdb","hyxnrujrqykzhizm"],["ccwfthnjt","a"],["fjubadocdwaygs","zezdb","a"],[],["peaqbonzgl","ccwfthnjt","hyxnrujrqykzhizm"],["xtadkauiqwravo","hyxnrujrqykzhizm"],["peaqbonzgl","a"],["x","a","hyxnrujrqykzhizm"],["zshbwqdhx"],[],["fjubadocdwaygs","mf","pcfpppaxsxtpixd","zshbwqdhx"],["pcfpppaxsxtpixd","a","zshbwqdhx"],["peaqbonzgl"],["peaqbonzgl","x","ulqocaijhezwfr"],["ulqocaijhezwfr"],["x"],["fjubadocdwaygs","peaqbonzgl"],["fjubadocdwaygs","xtadkauiqwravo"],["pcfpppaxsxtpixd","zshbwqdhx"],["peaqbonzgl","brgjopmm","pcfpppaxsxtpixd","a"],["fjubadocdwaygs","x","mf","ulqocaijhezwfr"],["jmhobexvmmlyyzk","brgjopmm","rahimgtlopffbwdg","hyxnrujrqykzhizm"],["x","ccwfthnjt","hyxnrujrqykzhizm"],["hyxnrujrqykzhizm"],["peaqbonzgl","x","xtadkauiqwravo","ulqocaijhezwfr","hyxnrujrqykzhizm"],["brgjopmm","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl","pcfpppaxsxtpixd"],["fjubadocdwaygs","x","a","zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","x"],["ccwfthnjt"]]
)
assert [13, 32, 49, 50, 51, 52] == a, a
