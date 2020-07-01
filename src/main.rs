

pub struct System {
    system: vec!(),
}

impl System {
    pub fn createNetwork(&mut self) -> i32 {
        self.system.push();
        self.system.len()
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
