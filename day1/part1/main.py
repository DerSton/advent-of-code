input = open("day1/input.txt", "r", encoding="utf-8").read().splitlines()

dial = 50
times_zero = 0

for line in input:
    direction = line[0]
    distaance = line[1:]
    
    sign = 1 if direction == "R" else -1
    
    dial = (dial + sign * int(distaance)) % 100
    
    print(f"turning {distaance} times to the {"right" if direction == "R" else "left"} dial now at {dial}")
    
    if dial == 0:
        times_zero = times_zero + 1

print(f"the dial hit 0 {times_zero} times")
