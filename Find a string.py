def count_substring(s,ss):
    count = start = 0
    while True:
        start = s.find(ss, start) + 1
        if start > 0:
            count+=1
        else:
            return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
