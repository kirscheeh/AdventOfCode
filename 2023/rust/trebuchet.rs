use std::fs;
use regex::Regex;

fn main () {
    let hay = fs::read_to_string("inputs/2023/trebuchet.txt").expect("You should be able to do this!");

    let re = Regex::new(r"(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))").unwrap();

    let mut results = vec![];
    for (_, [path, lineno, line]) in re.captures_iter(hay).map(|c| c.extract()) {
        results.push((path, lineno.parse::<u64>()?, line));
    }
    
}