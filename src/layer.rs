use crate::neuron;
use crate::connection;

pub struct Layer {
    neurons: Vec<neuron::Neuron>,
    connections: Vec<connection::Connection>,
}


pub fn create() -> Layer {
    Layer {
        neurons: vec!(),
        connections: vec!(),
    }
}

impl Layer {
}
