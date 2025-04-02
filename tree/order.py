# 상 좌 우 순으로 순회
def preorder(nodes, idx):
    if idx < len(nodes):
        ans = str(nodes[idx]) + " "
        ans += preorder(nodes, idx * 2 + 1)
        ans += preorder(nodes, idx * 2 + 2)
        return ans
    else:
        return ""

# 좌 상 우 순으로 순회
def inorder(nodes, idx):
    if idx < len(nodes):
        ans = inorder(nodes, idx * 2 + 1)
        ans += str(nodes[idx]) + " "
        ans += inorder(nodes, idx * 2 + 2)
        return ans
    else:
        return ""

# 좌 우 상 순으로 순회
def postorder(nodes, idx):
    if idx < len(nodes):
        ans = postorder(nodes, idx * 2 + 1)
        ans += postorder(nodes, idx * 2 + 2)
        ans += str(nodes[idx]) + " "
        return ans
    else:
        return ""
