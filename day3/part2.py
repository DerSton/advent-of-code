input = open("day3/input.txt", "r", encoding="utf-8").read().splitlines()

digits = 12
sum = 0

for bank in input:
    result = []
    remaining = digits
    start_idx = 0
    
    while remaining > 0:
        max_skip = len(bank) - start_idx - remaining

        max_digit = "-1"
        max_idx = -1
        for i in range(start_idx, start_idx + max_skip + 1):
            if bank[i] > max_digit:
                max_digit = bank[i]
                max_idx = i
        
        result.append(max_digit)
        start_idx = max_idx + 1
        remaining -= 1
    
    max_number = int("".join(result))
    sum = sum + max_number
    
print(sum)
