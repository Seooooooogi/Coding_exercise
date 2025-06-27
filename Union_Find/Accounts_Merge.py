from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union-find 방식
        def find(parents, x):
            if parents[x] != x:
                parents[x] = find(parents, parents[x])
            return parents[x]
        
        def union(x, y, parents):
            root1 = find(parents, x)
            root2 = find(parents, y)

            parents[root1] = root2
         
        parents = {}
        email_to_name = {}
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                if email not in parents:
                    parents[email] = email
                # 중복 이메일이 있으면 first_email이 root가 되도록 union
                union(email, first_email, parents)
                email_to_name[email] = name
        
        roots = defaultdict(list)
        answer = []

        # root email을 찾아주고 root email에다가 자식 이메일을 담아줌
        for email in parents.keys():
            root_email = find(parents, email)
            roots[root_email].append(email)
        
        # root email의 이름을 찾아 나머지 이메일을 한꺼번에 정답에 추가
        for root_email, emails in roots.items():
            name = email_to_name[root_email]
            answer.append([name] + sorted(emails))
        return answer
        
