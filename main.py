import sys
from queue import Queue

def panic(err: str) -> None:
    print(err, file=sys.stderr)
    exit()

class Automata:
    def __init__(self, file: str):
        self.file: str = file
        # Automata States, Inputs and Final States
        self.states: Tuple[str] = None
        self.final_states: Tuple[str] = None
        self.inputs: Tuple[str] = None

        # Transition Matrix
        self.transitions: Dict[str, Dict[str, Tuple[str]]] = {}
        self.load_from_file()

        # Current State
        self.state: Tuple[str] = None
        self.history: List[Tuple[str]] = None
        self.reset()
        # All Visited states

        

    def load_from_file(self) -> None:
        with open(self.file) as f:
            data: str = f.read().split('\n')

            # First Line has num of states and states
            self.states = tuple(x for x in data[0].split(' ')[1:] if x != '')

            # Second Line has num of final states and final states
            self.final_states =  tuple(x for x in data[1].split(' ')[1:] if x != '')

            # Third Line has num of inputs and inputs
            inputs =  list(x for x in data[2].split(' ')[1:] if x != '')
            inputs.append("lambda")
            self.inputs = tuple(inputs)

            # Fourth Line Ignore
            # Next Lines: Transitions
            for i in range(len(self.states)):
                # Split Line By # Ignoring trailing whitespace
                transitions: Tuple[str]= tuple(data[4+i].split('#'))[:-1]

                self.transitions[self.states[i]] = dict(
                    (
                        input, 
                        tuple(
                            state for state
                                in transition.split(' ')
                                if state != ''
                        )
                    ) for input,transition in zip(self.inputs, transitions))

    def closure(self, state: str) -> tuple[str]:
        states: Set[str] = set()
        notVisited: Queue = Queue(len(self.states));
        notVisited.put(state)
        
        while(not notVisited.empty()):
            s = notVisited.get()
            states.add(s)
            for t in self.transitions[s]['lambda']:
                if not t in states:
                    notVisited.put(t)
        return tuple(states)
    
    def transition(self, input: str) -> None:
        if not input in self.inputs:
            panic(f"Not a valid Input: {input}!")

        new_state: Tuple[Tuple[str]] = tuple()
        for s in self.state:
            for t in self.transitions[s][input]:
                new_state += self.closure(t)

        self.state = tuple(set(new_state))
        self.history.append(self.state)

    def reset(self) -> None:
        self.state = self.closure(self.states[0])
        self.history = [self.state]
        

    def __str__(self) -> str:
        string = f"""
            States: {self.states}
            Final States: {self.final_states}
            Inputs: {self.inputs}
            Transitions: """
        for s, values in self.transitions.items():
            string += "\n" + 2*"\t" + s + ":"
            for input, ns in values.items():
                string += "\n" + 3*"\t" + f"{input} -> {ns}"
        string += "\n\t" + f"Current State: {self.state}"
        string += "\n\t" + f"History: {self.history}"
        return string


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        panic("Not Enough Args were Passed!")
    file_path: str = sys.argv[1];
    automata: Automata = Automata(file_path)
    while(True):
        print(f"Current State: {automata.state}")
        print((f"History: {automata.history}"))
        chain = str(input("Introduce Cadena/exit/reset: "))
        match chain:
            case "exit":
                break
            case "reset":
                automata.reset()
                continue
            case other:
                chain = tuple( i for i in chain if i in automata.inputs)
                for command in chain:
                    automata.transition(command)



