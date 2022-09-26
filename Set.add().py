# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
Names = set([])
for i in range(n):
    Names.add(input())
print(len(Names))
