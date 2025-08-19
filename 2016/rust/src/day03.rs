use std::fs;

fn main() {
    let contents = fs::read_to_string("../../inputs/2016/day03.txt")
        .expect("Should have been able to read the file");

    let mut triangle_counter = 0;
    for triangle in contents.split("\n") {
        let side_lengths: Vec<i32> = triangle.trim().split_whitespace().map(|s| s.parse::<i32>().unwrap()).collect();

        if side_lengths[0] + side_lengths[1] > side_lengths[2] && side_lengths[0] + side_lengths[2] > side_lengths[1] && side_lengths[1] + side_lengths[2] > side_lengths[0] {
            triangle_counter += 1
        }
    }
    println!("{}", triangle_counter);
}