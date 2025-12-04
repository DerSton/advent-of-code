input = open("day3/input.txt", "r", encoding="utf-8").read().splitlines()

sum = 0

for bank in input:
    numbers = []
    
    for index, number in enumerate(bank):

        for number2 in bank[index+1:]:
            numbers.append(int(f"{number}{number2}"))
            
    numbers.sort()

    sum = sum + numbers[-1]
    
print(sum)
