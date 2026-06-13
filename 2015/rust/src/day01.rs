use std::fs;

fn main() {
    let contents = fs::read_to_string("inputs/2015/day01.txt")
        .expect("Should have been able to read the file");

    let up_floors = contents.chars().filter(|c| *c == '(').count();
    let down_floors =  contents.chars().filter(|c| *c == ')').count();
    // .chars() returns iterator over the characters of my string
    // .filter() filters iterator based on condition
    // |c| is similar to lambda function; c is each character in iterator
    // *c is a dereference and here not strictly used as c is not a reference anyway but a character already; after that I cannot use c anymore in the code as the ownership has transferred
    // .count() counts the elements in the iterator that passed filtering

    println!("The result to part 1 is {} floors.", up_floors-down_floors);

    let mut position = 0;
    let mut floor = 0;
    
    for c in contents.chars() {
        if c == '(' {
            floor += 1;
        } else {
            floor -= 1;
        }
        position += 1;
        if floor == -1 {
            println!("The result of part 2 is position {}.", position);
            break;
        }
    }
}