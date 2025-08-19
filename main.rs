
fn main() {
    let mut localisation: Vec<(i32, i32)> = Vec::new();
    let start_pos = (0,0);
    let steps = 12;

    for x in start_pos.0..start_pos.0+steps {
        localisation.push((x, start_pos.1));
    }
    println!("{:?}", localisation);
}

