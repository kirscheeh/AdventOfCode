use std::fs;
extern crate fancy_regex;
use std::io::{self, Write};


fn decode_string(s: &str) -> String {
    // Handle escape sequences manually
    let mut result = String::new();
    
    //let sting = s.trim_matches('"');
    let mut chars = s.chars().peekable();
    
    while let Some(c) = chars.next() {
        if c == '\\' {
            // Handle escape sequences
            if let Some(&next_char) = chars.peek() {
                match next_char {
                    '"' => {
                        result.push('"');
                        chars.next(); // skip "
                    },
                    '\\' => {
                        result.push('\\');
                        chars.next(); // skip \
                    },
                    'x' => {
                        // Handle hex escape sequences, e.g., \x41
                        chars.next(); // skip 'x'
                        let hex_value = chars.next().unwrap_or_default().to_string()
                            + &chars.next().unwrap_or_default().to_string();
                        if let Ok(_) = u8::from_str_radix(&hex_value, 16) {
                            result.push('x');
                        }
                    },
                    _ => (),
                }
            }
        } else {
            result.push(c);
        }
    }

    result
}

fn main() {
    let contents = fs::read_to_string("inputs/day08.txt") 
        .expect("Should have been able to read the file"); //

    let lines: Vec<&str> = contents.lines().collect();

    let _literal_length: usize = lines.iter().map(|x| x.len()).sum();
    let _normal_length: usize = lines.iter().map(|x| {
        let trimmed = &x[1..x.len() - 1]; // Remove the surrounding quotes
        decode_string(trimmed).len()  // Decode the string and calculate its length
    }).sum();
    

    let mut task2: i32 = 0;
    for line in lines {
        let mut buffer = Vec::new();
        writeln!(&mut buffer, "{:#?}", line).unwrap();
        let captured_output = String::from_utf8(buffer).unwrap();
        println!("{} {}", line, captured_output);
        task2 += captured_output.len() as i32 -1;
    }
    println!("{}", task2-_literal_length as i32)
}