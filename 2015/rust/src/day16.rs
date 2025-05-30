use std::fs;
use regex::Regex;

extern crate regex;
fn main() {
    let contents = fs::read_to_string("../../inputs/2015/day16.txt").expect("Should have been able to read the file");


    let cat_pattern = Regex::new(r"cats: (\d+)").unwrap();
    let tree_pattern = Regex::new(r"trees: (\d+)").unwrap();
    let pomeranians_pattern = Regex::new(r"pomeranians: (\d+)").unwrap();
    let goldfish_pattern = Regex::new(r"goldfish: (\d+)").unwrap();

    let part2 = true;

    for line in contents.lines() {
        if line.contains("children") {
            if !line.contains("children: 3") {
                continue
            }
        }
        if line.contains("cats") {
            let number_of_cats = cat_pattern.captures(&line)
            .and_then(|caps| caps.get(1))
            .and_then(|m| m.as_str().parse::<i32>().ok());
            
            if !line.contains("cats: 7") && !(part2 && !(number_of_cats <= Some(7))) {
                continue
            } 

        }
        if line.contains("trees") {
            let number_of_trees = tree_pattern.captures(&line)
            .and_then(|caps| caps.get(1))
            .and_then(|m| m.as_str().parse::<i32>().ok());
            
            if !line.contains("trees: 3") && !(part2 && !(number_of_trees <= Some(3))) {
                continue
            }

        }
        if line.contains("samoyeds") {
            if !line.contains("samoyeds: 2") {
                continue
            }
        }
        if line.contains("pomeranians") {
            let number_of_pomeranians = pomeranians_pattern.captures(&line)
            .and_then(|caps| caps.get(1))
            .and_then(|m| m.as_str().parse::<i32>().ok());
            
            if !line.contains("pomeranians: 3") && !(part2 && !(number_of_pomeranians > Some(3))) {
                continue
            }
            
        }
        if line.contains("akitas") {
            if !line.contains("akitas: 0") {
                continue
            }
        }
        if line.contains("vizslas") {
            if !line.contains("vizslas: 0") {
                continue
            }
        }
        if line.contains("goldfish") {
            let number_of_goldfish = goldfish_pattern.captures(&line)
            .and_then(|caps| caps.get(1))
            .and_then(|m| m.as_str().parse::<i32>().ok());
            
            if !line.contains("goldfish: 5") && !(part2 && !(number_of_goldfish > Some(5))) {
                continue
            } 
        }

        if line.contains("cars") {
            if !line.contains("cars: 2") {
                continue
            }
        }
        if line.contains("perfumes") {
            if !line.contains("perfumes: 1") {
                continue
            }
        }
        println!("{line}");
    }
}