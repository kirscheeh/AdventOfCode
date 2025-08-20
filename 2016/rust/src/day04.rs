use std::fs;
use regex::Regex;

extern crate regex;

fn main() {
    let contents = fs::read_to_string("../../inputs/2016/day04.txt").expect("Should have been able to read the file");

    let pattern = Regex::new(r"([a-z0-9\-]{1,})\[([a-z]{5})\]").unwrap();
    for line in contents.split("\n") {
        let Some(captures) = pattern.captures(line) else {println!("nah"); return;};

        let encrypted_name: Vec<&str> = captures.get(1).map_or("", |m| m.as_str()).split("").collect();
        let checksum = captures.get(2).map_or("", |m| m.as_str());

        let mut occurences = 0;

        for character in checksum.chars() {
            println!("{character}");
            if (let new_occurences = encrypted_name.clone().into_iter().filter(|n| *n == character.to_string()).count()) >= occurences {
                occurences = new_occurences;
            }
            
        }

    }
}