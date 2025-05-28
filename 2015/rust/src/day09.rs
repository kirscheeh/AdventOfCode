use std::fs;
use std::collections::{HashMap, HashSet};
use itertools::Itertools;

extern crate itertools;
extern crate regex;

fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day09.txt")
        .expect("Should have been able to read the file");

    let pattern = regex::Regex::new(r"([A-Za-z]{1,}) to ([A-Za-z]{1,}) = ([0-9]{1,})").unwrap();
    
    let mut distances: HashMap<(&str, &str), i32> = HashMap::new();
    let mut cities = HashSet::new();
    
    for line in contents.lines() {
        let data = pattern.captures(&line).expect("It should find a pattern, else inspect your input.");
        
        let city1 = data.get(1).map_or("", |m| m.as_str());
        let city2 = data.get(2).map_or("", |m| m.as_str());
        let distance = data.get(3).map_or("0", |m| m.as_str());
        
        distances.insert((city1, city2), distance.parse::<i32>().expect("Wrong distance, my guy"));
        distances.insert((city2, city1), distance.parse::<i32>().expect("Wrong distance, my guy"));
        
        cities.insert(city1);
        cities.insert(city2);
    }

    let mut minimal_distance:i32 = distances.values().sum();
    let mut maximal_distance = 0;

    for townchain in cities.iter().permutations(cities.len()) {
        /* kinda pythonic
        let mut tmp_dist = 0;
        for (index, city) in townchain[..townchain.len() - 1].to_vec().into_iter().enumerate() {
            let key = &(*city, *townchain[index+1]);
            
            match distances.get(key) {
                Some(dist) => tmp_dist+=dist,
                None => println!("This should not happen") 
            } 
        }
        */
        let tmp_dist = townchain.windows(2).map(
                |pair| {
                    let (from, to) = (*pair[0], *pair[1]);
                    *distances.get(&(from, to)).expect("Missing distance, dude")  
                }).sum();

        maximal_distance = maximal_distance.max(tmp_dist);
        minimal_distance = minimal_distance.min(tmp_dist)

    }
    println!("Maximal: {maximal_distance}, Minimal: {minimal_distance}");

}