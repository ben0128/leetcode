"""
LeetCode 721. Accounts Merge
Difficulty: Medium
Tags: Array, Hash Table, String
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
    先 init 一個 users，每個人、每個 user 都有自己的根，接著再逐一做 union。

如果在過程中找到了不同的 roots，就要把子樹的 root 掛到另一個 root 上面去合併。
最後再根據題目的要求，answer 的部分用人名當第一個元素，後續掛滿 sorted email。
掃描時遇到看過的 email，它告訴我該跟哪一行 union

複雜度：
    Time: 排序主導，Σ kᵢ log kᵢ ≤ n log n
    Space: 一開始的 inits 是 O(M)，等於 Account 數量。後續的 Email to User 是 O(K)，是 Unique Email 的數量。
"""

from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        users = [i for i in range(len(accounts))]
        m = len(users)
        emailToUser = {}

        def find(n, li):
            while li[n] != li[li[n]]:
                li[n] = li[li[n]]
                n = li[n]
            return li[n]
        
        for i in range(m):
            account = accounts[i]
            for j in range(1, len(account)):
                email = account[j]
                if email not in emailToUser:
                    emailToUser[email] = i
                else:
                    idxA = find(emailToUser[email], users)
                    idxB = find(i, users)
                    users[idxA] = idxB

        ansMap = defaultdict(set)
        for i in range(m):
            currIdx = find(i, users)
            for j in range(1, len(accounts[i])):
                ansMap[currIdx].add(accounts[i][j])
        return [ [accounts[i][0]]+sorted(list(emailSet)) for i, emailSet in ansMap.items()]




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

    # Edge: two single node
    edge_in1 = [["ac1", "ac1@x.com"], ["ac2", "ac2@x.com"]]
    edge_out1 = [["ac1", "ac1@x.com"], ["ac2", "ac2@x.com"]]
    assert normalize(s.accountsMerge(edge_in1)) == normalize(edge_out1), "Edge: single account"
    print("All tests passed!")
