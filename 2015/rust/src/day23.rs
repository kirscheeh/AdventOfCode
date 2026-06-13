use std::fs;
use std::collections::HashSet;

extern crate regex;

fn main () {
    let contents = fs::read_to_string("../../inputs/2015/day23.txt").expect("Should have been able to read the file");

    for line in contents.lines() {
        let splits: Vec<_> = line.split(" ").collect();
}