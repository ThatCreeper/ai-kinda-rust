pub struct System {
    networks: Vec<Network>,
}

impl System {
    pub fn create() -> System {
        System {
            networks: vec!(),
        }
    }

    pub fn create_network(&mut self) -> usize {
        self.networks.push(Network.create());
        self.networks.len() - 1
    }
    pub fn create_layer(&mut self, net: usize) -> usize {
        self.networks[net].layers.push(Layer.create());
        self.networks[net].layers.len() - 1
    }
}

pub struct Network {
    layers: Vec<Layer>,
}

impl Network {
    pub fn create() -> Network {
        Network {
            layers: vec!(),
        }
    }
}

pub struct Layer {
    neurons: Vec<Neuron>,
    connections: Vec<Connection>,
}

impl Layer {
    pub fn create() -> Layer {
        Layer {
            neurons: vec!(),
            connections: vec!(),
        }
    }
}

pub enum NeuronIO {
    Input,
    None,
    Output,
}

pub struct Neuron {
    ntype: i16,
    io: NeuronIO,
}

pub struct Connection {
    // placeholder
}

fn main() {
    println!("Hello, world!");
}
