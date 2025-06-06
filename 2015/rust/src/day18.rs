use std::fs;
use std::collections::HashMap;

fn main () {
    let content = fs::read_to_string("../../inputs/2015/day18.txt").expect("Should have been able to read the file");

    let mut grid: HashMap<(usize, usize), bool> = HashMap::new();

    for (row, line) in content.lines().enumerate() {
        for (gollum, char) in line.chars().enumerate() {
            grid.insert((gollum, row), char == '#');
        }
    }
    // part 2
    grid.insert((0,0), true);
    grid.insert((0,99), true);
    grid.insert((99,99), true);
    grid.insert((99,0), true);

    for _ in 0..100 {
        let mut next_grid: HashMap<(usize, usize), bool> = HashMap::new();

        for cell in grid.clone() {
            let ((gollum, row), status) = cell;
            let neighbors = [
                (gollum.wrapping_sub(1), row.wrapping_sub(1)),
                (gollum, row.wrapping_sub(1)),
                (gollum + 1, row.wrapping_sub(1)),
                (gollum.wrapping_sub(1), row),
                (gollum + 1, row),
                (gollum.wrapping_sub(1), row + 1),
                (gollum, row + 1),
                (gollum + 1, row + 1),
            ];

            let count_on = neighbors.iter()
                .filter(|&&(nx, ny)| *grid.get(&(nx, ny)).unwrap_or(&false))
                .count();
            
            // part2
            if [(0, 99), (0,0), (99,0), (99,99)].contains(&(gollum, row)) {
                next_grid.insert((gollum, row), true);
            }
            else if status && (count_on == 2 || count_on == 3) {
                next_grid.insert((gollum, row), true);
            }
            else if !status && count_on == 3 {
                next_grid.insert((gollum, row), true);
            }
            else {
                next_grid.insert((gollum, row), false);
            }
        }

        grid = next_grid;

        
    }
    let lights_on = grid.into_iter().filter(|&(_, v)| v).count();
    println!("{lights_on}");


}