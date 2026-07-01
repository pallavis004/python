def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    for i in range(3):
        if a[i] > b[i]:
            a_score += 1
        if a[i] < b[i]:
           b_score += 1
    return [a_score, b_score]

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = compareTriplets(a, b)
print(result[0], result[1])