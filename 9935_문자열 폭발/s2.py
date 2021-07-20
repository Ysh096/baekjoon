import sys
sys.stdin = open('input.txt')

text = input()
check = input()

check_len = len(check)

stack = []
for w in text:
    stack.append(w)
    if w == check[-1]:
        if ''.join(stack[-check_len:]) == check:
            for _ in range(check_len):
                stack.pop()
if stack == []:
    print("FRULA")
else:
    print(''.join(stack))