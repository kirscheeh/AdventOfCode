use std::fs;

fn main() {
    let contents = fs::read_to_string("inputs/day02.txt")
        .expect("Should have been able to read the file");

    let mut total_squares: i32 = 0;
    let mut total_ribbon: i32 = 0;
    
    for line in contents.lines() {
        let splits: Vec<_> = line.split("x").collect();
        
        match splits.as_slice() {
            [w_str, l_str, h_str] => {
                let w: i32 = w_str.parse().unwrap(); // .unwrap() handles the result of parse which could also fail
                let l: i32 = l_str.parse().unwrap();
                let h: i32 = h_str.parse().unwrap();

                let wh = w*h;
                let wl = w*l;
                let hl = h*l;

                // wrapping paper
                let smol = wh.min(wl.min(hl));
                total_squares += smol+2*(wl+wh+hl);

                // ribbon
                let (x, y) = find_two_smallest_values(w, l, h);
                total_ribbon += 2*(x+y)+w*l*h;
            }, 
            _ => println!("empty") // should never happen, still gotta prepare for it

        }
    }
    println!("The elves need {}m² of wrapping paper.", total_squares);  
    println!("The needed ribbon is {}m long.", total_ribbon);   
}

fn find_two_smallest_values(a: i32, b: i32, c: i32) -> (i32, i32) {
    let mut values = [a, b, c]; // this seems like python
    values.sort();
    (values[0], values[1]) // I don't need a return statement if I can just ignore the ; --> that is the same
}