use std::fs;

enum SimpleKeyPad {
    One,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine
}

enum ComplexKeyPad {
    One,
    Two,
    Three,
    Four,
    Five,
    Six,
    Seven,
    Eight,
    Nine,
    A,
    B,
    C,
    D
}

impl SimpleKeyPad {
    fn move_up(&self) -> SimpleKeyPad{
        match self {
            SimpleKeyPad::One => SimpleKeyPad::One,
            SimpleKeyPad::Two => SimpleKeyPad::Two,
            SimpleKeyPad::Three => SimpleKeyPad::Three,
            SimpleKeyPad::Four => SimpleKeyPad::One,
            SimpleKeyPad::Five => SimpleKeyPad::Two,
            SimpleKeyPad::Six => SimpleKeyPad::Three,
            SimpleKeyPad::Seven => SimpleKeyPad::Four,
            SimpleKeyPad::Eight => SimpleKeyPad::Five,
            SimpleKeyPad::Nine => SimpleKeyPad::Six
        }
    }
    fn move_down(&self) -> SimpleKeyPad{
        match self {
            SimpleKeyPad::One => SimpleKeyPad::Four,
            SimpleKeyPad::Two => SimpleKeyPad::Five,
            SimpleKeyPad::Three => SimpleKeyPad::Six,
            SimpleKeyPad::Four => SimpleKeyPad::Seven,
            SimpleKeyPad::Five => SimpleKeyPad::Eight,
            SimpleKeyPad::Six => SimpleKeyPad::Nine,
            SimpleKeyPad::Seven => SimpleKeyPad::Seven,
            SimpleKeyPad::Eight => SimpleKeyPad::Eight,
            SimpleKeyPad::Nine => SimpleKeyPad::Nine
        }
    }
    fn move_left(&self) -> SimpleKeyPad{
        match self {
            SimpleKeyPad::One => SimpleKeyPad::One,
            SimpleKeyPad::Two => SimpleKeyPad::One,
            SimpleKeyPad::Three => SimpleKeyPad::Two,
            SimpleKeyPad::Four => SimpleKeyPad::Four,
            SimpleKeyPad::Five => SimpleKeyPad::Four,
            SimpleKeyPad::Six => SimpleKeyPad::Five,
            SimpleKeyPad::Seven => SimpleKeyPad::Seven,
            SimpleKeyPad::Eight => SimpleKeyPad::Seven,
            SimpleKeyPad::Nine => SimpleKeyPad::Eight
        }
    }
    fn move_right(&self) -> SimpleKeyPad{
        match self {
            SimpleKeyPad::One => SimpleKeyPad::Two,
            SimpleKeyPad::Two => SimpleKeyPad::Three,
            SimpleKeyPad::Three => SimpleKeyPad::Three,
            SimpleKeyPad::Four => SimpleKeyPad::Five,
            SimpleKeyPad::Five => SimpleKeyPad::Six,
            SimpleKeyPad::Six => SimpleKeyPad::Six,
            SimpleKeyPad::Seven => SimpleKeyPad::Eight,
            SimpleKeyPad::Eight => SimpleKeyPad::Nine,
            SimpleKeyPad::Nine => SimpleKeyPad::Nine
        }
    }
    fn translate(&self) -> i32 {
        match self {
        SimpleKeyPad::One => 1,
        SimpleKeyPad::Two => 2,
        SimpleKeyPad::Three => 3,
        SimpleKeyPad::Four => 4,
        SimpleKeyPad::Five =>5,
        SimpleKeyPad::Six => 6,
        SimpleKeyPad::Seven => 7,
        SimpleKeyPad::Eight => 8,
        SimpleKeyPad::Nine => 9}
    }
}
impl ComplexKeyPad {
    fn move_up(&self) -> ComplexKeyPad {
        match self {
            ComplexKeyPad::One => ComplexKeyPad::One,
            ComplexKeyPad::Two => ComplexKeyPad::Two,
            ComplexKeyPad::Three => ComplexKeyPad::One,
            ComplexKeyPad::Four => ComplexKeyPad::Four,
            ComplexKeyPad::Five => ComplexKeyPad::Five,
            ComplexKeyPad::Six => ComplexKeyPad::Six,
            ComplexKeyPad::Seven => ComplexKeyPad::Three,
            ComplexKeyPad::Eight => ComplexKeyPad::Four,
            ComplexKeyPad::Nine => ComplexKeyPad::Nine,
            ComplexKeyPad::A => ComplexKeyPad::Six,
            ComplexKeyPad::B => ComplexKeyPad::Seven,
            ComplexKeyPad::C => ComplexKeyPad::Eight,
            ComplexKeyPad::D => ComplexKeyPad::B,
        }
    }
    fn move_down(&self) -> ComplexKeyPad {
        match self {
            ComplexKeyPad::One => ComplexKeyPad::Three,
            ComplexKeyPad::Two => ComplexKeyPad::Six,
            ComplexKeyPad::Three => ComplexKeyPad::Seven,
            ComplexKeyPad::Four => ComplexKeyPad::Eight,
            ComplexKeyPad::Five => ComplexKeyPad::Five,
            ComplexKeyPad::Six => ComplexKeyPad::A,
            ComplexKeyPad::Seven => ComplexKeyPad::B,
            ComplexKeyPad::Eight => ComplexKeyPad::C,
            ComplexKeyPad::Nine => ComplexKeyPad::Nine,
            ComplexKeyPad::A => ComplexKeyPad::A,
            ComplexKeyPad::B => ComplexKeyPad::D,
            ComplexKeyPad::C => ComplexKeyPad::C,
            ComplexKeyPad::D => ComplexKeyPad::D,
        }
    }

    fn move_left(&self) -> ComplexKeyPad {
        match self {
            ComplexKeyPad::One => ComplexKeyPad::One,
            ComplexKeyPad::Two => ComplexKeyPad::Two,
            ComplexKeyPad::Three => ComplexKeyPad::Two,
            ComplexKeyPad::Four => ComplexKeyPad::Three,
            ComplexKeyPad::Five => ComplexKeyPad::Five,
            ComplexKeyPad::Six => ComplexKeyPad::Five,
            ComplexKeyPad::Seven => ComplexKeyPad::Six,
            ComplexKeyPad::Eight => ComplexKeyPad::Seven,
            ComplexKeyPad::Nine => ComplexKeyPad::Eight,
            ComplexKeyPad::A => ComplexKeyPad::A,
            ComplexKeyPad::B => ComplexKeyPad::A,
            ComplexKeyPad::C => ComplexKeyPad::B,
            ComplexKeyPad::D => ComplexKeyPad::D,
        }
    }

    fn move_right(&self) -> ComplexKeyPad {
        match self {
            ComplexKeyPad::One => ComplexKeyPad::One,
            ComplexKeyPad::Two => ComplexKeyPad::Three,
            ComplexKeyPad::Three => ComplexKeyPad::Four,
            ComplexKeyPad::Four => ComplexKeyPad::Four,
            ComplexKeyPad::Five => ComplexKeyPad::Six,
            ComplexKeyPad::Six => ComplexKeyPad::Seven,
            ComplexKeyPad::Seven => ComplexKeyPad::Eight,
            ComplexKeyPad::Eight => ComplexKeyPad::Nine,
            ComplexKeyPad::Nine => ComplexKeyPad::Nine,
            ComplexKeyPad::A => ComplexKeyPad::B,
            ComplexKeyPad::B => ComplexKeyPad::C,
            ComplexKeyPad::C => ComplexKeyPad::C,
            ComplexKeyPad::D => ComplexKeyPad::D,
        }
    }
    fn translate(&self) -> String {
        match self {
            ComplexKeyPad::One => "1".to_string(),
            ComplexKeyPad::Two => "2".to_string(),
            ComplexKeyPad::Three => "3".to_string(),
            ComplexKeyPad::Four =>"4".to_string(),
            ComplexKeyPad::Five => "5".to_string(),
            ComplexKeyPad::Six => "6".to_string(),
            ComplexKeyPad::Seven => "7".to_string(),
            ComplexKeyPad::Eight => "8".to_string(),
            ComplexKeyPad::Nine =>"9".to_string(),
            ComplexKeyPad::A => "A".to_string(),
            ComplexKeyPad::B => "B".to_string(),
            ComplexKeyPad::C => "C".to_string(),
            ComplexKeyPad::D => "D".to_string()}
        }
    
}
fn main() {
     let contents = fs::read_to_string("../../inputs/2016/day02.txt")
        .expect("Should have been able to read the file");

    let instructions = contents.split("\n");
    
    let mut key_presses_simple: Vec<i32> = Vec::<i32>::new();
    let mut current_position_simple = SimpleKeyPad::Five;

    let mut key_presses_complex: Vec<String> = Vec::<String>::new();
    let mut current_position_complex = ComplexKeyPad::Five;

    for instruc in instructions {
        for movement in instruc.chars() {
            current_position_simple = match movement {
                'U' => current_position_simple.move_up(),
                'D' => current_position_simple.move_down(),
                'L' => current_position_simple.move_left(),
                'R' => current_position_simple.move_right(),
                _ => panic!("unkonwn direction!")
            };

            current_position_complex = match movement {
                'U' => current_position_complex.move_up(),
                'D' => current_position_complex.move_down(),
                'L' => current_position_complex.move_left(),
                'R' => current_position_complex.move_right(),
                _ => panic!("unknown direction!")
            };
        }
        key_presses_simple.push(current_position_simple.translate());
        key_presses_complex.push(current_position_complex.translate());
    }
    let bathroom_code_simple = key_presses_simple.into_iter().map(|number| number.to_string()).collect::<String>();
    println!("Part 1: {}", bathroom_code_simple);
    println!("Part 2: {:?}", key_presses_complex.join(""));
}
