use std::fs;

fn split_instruction(command:&str) -> (char, i32) {
   
   let direction = match command.chars().next() {
        Some(char) => match char {
            'L' => char,
            'R' => char,
            _ => panic!("Direction must be either R or L!")
        },
        None => panic!("You need a direction!")
    };

    let steps = command[1..].parse::<i32>().expect("This needs to be a numerical value!");

   (direction, steps)
}

fn spin(mut current_position: i32, (direction, mut step): (char, i32)) -> (i32, i32) {
    let real_step = step % 100;
    let mut border_crosser = 0;
    if direction == 'R' {
        
        current_position += real_step;

        if current_position > 99 {
            current_position -= 100;        
        }
    } else {

        current_position -= real_step;
        
        if current_position < 0 {
            current_position = 100 + current_position;
        }
    }
    (current_position, (step / 100) + border_crosser)
}

fn main() {
    let data = fs::read_to_string("../../inputs/2025/day01.txt")
        .expect("Should have been able to read the file");

    let mut dial_pos = 50;

    let rotations = data.split("\n").map(|s| split_instruction(&s));

    let mut border_counter = 0;
    let mut cross_border = 0;

    for instruction in rotations {
        (dial_pos, cross_border) = spin(dial_pos, instruction);
        
        //if dial_pos == 0 {
        //    border_counter += 1;
        //}

        border_counter += cross_border;
    }

    println!("{}", border_counter);  
}
