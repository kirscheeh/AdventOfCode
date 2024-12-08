
extern crate fancy_regex;
fn main() {
    let input: String = String::from("aabb");

   println!("{}", has_two_real_pairs(input));

}

fn _increase_password(_password:String) -> String {
    return String::new();
}

fn _has_increasing_straignt(_password:String) -> bool {
    false
}

fn _contains_forbidden_letters(password:String) -> bool {
    if password.contains("i") || password.contains("o") || password.contains("l") {
        return false;
    }
    return true;
}

fn has_two_real_pairs(password:String) -> bool {
    let pattern = fancy_regex::Regex::new(r"([a-z])\1").unwrap();
    let result = pattern.captures_iter(&password);
    println!("{:?}", result);
    return false;
}