"""
LeetCode 721. Accounts Merge
Difficulty: Medium
Tags: Array, Hash Table, String, DFS, BFS, Union Find, Sorting
URL: https://leetcode.com/problems/accounts-merge/

Problem:
    Given a list of accounts where each element accounts[i] is a list of strings,
    where the first element accounts[i][0] is a name, and the rest of the elements
    are emails representing emails of the account.

    Now, we would like to merge these accounts. Two accounts definitely belong
    to the same person if there is some common email to both accounts. Note that
    even if two accounts have the same name, they may belong to different people
    as people could have the same name. A person can have any number of accounts
    initially, but all of their accounts definitely have the same name.

    After merging the accounts, return the accounts in the following format: the
    first element of each account is the name, and the rest of the elements are
    emails in sorted order. The accounts themselves can be returned in any order.

    Example 1:
        Input: accounts = [
            ["John","johnsmith@mail.com","john_newyork@mail.com"],
            ["John","johnsmith@mail.com","john00@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]
        Output: [
            ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
            ["Mary","mary@mail.com"],
            ["John","johnnybravo@mail.com"]
        ]
        Explanation:
            The first and second John's are the same person as they have the
            common email "johnsmith@mail.com".
            The third John and Mary are different people as none of their email
            addresses are used by other accounts.
            We could return these lists in any order.

    Example 2:
        Input: accounts = [
            ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
        ]
        Output: [
            ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
            ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
            ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
            ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
            ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]
        ]

    Constraints:
        - 1 <= accounts.length <= 1000
        - 2 <= accounts[i].length <= 10
        - 1 <= accounts[i][j].length <= 30
        - accounts[i][0] consists of English letters.
        - accounts[i][j] (for j > 0) is a valid email.

思路：
    1. row index 當 UF 節點（不用 name，因為同名可能不同人）
    2. emailToIdx[email] = row 當橋樑：掃到重複 email 就 union 兩個 row
    3. 聚合：find 出每個 email 的 root，同 root 一組，排序後貼上名字
    陷阱：union 要寫 roots[find(i)] = find(j)，不能寫 roots[i] = ...（會斷鏈）

複雜度：
    n = 總共的 email 數量
    Time: O(n log n)   # 瓶頸是排序，UF 操作近似 O(α(n))
    Space: O(n)        # emailToIdx + roots + 輸出
"""

from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        roots = [i for i in range(n)]
        emailToIdx = {}
        def find(node):
            while roots[node] != roots[roots[node]]:
                roots[node] = roots[roots[node]]
            return roots[node]
        
        for i in range(n):
            account = accounts[i]
            for email in account[1:]:
                if email in emailToIdx:
                    roots[find(i)] = find(emailToIdx[email])
                emailToIdx[email] = roots[i]
        
        tmp = defaultdict(list)
        for email, idx in emailToIdx.items():
            rootI = find(idx)
            tmp[rootI].append(email)
        for v in tmp.values():
            v.sort()
        return [[accounts[idx][0]]+emails for idx, emails in tmp.items()]



if __name__ == "__main__":
    s = Solution()

    def normalize(result):
        # Outer list order is unspecified; inner lists are name + sorted emails.
        # Sort outer list to get a deterministic comparison.
        return sorted([list(acc) for acc in result])

    # Case 1: two Johns share johnsmith@mail.com → merged; third John separate; Mary separate
    case1_in = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    case1_out = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    assert normalize(s.accountsMerge(case1_in)) == normalize(case1_out), "Case 1"

    # Case 2: no overlap at all → output equals input with sorted emails per account
    case2_in = [
        ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
    ]
    case2_out = [
        ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
    ]
    assert normalize(s.accountsMerge(case2_in)) == normalize(case2_out), "Case 2"

    # Case 3: chain merge — A overlaps B, B overlaps C → all three merge into one
    case3_in = [
        ["Alex", "a@x.com", "b@x.com"],
        ["Alex", "b@x.com", "c@x.com"],
        ["Alex", "c@x.com", "d@x.com"],
    ]
    case3_out = [
        ["Alex", "a@x.com", "b@x.com", "c@x.com", "d@x.com"],
    ]
    assert normalize(s.accountsMerge(case3_in)) == normalize(case3_out), "Case 3 chain merge"

    # Case 4: diamond merge — row 2 bridges row 0 and row 1 (no direct overlap between 0 and 1)
    case4_in = [
        ["John", "a@x", "b@x"],
        ["John", "c@x", "d@x"],
        ["John", "b@x", "c@x"],
    ]
    case4_out = [
        ["John", "a@x", "b@x", "c@x", "d@x"],
    ]
    assert normalize(s.accountsMerge(case4_in)) == normalize(case4_out), "Case 4 diamond merge"

    # Edge: single account, single email
    edge_in = [["Solo", "solo@x.com"]]
    edge_out = [["Solo", "solo@x.com"]]
    assert normalize(s.accountsMerge(edge_in)) == normalize(edge_out), "Edge: single account"

    print("All tests passed!")
