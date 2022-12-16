def tribonacci(signature, n):
    sequence = signature
    if n == 0:
        sequence = []
    else:
        for x, y in enumerate(range(0, n)):
            sequence.append(sum(sequence[x:y+3]))
    return sequence[0:n]


    