use std::fs;
use std::collections::HashMap;

enum Direction {
    Up,
    Down,
    Left,
    Right
}


fn apply_move(pos: (i32, i32),  dir: Direction, allowed: &HashMap<(i32, i32), String>) -> (i32, i32) {
    let new_pos = match dir {
        Direction::Up =>  (pos.0, pos.1 - 1),
        Direction::Down =>  (pos.0, pos.1 + 1),
        Direction::Left => (pos.0 - 1, pos.1),
        Direction::Right =>   (pos.0 + 1, pos.1)};

    if allowed.contains_key(&new_pos) {
        return new_pos;
    }
    else {
        return pos;
    }    
    
}

fn main() {
     let contents = fs::read_to_string("../../inputs/2016/day02.txt")
        .expect("Should have been able to read the file");
    
    // the translator section needs to be adapted
    let mut translator: HashMap<(i32, i32), String> = HashMap::new();

    translator.insert((0, 0), "5".to_string());
    translator.insert((1, 0), "6".to_string());
    translator.insert((2, 0), "7".to_string());
    translator.insert((3, 0), "8".to_string());
    translator.insert((4, 0), "9".to_string());

    translator.insert((1, -1), "2".to_string());
    translator.insert((2, -1), "3".to_string());
    translator.insert((3, -1), "4".to_string());
    translator.insert((2, -2), "1".to_string());

    translator.insert((1, 1), "A".to_string());
    translator.insert((2, 1), "B".to_string());
    translator.insert((3, 1), "C".to_string());
    translator.insert((2, 2), "D".to_string());

    let instructions = contents.split("\n");
    let mut current_pos = (0,0); // center 5
    let mut keypresses: Vec<String>  = Vec::<String>::new();

    for instruc in instructions {
        for movement in instruc.chars() {
            current_pos = match movement {
                'U' => apply_move(current_pos, Direction::Up, &translator),
                'D' => apply_move(current_pos, Direction::Down, &translator),
                'L' => apply_move(current_pos, Direction::Left, &translator),
                'R' => apply_move(current_pos, Direction::Right, &translator),
                _ => panic!("unknown")
            };
        }
        keypresses.push(translator
        .get(&current_pos)
        .expect("huh")
        .clone()
);
       
    }
    println!("{:?}", keypresses);
}