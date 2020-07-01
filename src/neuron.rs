pub enum NeuronIO {
    Input,
    None,
    Output,
}

pub struct Neuron {
    ntype: i16,
    io: NeuronIO,
}

