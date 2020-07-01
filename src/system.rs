use crate::network;
use crate::layer;

pub struct System {
    networks: Vec<network::Network>,
}

pub fn create() -> System {
    System {
        networks: vec!(),
    }
}

impl System {
    pub fn create_network(&mut self) -> usize {
        self.networks.push(network::create());
        self.networks.len() - 1
    }
    pub fn create_layer(&mut self, net: usize) -> usize {
        self.networks[net].add_layer(layer::create())
    }
}
