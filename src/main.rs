pub enum NeuronConnection {
    Neuron(Neuron),
    Connection
}

pub struct System {
    system: Vec<Vec<Vec<Vec<NeuronConnection>>>>,
}

impl System {
    pub fn create_network(&mut self) -> usize {
        self.system.push(vec!(vec!(vec!(),vec!())));
        self.system.len() - 1
    }
    pub fn create_layer(&mut self, net: usize) -> usize {
        self.system[net].push(vec!(vec!(),vec!()));
        self.system[net].len() - 1
    }
}

pub enum NeuronIO {
    Input,
    None,
    Output
}

pub struct Neuron {
    ntype: i16,
    IO: NeuronIO,
}

fn main() {
    println!("Hello, world!");
}
