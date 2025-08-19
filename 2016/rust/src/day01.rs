use std::fs;
use std::collections::HashSet;

enum Direction {
    North,
    East,
    South,
    West
}

impl Direction {
    fn turn_left(&self) -> Direction {
        match self {
            Direction::North => Direction::West,
            Direction::West => Direction::South,
            Direction::South => Direction::East,
            Direction::East => Direction::North
        } }

    fn turn_right(&self) -> Direction {
        match self {
            Direction::North => Direction::East,
            Direction::East  => Direction::South,
            Direction::South => Direction::West,
            Direction::West  => Direction::North
            }
    }
}

fn get_distance(pos:(i32, i32)) -> i32 {
    pos.0.abs() + pos.1.abs()
}

fn check_positions(loc: &mut HashSet<(i32, i32)>, start:(i32, i32), stop: (i32, i32), do_not_check:bool) -> (bool, (i32, i32)) {
    if start.0 == stop.0 { // horizontal move
        // get start and stop, index shuffling
        let (y1, y2) = if stop.1 < start.1 { (stop.1, start.1-1) } else {(start.1+1, stop.1)};

        for y in y1..=y2 {
            if loc.contains(&(start.0, y)) && !do_not_check {
                return (true, (start.0, y));
            } 
            else {
                loc.insert((start.0, y));  
            }
             
        }
    }
    else { // vertical move
                // get start and stop, index shuffling

        let (x1, x2) = if stop.0 < start.0 { (stop.0, start.0-1) } else {(start.0+1, stop.0)};
        
        for x in x1..=x2 {
            if loc.contains(&(x, start.1)) && !do_not_check {
                return (true, (x, start.1));
            } else {
            loc.insert((x, start.1));     
            }
        }
    }
    // can only be here if no path crossing happened
    return (do_not_check, (0,0));
}

fn move_it(pos: (i32, i32), direction: &Direction, steps: i32) -> (i32, i32) {
    match direction {
        Direction::North => (pos.0, pos.1 + steps),
        Direction::East  => (pos.0 + steps, pos.1),
        Direction::South => (pos.0, pos.1 - steps),
        Direction::West  => (pos.0 - steps, pos.1)
    }
}
fn main() {
    let contents = fs::read_to_string("../../inputs/2016/day01.txt")
        .expect("Should have been able to read the file");

    let instructions = contents.split(", ");
    
    let mut current_position = (0,0);
    let mut direction = Direction::North;
    let mut visited:HashSet<(i32, i32)> = HashSet::new();
    let mut first_location_visited_twice = false;
    let mut first_duplicate = (0,0);
    let mut test_pos = (0,0);

    for instruc in instructions {
        let (turn, steps) = instruc.trim().split_at(1);
        let steps: i32 = steps.parse().expect("This should be a step number, INTEGER!");

        // get next directoin to face after turn
        direction = match turn {
            "L" => direction.turn_left(),
            "R" => direction.turn_right(),
            _ => panic!("unknown turn"),
        };

        let next_position = move_it(current_position, &direction, steps);
        // check if on path to new position, path is crossed
        (first_location_visited_twice, test_pos) = check_positions(&mut visited, current_position, next_position, first_location_visited_twice);

        // only safe the first path-crossing
        if first_location_visited_twice && first_duplicate == (0,0) {
            first_duplicate = test_pos;
        }
        current_position = next_position;
    }
    println!("Part 1: {}", get_distance(current_position));
    println!("Part 2: {}", get_distance(first_duplicate));
}