from typing import List

class Agent:
    def __init__(self, _values, tag):
        self.values = _values
        self.tag = tag
    def value(self, option: int) -> float:
        return self.values[option]

def vcg (agents: List[Agent], num_options: int) :
    #find chosen choice
    options_values: List[float] = []
    for op in range(num_options):
        options_values.append(0.0)
        for agent in agents:
            options_values[op] += agent.value(op)
    chosen = find_max(options_values) #returns the index op the max value
    print("The chosen option is: ", chosen)

    #find agent's pay
    for a in agents:
        max_value_without_a: float = options_values[0] - a.value(0)
        for op in range(num_options):
            value_without_a = options_values[op] - a.value(op)
            if (value_without_a > max_value_without_a):
                max_value_without_a = value_without_a
        
        chosen_value_without_a = options_values[chosen] - a.value(chosen)
        print("Agent", a.tag, "pays",  max_value_without_a - chosen_value_without_a)

def find_max(list: List[float]):
    max: int = 0
    for x in range(len(list)):
        if (list[x] > list[max]):
            max = x
    return max

if __name__ == "__main__" :
    import doctest
    doctest.testfile("test.txt",verbose=True)
