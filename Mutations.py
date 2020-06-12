def mutate_string(string, position, character):
    s=''
    for i in range(len(string)):
        if i==position:
            s=s+character
        else:
            s=s+string[i]
    return s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
