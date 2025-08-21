use std::fs;
use regex::Regex;
use std::collections::HashMap;

extern crate regex;

fn decode(name: &str, sector_id: i32) -> String { //casesar cipher
    let shift = sector_id % 26;
    let test: String = name.chars()
        .map(|c|  { 
            if c == '-' { // turn into spaces
                ' '
            } else if c.is_ascii_lowercase() {
                let a = b'a';
                let shifted: u8 = ((c as u8 - a + shift as u8) % 26) +a;
                shifted as char
            } else {
                c
            }

        }).collect();
    test
}

fn main() {
    let contents = fs::read_to_string("../../inputs/2016/day04.txt").expect("Should have been able to read the file");

    let pattern = Regex::new(r"([a-z\-]{1,})([0-9]{1,})\[([a-z]{5})\]").unwrap();
    let mut sector_ids = 0;
    let mut part2_id = 0;
    
    for line in contents.lines() {
        let Some(captures) = pattern.captures(line) else { continue };

        let encrypted_name: &str = captures.get(1).map_or("", |m| m.as_str());
        let checksum = captures.get(3).map_or("", |m| m.as_str());
        let sector_id = captures.get(2).map_or(0, |m| m.as_str().parse::<i32>().unwrap_or(0));
        
        let mut letter_counter: HashMap<char, usize> = HashMap::new();
        for c in encrypted_name.chars() {
            if c.is_ascii_lowercase() {
            *letter_counter.entry(c).or_insert(0) += 1;
            }
        }
        let mut letter_counts: Vec<_> = letter_counter.iter().collect();
        letter_counts.sort_by(|a, b| {
            let cmp_result = b.1.cmp(&a.1);

            if cmp_result == std::cmp::Ordering::Equal {
                a.0.cmp(&b.0) // Sortiert nach dem Buchstaben in aufsteigender Reihenfolge
            } else {
                cmp_result // Ansonsten behalte das erste Ergebnis
            }
         });
        let created_checksum: String = letter_counts.iter().take(5).map(|p| p.0).collect();
        
        if created_checksum == checksum {
            sector_ids += sector_id;
            let name = decode(encrypted_name , sector_id);
            if name.contains("north") {
                part2_id = sector_id;
            }
        }
    }
    println!("Part 1: {sector_ids}");
    println!("Part 2: {part2_id}");
}


