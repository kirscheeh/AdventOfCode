use std::fs;
use std::collections::HashMap;

fn main() {
    let contents = fs::read_to_string("../../inputs/2016/day06.txt").expect("Should have been able to read the file");

    let mut positions: HashMap<i32, HashMap<char, i32>> = (0..8)
        .map(|i| (i, HashMap::new()))
        .collect();

    for line in contents.lines() {
        for (index, c) in line.chars().enumerate() {
            if let Some(inner_map) = positions.get_mut(&(index as i32)) {
                *inner_map.entry(c).or_insert(0) +=1;
            }
        }
    }
    let mut password_p1 = vec![' '; 8];
    let mut password_p2 = vec![' '; 8];
    for index in 0..positions.len() {
        if let Some(inner) = positions.get(&(index as i32)) {
            if let Some(max_key) = inner.iter().max_by(|a ,b| a.1.cmp(&b.1)).map(|(k, _v)| k) {
                password_p1[index] = *max_key; }
           
            if let Some(min_key) = inner.iter().min_by(|a ,b| a.1.cmp(&b.1)).map(|(k, _v)| k) {
                password_p2[index] = *min_key; }
            
        }
    }
    println!("Part 1: {}", password_p1.iter().collect::<String>());
    println!("Part 2: {}", password_p2.iter().collect::<String>());

    

}