use crate::layer;

pub struct Network {
    layers: Vec<layer::Layer>,
}

pub fn create() -> Network {
    Network {
        layers: vec!(),
    }
}

impl Network {
    pub fn add_layer(&mut self, layer: layer::Layer) -> usize {
        self.layers.push(layer);
        self.layers.len() - 1
    }
}
