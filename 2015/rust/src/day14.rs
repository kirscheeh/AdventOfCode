use std::fs;
use std::collections::HashMap;

extern crate regex;

fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day14.txt").expect("Should have been able to read the file");
    let pattern = regex::Regex::new(r"([A-za-z]{1,}) can fly ([0-9]{1,}) km\/s for ([0-9]{1,}) seconds, but then must rest for ([0-9]{1,}) seconds").unwrap();

    let mut reindeer_info = HashMap::new();
    let mut kilometers = HashMap::new();
    let mut scores = HashMap::new();

    for line in contents.lines() {
        let data = pattern.captures(&line).expect("It should find a pattern, else inspect your input.");

        let reindeer = data.get(1).map_or("", |m| m.as_str()).to_string();
        let speed: i32 = data.get(2).map_or("0", |m| m.as_str()).parse().unwrap();
        let duration: i32 = data.get(3).map_or("0", |m| m.as_str()).parse().unwrap();
        let rest: i32 = data.get(4).map_or("0", |m| m.as_str()).parse().unwrap();

        reindeer_info.insert(reindeer.clone(), (speed, duration, rest));
        kilometers.insert(reindeer.clone(), (0, true, duration));
        scores.insert(reindeer, 0);
    }

    for i in (1..1000).rev() {
        let max_dist = kilometers.values().map(|(distance, _, _)| *distance).max().unwrap();
        for (reindeer, (speed, duration, rest)) in &reindeer_info {
            let entry = kilometers.get_mut(reindeer).unwrap();

            if entry.1 {
                entry.0 += *speed;
                entry.2 -= 1;
            } else {
                entry.2 -= 1;
            }
            if entry.2 == 0 {
                if entry.1 {
                    entry.2 = *rest;
                } else {
                    entry.2 = *duration;
                }
                entry.1 = !entry.1;
            }
             if entry.0 == max_dist {
                *scores.get_mut(reindeer).unwrap() += 1;
            }
        }

    }
    let max_distance = kilometers.values().map(|(distance, _, _)| distance).max().unwrap();

    println!("Max distance: {}", max_distance);
    println!("Highest Score: {:?}", scores);
}