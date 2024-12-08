use std::fs;
use std::collections::HashSet;


fn main() {
    let contents = fs::read_to_string("inputs/day03.txt")
        .expect("Should have been able to read the file");

    let mut coord = (0,0);

    // let mut visited: Vec<(i32, i32)> = vec![(0, 0)]; // better: 
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    visited.insert(coord);
    
    let mut presents = 1;

    let mut santa = (0,0);
    let mut robo_santa = (0,0);

    let mut visited_santas: HashSet<(i32, i32)> = HashSet::new();
    visited_santas.insert(santa);
    
    let mut presents_santas = 1;

    for (index, c) in contents.chars().enumerate() {
        let current_santa = if index % 2 == 0 { &mut santa } else { &mut robo_santa };

        match c {
            '>' => {
                coord.0 += 1;
                current_santa.0 += 1;
            }
            '<' => {
                coord.0 -= 1;
                current_santa.0 -= 1;
            }
            '^' => {
                coord.1 -= 1;
                current_santa.1 -= 1;   
            }
            'v' => {
                coord.1 += 1;
                current_santa.1 += 1;
            }
            _ => continue
        }

        // Part 1
        if !visited.contains(&coord) {
            presents += 1;
            visited.insert(coord);
        } 

        // Part 2
        if !visited_santas.contains(&current_santa) {
            presents_santas += 1;
            visited_santas.insert(*current_santa);
        } 
        
    }
    println!("Santa visists {} houses at least once.", presents);
    println!("Santa and Robo-Santa visist {} houses at least once.", presents_santas);
}