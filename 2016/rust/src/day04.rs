use std::fs;
use regex::Regex;
use std::collections::HashMap;

extern crate regex;

fn main() {
    let contents = fs::read_to_string("../../inputs/2016/day04.txt").expect("Should have been able to read the file");

    let pattern = Regex::new(r"([a-z\-]{1,})([0-9]{1,})\[([a-z]{5})\]").unwrap();
    let mut sector_ids = 0;

    for line in contents.split("\n") {
        let Some(captures) = pattern.captures(line) else { println!("nah"); return; };

        let encrypted_name: &str = captures.get(1).map_or("", |m| m.as_str());
        let checksum = captures.get(3).map_or("", |m| m.as_str());
        let sector_id = captures.get(2).map_or(0, |m| m.as_str().parse::<i32>().unwrap_or(0));
        
        println!("{:?}", encrypted_name);

        let mut letter_counter: HashMap<char, usize> = HashMap::new();


        for character in checksum.chars() {
            // count occurences as long as they differ in length
            let curr_occurence = encrypted_name.split("").filter(|n| *n == character.to_string()).count();
            letter_counter.insert(character, curr_occurence);
        }
        let mut count_vec: Vec<_> = letter_counter.iter().collect();

        count_vec.sort_by(|a, b| {
            let cmp_result = b.1.cmp(&a.1);

            if cmp_result == std::cmp::Ordering::Equal {
                a.0.cmp(&b.0) // Sortiert nach dem Buchstaben in aufsteigender Reihenfolge
            } else {
                cmp_result // Ansonsten behalte das erste Ergebnis
            }
         });
        let created_checksum: String = count_vec.iter().map(|p| p.0).collect();
        if created_checksum == checksum {
            sector_ids += sector_id;
        }

    println!("{sector_ids}");
    // 411182 too hiht
    }
}