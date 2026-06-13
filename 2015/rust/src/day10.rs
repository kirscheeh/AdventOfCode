fn process_string(puzzle:String) -> String {
    let mut result: String = String::new();
    let mut previous = puzzle.chars().nth(0).unwrap();

    let mut occ_counter = 1;
    
    for c in puzzle[1..].chars() {

        if c == previous {
            occ_counter += 1;  
        }
        else {

            result += &occ_counter.to_string();
            result += &previous.to_string();

            previous = c;
            occ_counter = 1;

        }  
    }
    result += &occ_counter.to_string();
    result += &previous.to_string();
    return result;
    }

fn main() {
    let mut puzzle = String::from("1113222113");
    
    for _ in 0..50 {
        puzzle = process_string(puzzle);
    
}
println!("{}", puzzle.len());
 }