extern crate fancy_regex;
use std::fs;

fn main() {
    let contents = fs::read_to_string("inputs/day12.txt").expect("Should have been able to read the file");

    let pattern = fancy_regex::Regex::new(r"-?[0-9]{1,}").unwrap();
    let sumup_all = pattern.find_iter(&contents).map(|x| x.unwrap().as_str().parse::<i32>().unwrap()).collect::<Vec<_>>();
    println!("{}", sumup_all.iter().sum::<i32>());

    let json: serde_json::Value = serde_json::from_reader(fs::File::open("inputs/day12.txt").expect("file should open read only")).expect("file should be proper JSON");

    for (key, value) in json.as_object().unwrap() {
        println!("{} {}",key, value)
    }


}
//    