def is_leap(year):
        leap = False 
        if year%4==0 and (year%100==0) and year%400==0:
            leap=True
        elif not(year%4==0) and not(year%100==0) and not(year%400==0):
            leap=False
        else:
            leap=False  
        return leap

year = int(input())
print(is_leap(year))
