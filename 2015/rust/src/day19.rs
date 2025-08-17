use std::fs;
use std::collections::HashSet;

extern crate regex;

fn main () {
    let contents = fs::read_to_string("../../inputs/2015/day19.txt").expect("Should have been able to read the file");

    let mut parts = contents.splitn(2, "\n\n");
    let rules: Vec<&str> = parts.next().unwrap_or("").split('\n').collect();
    let molecule = parts.next().unwrap_or("MOLECULE");

    let mut replacements: HashSet<String> = HashSet::new();

    for rule in rules {
        let mut parts = rule.split(" => ");
        
        let pattern = parts.next().unwrap();
        let replacement = parts.next().unwrap();

        let rgx = regex::Regex::new(&format!("({})", pattern)).unwrap();

        for rgx_match in rgx.find_iter(molecule) {
            let new_molecule = format!(
                "{}{}{}",
                &molecule[..rgx_match.start()],
                replacement,
                &molecule[rgx_match.end()..]
            );
            replacements.insert(new_molecule);
        }
    }

    println!("Part 1: {}", replacements.len());

}