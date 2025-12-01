input = open("day1/input.txt", "r", encoding="utf-8").read().splitlines()

dial = 50
times_zero = 0

for line in input:
    direction = line[0]
    distaance = int(line[1:])
    
    sign = 1 if direction == "R" else -1
    
    for i in range(distaance):
        dial = dial + sign
        
        if dial > 99:
            dial = 0
        elif dial < 0:
            dial = 99
        
        if dial == 0:
            times_zero = times_zero + 1
            
    print(f"turning {distaance} times to the {"right" if direction == "R" else "left"} dial now at {dial}")

print(f"the dial hit 0 {times_zero} times")
