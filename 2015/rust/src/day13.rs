use std::fs;
use itertools::Itertools;
use std::collections::{HashMap, HashSet};

extern crate regex;
extern crate itertools;


fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day13.txt").expect("Should have been able to read the file");
    let replacements = regex::Regex::new(r"(gain |lose )").unwrap();

    let content_with_number = replacements.replace_all(&contents, |captures: &regex::Captures| {
        match &captures[0] {
            "gain " => "+",
            "lose " => "-",
            _ => unreachable!(),
        }
    });

    let mut units: HashMap<(&str, &str), i32> = HashMap::new();
    let mut guests = HashSet::new();
    
    let pattern = regex::Regex::new(r"([A-Za-z]{1,}) would ([-+0-9]{2,}) happiness units by sitting next to ([A-Za-z]{1,})").unwrap();
    for line in content_with_number.lines() {
        let data = pattern.captures(&line).expect("It should find a pattern, else inspect your input.");
        
        let person_a = data.get(1).map_or("", |m| m.as_str());
        let unit = data.get(2).map_or("0", |m| m.as_str());
        let person_b = data.get(3).map_or("", |m| m.as_str());

        guests.insert(person_a);
        guests.insert(person_b);

        units.insert((person_a, person_b), unit.parse::<i32>().expect("Wrong distance, my guy"));

        if !units.contains_key(&(person_a, "ME")) {
            units.insert((person_a, "ME"), 0);
            units.insert(("ME", person_a), 0);
        }
        
    }
    
    // Part 2
    guests.insert("ME");

    let table_order = guests.iter().permutations(guests.len());
    let mut max_happiness = 0;

    for guest in table_order {
        let turn1: i32 = guest.windows(2).map(
            |pair| {
                let (left, right) = (*pair[0], *pair[1]);
                *units.get(&(left, right)).expect("Missing distance, dude")
            }
        ).sum();
        let turn2: i32 = guest.windows(2).map(
            |pair| {
                let (left, right) = (*pair[1], *pair[0]);
                *units.get(&(left, right)).expect("Missing distance, dude")
            }
        ).sum();
        let left_end = units.get(&(*guest[0], *guest[guest.len()-1])).unwrap();
        let right_end = units.get(&(*guest[guest.len()-1], *guest[0])).unwrap();

        let curr_happiness = turn1 + turn2 + left_end + right_end;
        max_happiness = max_happiness.max(curr_happiness);
    }
    println!("Maximum Happiness with Me: {}", max_happiness);

}