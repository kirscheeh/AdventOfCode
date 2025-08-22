extern crate md5;

fn main() {
    let content = "ugkcyxxp";
    let mut index = 0;

    let mut current = format!("{}{}", content, index);
    let mut part1 = Vec::<char>::new();
    let mut part2 = vec![' '; 8];
    println!("{:?}", part2);
    
    loop {

        let digest = md5::compute(&current);
        let md5sum = format!("{:x}", digest);
        
        if md5sum.starts_with("00000") {
            let chars:Vec<char> = md5sum.chars().collect();
            let sixth = chars[5];
            
            if part1.len() < 8 {
                part1.push(sixth);
            }

            if let Some(pos) = sixth.to_digit(10) {
                if pos < 8 && part2[pos as usize] == ' ' {
                    part2[pos as usize] = chars[6];
                    println!("{:?}", part2); // does this count as cool animation?
                }     
            } 
        }

        index += 1;
        current = format!("{}{}", content, index);

        if part2.iter().all(|&i| i != ' ') {
            break;
        }
     }
     println!("Part 1: {:?}", part1);
     println!("Part 2: {:?}", part2);
}