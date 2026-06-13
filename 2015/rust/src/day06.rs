use std::fs;
extern crate fancy_regex;
fn main() {
    let contents = fs::read_to_string("inputs/day06.txt").expect("Should have been able to read the file");

    let mut matrix_simple: Vec<Vec<bool>> = vec![vec![false; 1000]; 1000];
    let mut matrix_complex: Vec<Vec<i32>> = vec![vec![0; 1000]; 1000];

    for line in contents.lines() {
        let coords: Vec<usize> = read_line(line);
        for x_coord in coords[0]..coords[2]+1 {
            for y_coord in coords[1]..coords[3]+1 {
                if line.contains("toggle") {
                    matrix_simple[x_coord][y_coord] = !matrix_simple[x_coord][y_coord];
                    matrix_complex[x_coord][y_coord] += 2;
                } else if line.contains("on") {
                    matrix_simple[x_coord][y_coord] = true;
                    matrix_complex[x_coord][y_coord] += 1;
                } else {
                    matrix_simple[x_coord][y_coord] = false;
                    matrix_complex[x_coord][y_coord] -= 1;

                    if matrix_complex[x_coord][y_coord] < 0 {
                        matrix_complex[x_coord][y_coord] = 0;
                    }
                }
            }
        }
    }

    // check how many lights are lit
    let mut counter = 0;
    let mut brightness = 0;
    for x in 0..1000 {
        for y in 0..1000 {
            if matrix_simple[x][y] {
                counter += 1;
            }
            brightness += matrix_complex[x][y]
        }
    }

    println!("Considering only the status of the ligths, {} are on.", counter);
    println!("Considering the brightness, all lamps together have a brightness of {}.", brightness);

}

fn read_line(input: &str) -> Vec<usize> {
    let re = fancy_regex::Regex::new(r"[0-9]{1,}").unwrap();
    let mut result = re.captures_iter(input);

    let x_start_group = result.next().unwrap().unwrap();
    let y_start_group = result.next().unwrap().unwrap();
    let x_stop_group = result.next().unwrap().unwrap();
    let y_stop_group = result.next().unwrap().unwrap();


    let x_start: usize =  x_start_group.get(0).unwrap().as_str().parse().unwrap();
    let y_start: usize =  y_start_group.get(0).unwrap().as_str().parse().unwrap();
    let x_stop: usize =  x_stop_group.get(0).unwrap().as_str().parse().unwrap();
    let y_stop: usize =  y_stop_group.get(0).unwrap().as_str().parse().unwrap();


    return vec![x_start, y_start, x_stop, y_stop];
}
