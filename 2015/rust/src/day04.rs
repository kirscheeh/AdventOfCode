//use std::fs;
extern crate md5;

fn main() {
    let input = "yzbqklnj";
    
    let mut counter = 0;
    let mut current = format!("{}{}", input, counter);
    let mut first_occurence = true;

    loop {

        let digest = md5::compute(&current);
        
        let md5sum = format!("{:x}", digest);
        
        if md5sum.starts_with("00000") & first_occurence {
            println!("Fize zeroes in the has are achieved at {} with {}.", counter, md5sum);
            first_occurence = false;
        } else if md5sum.starts_with("000000") {
            println!("Six zeroes in the has are achieved at {} with {}.", counter, md5sum);
            break;
        }
        counter += 1;
        
        current = format!("{}{}", input, counter);

        
    }
}