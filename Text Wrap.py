import textwrap

def wrap(string, max_width):
    c=max_width-1
    for i in range(len(string)):
        if i==c:
            c=c+max_width
            print(string[i],end="")
            print('')
        else:
            print(string[i],end="")
    return ''

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
