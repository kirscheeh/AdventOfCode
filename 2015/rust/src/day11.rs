
extern crate fancy_regex;
fn main() {
    let input: String = String::from("hxbxwxba");
    let out1 = generate_new(&input, false);
    println!("{out1}");
    let out2 = generate_new(&out1, true);
    println!("{out2}");


}

fn increase(pw:Vec<u8>) -> Vec<u8> {
    let mut pw_inv: Vec<u8> = pw.into_iter().rev().collect();
    
    for (index, elem) in pw_inv.clone().into_iter().enumerate() {
        if elem + 1 > 122 {
            pw_inv[index] = 97;
        } else {
            pw_inv[index] = elem + 1;
            break; 
        }
    }
    pw_inv.into_iter().rev().collect()
}

fn generate_new(pw:&String, inc:bool) -> String {
    let mut pw_ascii = to_ascii_list(pw);
    if inc {
        pw_ascii = increase(pw_ascii);
    }
        
    while !(increasing_straight(&pw_ascii) & no_forbidden_letters(&pw_ascii) & two_pairs(&pw_ascii)) {
        pw_ascii = increase(pw_ascii);
    }

    to_str(pw_ascii)
}

fn to_ascii_list(password: &String) -> Vec<u8> {
    let mut pw = vec![0; password.len() as usize];
    for (index, char) in password.chars().enumerate() {
        pw[index] = char as u8
    }
   pw
}

fn to_str(password: Vec<u8>) -> String {
    let mut pw = String::new();
    for elem in password {
        pw.push(elem as char);
    }
   pw
}



fn increasing_straight(password:&Vec<u8>) -> bool {
    password.windows(3).any(|triple| {
    triple[0] + 1 == triple[1] && triple[1] + 1 == triple[2]
    })
    
}
fn no_forbidden_letters(password:&Vec<u8>) -> bool {

    if password.contains(&105) || password.contains(&108)|| password.contains(&111) {
        return false;
    }
    return true;
}

fn two_pairs(password:&Vec<u8>) -> bool {
    let mut pairs = 0;
    let mut i = 0;
    while i < password.len() - 1 {
        if password[i] == password[i + 1] {
            pairs += 1;
            i += 2; // skip the next char to avoid overlapping pairs
        } else {
            i += 1;
        }
    }
    pairs >= 2
}