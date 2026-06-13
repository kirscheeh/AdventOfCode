#!/usr/bin/env python

def parse_data(path:str="input/day_10.txt") -> list:
    data = open(path).read().splitlines()
    data = [(2, int(x.split(" ")[1])) if not "noop" in x else (1,0) for x in data]
    return data

def follow_commands(data):
    cycle, cpu = 1, 1   
    signal_strength=0
    
    crt = {x:["."]*40 for x in range(6)}
    sprite=[0,1,2]
    for add_cycle, value in data:
        for _ in range(add_cycle):
            # Part 1
            if cycle in range(20, 260, 40):
                signal_strength = signal_strength+cycle*cpu
                
            # Part 2
            if cycle%40-1 in sprite:
                if 1 <= cycle < 40:
                    crt[0][cycle%40-1]="#"
                elif 40 <= cycle < 80:
                    crt[1][cycle%40-1]="#"
                elif 80 <= cycle < 120:
                    crt[2][cycle%40-1]="#"
                elif 120 <= cycle < 160:
                    crt[3][cycle%40-1]="#"
                elif 160 <= cycle < 200:
                    crt[4][cycle%40-1]="#"
                elif 200 <= cycle < 240:
                    crt[5][cycle%40-1]="#"
            
            cycle+=1
            
        cpu+=value
        sprite = [cpu-1, cpu, cpu+1]

    return signal_strength, crt

        

def main():
    data = parse_data()
    
    signal_strength, crt = follow_commands(data)
    print("one", signal_strength)
    print("two")
    for key, value in crt.items():
        print("".join(value))
          
    
    cpu = 1
if __name__ == "__main__":
    main()