use std::fs;
extern crate fancy_regex;

fn three_vowels(input: &str) -> bool {
    let mut counter = 0;
    
    for vowel in vec!['a', 'e', 'i', 'o', 'u'] {
        counter += input.chars().filter(|c| *c == vowel).count();
    }
    
    return counter >= 3;
}

fn twice_in_a_row(input: &str) -> bool {
    input.chars().zip(input.chars().skip(1)).any(|(c1, c2)| c1 == c2)
    // .zip() zips the iterator with a second iterator where we skip the first letter
    // then we compare if the two iterators, that are misplaced by one, show the same character with .any()
    // maybe this would also be good with regex
    
}

fn bad_strings(input: &str) -> bool {
    for bad_string in vec!["ab", "cd", "pq", "xy"] {
        if input.contains(&bad_string) {
            return false;
        }
    }
    return true;
}

fn pair_appears_twice(input: &str) -> bool {
    let pattern = fancy_regex::Regex::new(r"([a-z][a-z]).*\1").unwrap();
    let result = pattern.is_match(input);
    assert!(result.is_ok());
    return result.unwrap();
}

fn one_letter_apart(input: &str) -> bool {
    let pattern = fancy_regex::Regex::new(r"([a-z]).\1").unwrap();
    let result = pattern.is_match(input);
    assert!(result.is_ok());
    return result.unwrap();
}

fn main() {
    let contents = fs::read_to_string("inputs/day05.txt")
        .expect("Should have been able to read the file");

    let mut ridiculous_nice_strings = 0;
    let mut nice_strings = 0;

    for line in contents.lines() {
        if three_vowels(line) & twice_in_a_row(line) & bad_strings(line) {
            ridiculous_nice_strings += 1;
        }
        if pair_appears_twice(line) & one_letter_apart(line) {
            nice_strings += 1;
        }

    }

    println!("Given the old ridiculous rules, {} strings are nice.", ridiculous_nice_strings);
    println!("If you consider the normal rules, {} strings are nice.", nice_strings)
    
}
