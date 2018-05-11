def hack(n, k):
    def countOne(s):
        return s.count('1')
    binario = []
    for i in range(2**n):
        binario.append(bin(i))
    binario.sort(key=countOne, reverse = True)
    return binario

print(hack(3, 5))

##https://www.youtube.com/watch?time_continue=38&v=sAEjJF9HbMc