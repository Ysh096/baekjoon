import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def main(n):
    a.sort()
    b.sort()
    ab = [i + j for i in a for j in b]
    ab.sort()
    ab.append((1 << 29) + 2)
    c.sort(reverse=True)
    d.sort(reverse=True)
    cd = [i + j for i in c for j in d]
    cd.sort(reverse=True)
    cd.append((1 << 29) + 1)
    i = j = 0
    k = n * n
    res = 0
    while (i < k and j < k):
        m = ab[i] + cd[j]
        if (m > 0):
            j += 1
        elif (m < 0):
            i += 1
        else:
            u, v = ab[i], cd[j]
            p = i
            q = j
            while (u == ab[i]): i += 1
            while (v == cd[j]): j += 1
            res += (i - p) * (j - q)

    return res


if __name__ == '__main__':
    n = int(input())
    a, b, c, d = [], [], [], []
    for _ in range(n):
        v, w, x, y = map(int, input().split())
        a.append(v)
        b.append(w)
        c.append(x)
        d.append(y)
    print(main(n))