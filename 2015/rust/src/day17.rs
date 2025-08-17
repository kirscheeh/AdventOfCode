use regex::Regex;
use itertools::Itertools;
use std::collections::HashSet;
use std::cmp::min;
use std::fs;

extern crate itertools;
extern crate regex;

fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day17.txt").expect("Should have been able to read the file");
    let mut containers = Vec::new();

    for line in contents.lines() {
        let num: i32 = line.trim().parse().expect("Not a number");
        containers.push(num);
    }
        
    let permutations: Vec<Vec<i32>> = (1..=containers.len())
        .flat_map(|k| containers.iter().cloned().combinations(k))
        .collect();
   
    let mut option_counter_all = 0;
    let mut minimum_number = usize::MAX;
    for permutation in permutations.clone() {
        if permutation.clone().into_iter().sum::<i32>() == 150 {
            option_counter_all +=1;
            
            minimum_number = min(minimum_number, permutation.len())
        }
    }
    let mut option_counter_min = 0;
    for permutation in permutations {
        if permutation.clone().into_iter().sum::<i32>() == 150 && permutation.len() == minimum_number {
            option_counter_min +=1;
            
            minimum_number = min(minimum_number, permutation.len())
        }
    }
    println!("Part 1: {option_counter_all}, Part 2: {option_counter_min}");
 
}