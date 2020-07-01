class system:
    system = []

    #[net]                  [layer]  [0 / 1]                      [pointer]
    #(controlls everything) (orders) (0 - neuron, 1 - connection) (way to see what object)

    def createNet(self, net): # (self, int)
        self.system.insert(net, [[[], []]])

    def createLayer(self, net, layer): # (self, int, int)
        self.system[net].insert(layer, [[], []])
    
    def createNeuron(self, id, net, layer, index, type, IO): # (self, int, int, int, int, int, int)
        id = neuron(type, IO, id)
        self.system[net][layer][0].insert(index, id)

    def createConnection(self, id, net, layer, start, end, weight = 1): # (self, int, int, int, int, int, float)
        id = connection(start, end, weight, self)
        self.system[net][layer][1].append(id)

    def check(self):
        for x in range(0, len(self.system)):
            #net
            for x2 in range(0, len(self.system[x])):
                #layer
                for x3 in range(0, len(self.system[x][x2][0])):
                    self.system[x][x2][0][x3].check()
                for x3 in range(0, len(self.system[x][x2][1])):
                    self.system[x][x2][1][x3].check()


class neuron:
    
    value = 0
    output = 0

    def __init__(self, type, IO, name):
        self.type = type
        self.IO = IO
        self.name = name
        self.inputs = []

    def __repr__(self):
        return "<neuron type:" + str(self.type) + " IO:" + str(self.IO) + " name:" + str(self.name) + ">"

    def __str__(self):
        return self.__repr__()

    def __truediv__(self, other):
        raise Exception("YES.")

    def check(self):
        #get input
        
        self.value = sum(self.inputs)
        self.inputs = []
        if self.IO == -1:
            self.value = int(input('input for neuron ' + str(self.name) + ': '))

        #transform inputs

        if self.type == 0:
            self.output = self.value
        elif self.type == 1:
            if self.value > 0:
                self.output = self.value
            else:
                self.output = 0
        elif self.type == 2:
            if self.value >= 1:
                self.output = 1
            else:
                self.output = 0
        elif self.type == 3:
            if self.value >= 1:
                self.output = 1
            elif self.value <= -1:
                self.output = 1
            else:
                self.output = 0

        if self.IO == 1:
            print(self.output)


class connection:
    
    def __init__(self, start, end, weight, sys):
        self.start = start
        self.end = end
        self.weight = weight
        self.sys = sys

        for x in range(0, len(sys.system)):
            #net
            for x2 in range(0, len(sys.system[x])):
                #layer
                for x3 in range(0, len(sys.system[x][x2][0])):
                    #index
                    if self.sys.system[x][x2][0][x3].name == self.start:
                        self.startNet = x
                        self.startLayer = x2
                        self.startIndex = x3
                    elif self.sys.system[x][x2][0][x3].name == self.end:
                        self.endNet = x
                        self.endLayer = x2
                        self.endIndex = x3
    
    def check(self):
        if not (self.start == self.sys.system[self.startNet][self.startLayer][0][self.startIndex] and self.end == self.sys.system[self.endNet][self.endLayer][0][self.endIndex]):
            for x in range(0, len(sys.system)):
                #net
                for x2 in range(0, len(sys.system[x])):
                    #layer
                    for x3 in range(0, len(sys.system[x][x2][0])):
                        #index
                        if self.sys.system[x][x2][0][x3].name == self.start:
                            self.startNet = x
                            self.startLayer = x2
                            self.startIndex = x3
                        elif self.sys.system[x][x2][0][x3].name == self.end:
                            self.endNet = x
                            self.endLayer = x2
                            self.endIndex = x3
        
        self.sys.system[self.endIndex][self.endLayer][0][self.endIndex].inputs.append(self.sys.system[self.startNet][self.startLayer][0][self.startIndex].output * self.weight)
                            
    
    def __repr__(self):
        return "<connection start:" + str(self.start) + " end:" + str(self.end) + " weight:" + str(self.weight) + ">"

    def __str__(self):
        return self.__repr__()

sys = system()
sys.createNet(0)
sys.createLayer(0, 0)
sys.createNeuron(1, 0, 0, 0, 0, -1)
sys.createLayer(0, 1)
sys.createNeuron(2, 0, 1, 0, 0, 0)
sys.createConnection(1, 0, 0, 1, 2, 1)
sys.createLayer(0, 2)
sys.createNeuron(3, 0, 2, 0, 0, 1)
sys.createConnection(2, 0, 1, 2, 3, 1)

#0->0->0
#I  N  O

print(sys.system[0][0][0][0].name)

print(sys.system)

for x in range(0, 5):
    sys.check()