scorelist = []
Result = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result+=[[name,score]]
        scorelist+=[score]
    a=sorted(list(set(scorelist))) [1]
    for b,c in sorted(Result):
        if c==a:
            print(b)
