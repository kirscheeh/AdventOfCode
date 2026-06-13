import math

junction_boxes = open("inputs/2025/day08.txt").read().splitlines()

def euclidian_distance(box1, box2) -> float:
    return math.sqrt((box1[0]-box2[0])**2 + (box1[1]-box2[1])**2 + (box1[2]-box2[2])**2)

def read_boxes(boxes:str)-> dict[int, tuple[int, int, int]]:
    junction_boxes = []
    for box in boxes:
        junction_boxes.append(tuple(map(int, box.split(","))))
    return junction_boxes

def get_distances(boxes:list) -> list[tuple[int, int, float]]:
    dist = []
    
    for i1, box1 in enumerate(boxes):
        for i2, box2 in enumerate(boxes):
            if i1 <= i2:
                continue
            dist.append((box1, box2, euclidian_distance(box1, box2)))
    
    return sorted(dist, key=lambda x: x[2])

def connect_x_boxes(eucl_dist:list[tuple], boxes, number, p2=False) -> dict:
    # returns circuits
    circuits = {}
    number_circuits = 1
    not_in_circuit = {box:True for box in boxes}
    first = True
    if p2:
        loop_range = len(eucl_dist)+20
    else:
        loop_range=number

    for (box1, box2, _) in eucl_dist[:loop_range]:

        if (nr_circuit:=circuits.get(box1)) and not circuits.get(box2): # one is in circuit
            circuits[box2] = nr_circuit
            not_in_circuit[box2]=False

        elif (nr_circuit:=circuits.get(box2)) and not circuits.get(box1): # two is in circuit
            circuits[box1] = nr_circuit
            not_in_circuit[box1]=False
        elif (nr_circuit1:=circuits.get(box1)) and (nr_circuit2:=circuits.get(box2)): # both are in circuit
            if nr_circuit1 == nr_circuit2: # same circuit
                pass
            else: # different circuit
                nr2_boxes = [box for box, value in circuits.items() if value == nr_circuit2]
                for box in nr2_boxes:
                    circuits[box] = nr_circuit1  
        else: # non on circuit
            circuits[box1] = number_circuits
            circuits[box2] = number_circuits
            not_in_circuit[box1] = False
            not_in_circuit[box2] = False
            number_circuits +=1

        if sum(list(not_in_circuit.values())) == 0 and p2 and first:
            print("Part2", box1[0]*box2[0])
            return 0
        
    return circuits

def get_circuit_sizes(circuits: dict) -> list[int]:
    circuit_numbers = set(circuits.values())
    
    return sorted([list(circuits.values()).count(nr) for nr in circuit_numbers])

def get_bridge_boxes(circuits: dict):
    pass

boxes = read_boxes(junction_boxes)
sorted_euclidian_distances = get_distances(boxes)

circuits = connect_x_boxes(sorted_euclidian_distances, boxes, 1000, True)
if not circuits == 0:
    print("Part 1", math.prod(get_circuit_sizes(circuits)[-3:]))