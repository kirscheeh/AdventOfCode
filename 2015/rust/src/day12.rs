extern crate fancy_regex;
extern crate json;
use std::fs;

fn sum_without_red(value: &json::JsonValue) -> i32 {
    match value {
        json::JsonValue::Number(n) => n.as_fixed_point_i64(0).unwrap_or(0) as i32,
        json::JsonValue::Array(arr) => arr.iter().map(sum_without_red).sum(),
        json::JsonValue::Object(obj) => {
            if obj.iter().any(|(_, v)| v == "red") {
                0
            } else {
                obj.iter().map(|(_, v)| sum_without_red(v)).sum()
            }
        }
        _ => 0,
    }
}

fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day12.txt").expect("Should have been able to read the file");

    let pattern = fancy_regex::Regex::new(r"-?\d+").unwrap();
    let sum: i32 = pattern
        .find_iter(&contents)
        .filter_map(|m| m.ok().and_then(|mat| mat.as_str().parse::<i32>().ok()))
        .sum();
    println!("Part 1: {}", sum);

    // \{["a-z,+":0-9\[\]]{1,}red["a-z,+":0-9\[\]]{1,}\}

    let contents2 = json::parse(&contents).unwrap();
    
    let sum2 = sum_without_red(&contents2);
    println!("Part 2: {}", sum2);
}