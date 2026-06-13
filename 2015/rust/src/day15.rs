use std::fs;
use regex::Regex;
use itertools::Itertools;
use std::collections::HashSet;
use std::cmp::max;

extern crate itertools;
extern crate regex;

fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day15.txt").expect("Should have been able to read the file");

    let pattern = Regex::new(r"(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)").unwrap();
    let mut ingredients = Vec::<Vec<i32>>::new();
    
    for line in contents.lines() {
        if let Some(captures) = pattern.captures(line) {
            // Skip the first capture (the whole match), then map to i32
            let numbers: Vec<i32> = captures.iter()
            .skip(2) // skip 0 (whole match) and 1 (ingredient name)
            .map(|c| c.unwrap().as_str().parse::<i32>().unwrap())
            .collect();
            ingredients.push(numbers);
        }
    }
    let num_ingredients = ingredients.len();
    
    // for some reason, combinations_with_replacement worked as well but I cannot get why
    let permutations: Vec<Vec<i32>> = std::iter::repeat(0..=100)
    .take(num_ingredients)
    .multi_cartesian_product()
    .filter(|counts| counts.iter().sum::<i32>() == 100)
    .collect();
    
    let mut max_score = 0;
  
    for perm in permutations {
        let mut values = vec![0; ingredients[0].len()];
        for ingredient in 0..num_ingredients {

            for (index, property) in ingredients[ingredient].clone().into_iter().enumerate() {
                let tmp = property*perm[ingredient];

                values[index] += tmp;
            }
        }
        // part2
        if values[values.len()-1] != 500 {
            continue; 
        }

        let sum: i32 = values.iter().take(4).map(|&v| if v < 0 { 0 } else { v }).product(); 
        max_score = max(max_score, sum);

    }
    println!("{max_score}");
 
}