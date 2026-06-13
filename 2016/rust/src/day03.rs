use std::fs;
use itertools::Itertools;

extern crate itertools;

fn _valid_triangle(triangle:Vec<i32>) -> bool {
    return triangle[0] + triangle[1] > triangle[2] && triangle[0] + triangle[2] > triangle[1] && triangle[1] + triangle[2] > triangle[0]
}

fn count_triangles(triangles:Vec<Vec<i32>>) -> i32 {
    let mut valid_triangles = 0;
    
    for triangle in triangles {
        if _valid_triangle(triangle) {
            valid_triangles +=1;
        }
    }
    valid_triangles
}

fn part1(lines: &Vec<&str>, mut triangles:Vec<Vec<i32>>) -> Vec<Vec<i32>>  {
    
    let mut triangle_index = 0;
    for line in lines {
        let triangle: Vec<i32> = line.trim().split_whitespace().map(|s| s.parse::<i32>().unwrap()).collect();
        triangles[triangle_index] = triangle;
        triangle_index+=1;
    }

    triangles
}

fn part2(lines: &Vec<&str>, mut triangles: Vec<Vec<i32>>) -> Vec<Vec<i32>>  {
    let mut triangle_index=0;

    let mut lines = lines.iter(); // without collect, i cannot define the type in a nice manner, but I could use next; with collect i cannot iterate without explicitly stating its an iterator

    while let Some((line1, line2, line3)) = lines.next_tuple() {

        let row_parsing = |line: &&str | {
            line.trim()
            .split_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>()
        };
        
        let row1 = row_parsing(line1);
        let row2 = row_parsing(line2);
        let row3 = row_parsing(line3);
       
        triangles[triangle_index] =  vec![row1[0], row2[0], row3[0]];
        triangles[triangle_index+1] = vec![row1[1], row2[1], row3[1]];
        triangles[triangle_index+2] = vec![row1[2], row2[2], row3[2]];

        triangle_index += 3;
    }
    triangles
}

fn main() {

    let contents = fs::read_to_string("../../inputs/2016/day03.txt")
        .expect("Should have been able to read the file");

    let mut lines: Vec<&str> = contents.split("\n").collect();

    let line_number  = lines.len();

    let mut triangles: Vec<Vec<i32>> = vec![vec![0;3]; line_number];
    let mut triangle_index=0;
    
    let p1_triangles = part1(&lines, triangles.clone());
    let p2_triangles = part2(&lines, triangles.clone());

    println!("Part 1: {}\nPart 2: {}", count_triangles(p1_triangles), count_triangles(p2_triangles));
}