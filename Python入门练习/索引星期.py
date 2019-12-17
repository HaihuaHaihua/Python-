days="MonTueWedThuFriSatSun"
n=input("input a day(1-7): ")
pos=(int(n)-1)*3
dayAbbrev=days[pos:pos+3]
print("the day is : "+dayAbbrev+'.')

input()
