extern crate fancy_regex;
use std::fs;

fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day12.txt").expect("Should have been able to read the file");

    let pattern = fancy_regex::Regex::new(r"-?\d+").unwrap();
    let sum: i32 = pattern
        .find_iter(&contents)
        .filter_map(|m| m.ok().and_then(|mat| mat.as_str().parse::<i32>().ok()))
        .sum();
    println!("Part 1: {}", sum);
    // \{["a-z,+":0-9\[\]]{1,}red["a-z,+":0-9\[\]]{1,}\}
    let pattern = fancy_regex::Regex::new(r#"{[a-z0-9\[\],+:\"]+:\"red\"[a-z0-9\[\],+:\"]+}"#).unwrap();
    let bad_strings: Vec<String> = pattern
        .find_iter(&contents)
        .filter_map(|m| m.ok().map(|mat| mat.as_str().to_string()))
        .collect();
    println!("{:?}", bad_strings);
    let pattern = fancy_regex::Regex::new(r"-?\d+").unwrap();
    let sum2: i32 = pattern
        .find_iter(&bad_strings.join(" "))
        .filter_map(|m| m.ok().and_then(|mat| mat.as_str().parse::<i32>().ok()))
        .sum();
    println!("Without red {}", sum-sum2);
}