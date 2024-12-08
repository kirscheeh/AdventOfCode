use std::fs;
extern crate petgraph;
use petgraph::graph::{self, Graph, Node, NodeIndex};
use petgraph::algo;
use petgraph::dot::Dot;
use std::collections::HashMap;


fn main() {
    let contents = fs::read_to_string("inputs/day09.txt")
        .expect("Should have been able to read the file");

    let mut graph: Graph<&str, u32, petgraph::Undirected> = Graph::new_undirected();
    let mut node_indices: HashMap<&str, NodeIndex> = HashMap::new();

    for line in contents.lines() {
        let parts: Vec<&str> = line.split_whitespace().collect();
        let start = parts[0];
        let dest = parts[2];
        let dist: u32 = parts[4].parse::<u32>().unwrap();

        let origin = *node_indices.entry(start).or_insert_with(|| graph.add_node(start));

        // Ensure `destination` node exists in the graph and map
        let destination = *node_indices.entry(dest).or_insert_with(|| graph.add_node(dest));

        // Add the edge with the given distance
        graph.add_edge(origin, destination, dist);

    }
    println!("{}", Dot::new(&graph));
    //for (start_name, start_node) in node_indices {}
   
}

fn traveling_salesman_problem(graph: Graph<&str, u32, petgraph::Undirected>, node_dict: HashMap<&str, NodeIndex>, start_node: NodeIndex) {
    let vertices: [NodeIndex; *graph.node_count()] = node_dict.values().cloned().collect();
}
