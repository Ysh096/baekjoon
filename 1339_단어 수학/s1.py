import sys
sys.stdin = open('input.txt')
N = int(input())
dict = {}
for _ in range(N):
    word = input()
    word_len = len(word)
    for i in range(word_len):
        j = word_len-i-1
        if dict.get(word[i]):
            dict[word[i]] += 10**j
        else:
            dict[word[i]] = 10**j
arr = []
for key, val in dict.items():
    arr.append((key, val))
arr.sort(key=lambda x: -x[1])

result = 0
for k in range(len(arr)):
    result += arr[k][1] * (9-k)

print(result)
