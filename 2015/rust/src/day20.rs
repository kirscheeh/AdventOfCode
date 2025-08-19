use std::collections::HashSet;


fn main() {
    let number_presents = 36_000_000;

    fn get_divisors(x: i32) -> Vec<i32> {
        let mut divisors = Vec::new();
        let sqrt_x = (x as f64).sqrt() as i32;
        for i in 1..=sqrt_x {
            if x % i == 0 {
                // For part 2, check if the elf (i) has delivered to less than 50 houses.
                if x / i <= 50 {
                    divisors.push(i);
                }
                if i != x / i && i <= 50 {
                    divisors.push(x / i);
                }
            }
        }
        divisors
    }

    let mut counter = 1;
    // Consider using a loop with step size or parallelization for further speedup.
    while get_divisors(counter).iter().map(|&d| d * 11).sum::<i32>() < number_presents {
        counter += 1;
    }
    println!("{counter}");
}