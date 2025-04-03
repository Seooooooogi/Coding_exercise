def solution(nodeinfo):
    # loc = (x, y) 좌표
    # num = node의 직접적인 번호
    class Node:
        def __init__(self, loc, num, left=None, right=None):
            self.loc = loc
            self.num = num
            self.left = left
            self.right = right
            
        def chk_left(self):
            return self.left is not None
        
        def chk_right(self):
            return self.right is not None
        
    def make_tree(nodeinfo):
        # 0번 노드가 없기 때문에 편의성을 위해서 1번부터 담음
        nodes = [i for i in range(1, len(nodeinfo) + 1)]
        # y축은 제일 큰 순서대로, x축은 작은 순서대로 정렬하기 위해 lambda x: nodeinfo[x-1][1], -nodeinfo[x-1][0] 사용
        nodes = sorted(nodes, key=lambda x: (nodeinfo[x-1][1], -nodeinfo[x-1][0]), reverse=True)
        root = None
        for i in range(len(nodes)):
            # root 노드가 없다면 가장 y축이 큰 노드가 root 노드
            if root is None:
                root = Node(nodeinfo[nodes[0] - 1], nodes[0])
            else:
                # 아니라면 parent root부터 시작하여 진행해 가면서 부모 노드로부터 왼쪽인지 오른쪽인지 판별
                parent = root
                node = Node(nodeinfo[nodes[i] - 1], nodes[i])
                while True:
                    # 부모 노드보다 왼쪽일 경우
                    if node.loc[0] < parent.loc[0]:
                        # 부모 노드가 바로 위에 없는 경우 바로 위 부모까지 이동 후 연결
                        # 함수를 부르고 나서 () 안 넣으면 무조건 True로 나옴(주의)
                        if parent.chk_left():
                            parent = parent.left
                            continue
                        # 아니라면 바로 연결
                        parent.left = node
                        break
                    # 부모 노드보다 오른쪽일 경우
                    else:
                        if parent.chk_right():
                            parent = parent.right
                            continue
                        parent.right = node
                        break
        return root
    
    # 전위 순회
    # 현재 것 answer에 추가하고 왼쪽-오른쪽 순으로 나오도록 역순으로 담아줌
    def preorder(root):
        answer = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            answer.append(node.num)
            stack.append(node.right)
            stack.append(node.left)
        return answer
    
    # 후위 순회
    # 왼쪽-오른쪽-위 순으로 나오게 하기 위해 현재 노드에 visited를 담아 True인 경우에만 answer에 append
    def postorder(root):
        answer = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                answer.append(node.num)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return answer
    
    root = make_tree(nodeinfo)
    answer = [preorder(root), postorder(root)]
    
    return answer
  
