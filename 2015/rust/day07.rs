use std::fs;
use std::collections::HashMap;

// for part 2, simply add the solution of part a as value for b

fn main() {
    let contents = fs::read_to_string("inputs/day07.txt")
        .expect("Should have been able to read the file");

    let lines: Vec<&str> = contents.lines().collect();

    let mut data: HashMap<String, String> = HashMap::new();
    let mut results: HashMap<String, i32> = HashMap::new();
    
    
    for line in lines {
        let parts:Vec<&str> = line.split(" -> ").collect();

        match parts[0].parse::<i32>() {
            Ok(value) => {
                data.insert(parts[1].to_string(), value.to_string());
                results.insert(parts[1].to_string(), value);
            }
            Err(_) => {data.insert(parts[1].to_string(), parts[0].to_string());}
        }
    }
    loop {
        for (key, value) in data.clone().iter() {
            if let Ok(num) = value.parse::<i32>() {
                if !results.contains_key(key) {
                    results.insert(key.clone(), num);
                }
            }

            else {
                let equation: Vec<&str> = value.split_whitespace().collect();
                
                if equation.len() == 1 {
                    if let Some(&num) = results.get(equation[0]) {
                        results.insert(key.clone(), num);
                    }
                    continue;
                }
                match equation[1] {
                    "AND" => {
                        if results.contains_key(equation[0]){
                            data.insert(key.clone(), data[key].replace(equation[0], &results[equation[0]].to_string()));
                        }

                        if results.contains_key(equation[2]){
                            data.insert(key.clone(), data[key].replace(equation[2], &results[equation[2]].to_string()));
                        }
                        match equation[0].parse::<i32>() {
                            Ok(tmp1) => {
                                match equation[2].parse::<i32>() {
                                    Ok(tmp2) => {results.insert(key.clone(), tmp1 & tmp2);}
                                    Err(_) => {continue;}
                                }
                            }, 
                            Err(_) => continue
                        }
                    }
                    "OR" => {
                        if results.contains_key(equation[0]){
                            data.insert(key.clone(), data[key].replace(equation[0], &results[equation[0]].to_string()));
                        }

                        if results.contains_key(equation[2]){
                            data.insert(key.clone(), data[key].replace(equation[2], &results[equation[2]].to_string()));
                        }
                        match equation[0].parse::<i32>() {
                            Ok(tmp1) => {
                                match equation[2].parse::<i32>() {
                                    Ok(tmp2) => {results.insert(key.clone(), tmp1 | tmp2);}
                                    Err(_) => {continue;}
                                }
                            }, 
                            Err(_) => continue
                        }
                    }
                    "LSHIFT" => {
                        if results.contains_key(equation[0]){
                            data.insert(key.clone(), data[key].replace(equation[0], &results[equation[0]].to_string()));
                        }

                        match equation[0].parse::<i32>() {
                            Ok(tmp1) => {
                                match equation[2].parse::<i32>() {
                                    Ok(tmp2) => {results.insert(key.clone(), tmp1 << tmp2);}
                                    Err(_) => {continue;}
                                }
                            }, 
                            Err(_) => continue
                        }
                    }
                    "RSHIFT" => {
                        if results.contains_key(equation[0]){
                            data.insert(key.clone(), data[key].replace(equation[0], &results[equation[0]].to_string()));
                        }

                        match equation[0].parse::<i32>() {
                            Ok(tmp1) => {
                                match equation[2].parse::<i32>() {
                                    Ok(tmp2) => {results.insert(key.clone(), tmp1 >> tmp2);}
                                    Err(_) => {continue;}
                                }
                            }, 
                            Err(_) => continue
                        }
                    }
                    _ => {
                        if results.contains_key(equation[1]){
                            data.insert(key.clone(), data[key].replace(equation[1], &results[equation[1]].to_string()));
                        }


                        match equation[1].parse::<i32>() {
                            Ok(tmp2) => {results.insert(key.clone(), !tmp2 & 0xFFFF);}
                            Err(_) => {continue;}
                        }
    
                        }
                }
            }
        }
        if results.contains_key("a")  {
            break;
        }

}
println!("{}", results["a"]);
}