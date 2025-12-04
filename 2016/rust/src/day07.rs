use std::fs;
use std::fmt::format;
use regex::Regex;

extern crate regex;

fn supports_tls(ipv6:&str) -> bool {
    let pairs: Vec<String> = ipv6.chars().collect::<Vec<_>>().windows(2).filter(|t| t[0] != t[1]).map(|t| format!("{}{}", t[0], t[1])).collect();
    let rev_ipv6 = ipv6.chars().rev().collect::<String>();
         
    for half in &pairs {
        let rev_half = half.chars().rev().collect::<String>();
        let pair: String = format!("{}{}", half, rev_half);
        if rev_ipv6.contains(&pair) {
            return true;

        }
    }
        false
} 

fn main() {
    let contents = fs::read_to_string("../../inputs/2016/day07.txt").expect("Should have been able to read the file");
    let splitter = Regex::new(r"([a-z]{4,})\[([a-z]{1,})\]([a-z]{1,})").unwrap();
    let mut valid = 0;
    for line in contents.lines() {
        let data = splitter.captures(&line).expect("That should've matched...");
        let before = data.get(1).map_or("", |m| m.as_str());
        let brackets = data.get(2).map_or("", |m| m.as_str());
        let after = data.get(3).map_or("", |m| m.as_str());
        
        if (supports_tls(before) || supports_tls(after)) && !supports_tls(brackets){
            valid+=1;
        } 
        else {
            println!("{line} {data:?}");
        }
    }
    println!("Part 1: {valid}");

}