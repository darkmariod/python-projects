n = int(input('Enter a number'))
first, second = 0,1
print('Fibonnaci sequence up to', n, ':', end=' ')
for _ in range(n):
    print(first, end=' ')
    first, second = second, first + second

def fibonnaci(n, memo={})
    if n in memo:
        return memo[n]
    if n <= 1:
        return n 
    memo[n] = fibonnaci(n-1, memo) + fibonnaci(n-2, memo)
    return memo[n]
    
n = int(input('Enter a number'))
print('Fibonnaci sequence up to', n, ':', end=' ')
for _ in range(n):
    print(first, end=' ')
    first, second = second, first + second
