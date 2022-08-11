count = 0
with open('hello.txt','r')as file:
    for line in file:
        words = line.split()
        for word in words:
            if 'hello' in word:
                count = count + 1
print(count)
