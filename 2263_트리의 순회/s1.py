import sys
sys.stdin = open('input.txt')

# 중위순회와 후위순회가 주어졌을 때 전위순회를 구해라?
# 후위순회의 마지막은 루트, 중위순회에서 그 루트를 찾아보면 양옆이 왼쪽, 오른쪽
# 왼쪽의 중심(/2)이 또 서브트리의 루트, 오른쪽의 중심이 또 서브트리의 루트, ...
N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
order = []
root = post_order[-1]
order.append(root)
root_idx = in_order.index(root)
def find_order(in_order, root_idx):
    if len(in_order) == 1:
        return
      # 중위순회에서 root의 위치
    left_sub = in_order[:root_idx]
    left_root = len(left_sub) // 2
    order.append(left_sub[left_root])
    find_order(left_sub, left_root)
    if root_idx+1 >= len(in_order):
        return
    else:
        right_sub = in_order[root_idx+1:]
        right_root = len(right_sub) // 2
        order.append(right_sub[right_root])
        find_order(right_sub, right_root)

find_order(in_order, root_idx)
print(*order)

# 0 1 3 7 8 4 9 10 2 5 11 6

