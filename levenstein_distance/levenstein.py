def levenstein(str1, str2):
    """returns levenstein's distance between str1 and str2"""
    a, b = len(str1), len(str2)
    table = [list(range(a+1))]
    table.extend([[i] for i in range(1, b+1)])
    for i in range(1, b+1):
        for j in range(1, a+1):
            if str1[j-1] == str2[i-1]:
                table[i].append(min(table[i-1][j-1],
                                    table[i-1][j]+1,
                                    table[i][j-1]+1))
            else:
                table[i].append(min(table[i-1][j-1]+2,
                                    table[i-1][j]+1,
                                    table[i][j-1]+1))
    return table[-1][-1]


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(levenstein(str1, str2))
