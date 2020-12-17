n=20
primo=1
secondo=1

for i in range(n):
    print(primo, end=' ')
    fibonacci=primo+secondo
    primo=secondo
    secondo=fibonacci
