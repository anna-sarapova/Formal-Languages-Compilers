from pprint import pprint

def union(x, y):
    """ Concatinates two strings together such that there are no duplicate characters """
    result = list(set(x + y))
    result.sort()
    return "".join(result)

def add_new_state(dfa, state):
    """ Adds new state to dfa, handling transitions """
    transition = dfa[state[0]]

    for substate in state:
        # substate represents the state broken down like: AB = "A" & "B"
        transition = tuple(union(x, y)
            # transition is the values which appear in dfa
            for x, y in zip(transition, dfa[substate]))

    dfa[state] = transition
    return dfa

def extend_dfa(dfa, temp_list, current_state):
    """ Extends dfa and temporary list (temp_list) based on current_state """
    # Check if new states appear
    for state in dfa.get(current_state, ()):
        if not state:
            continue
        # if state is not null, function will continue

        if state not in dfa:
            # Add new states in temp_list
            temp_list.append(state)

            # Add new states in dfa
            dfa = add_new_state(dfa, state)

    return dfa, temp_list

def NFA_to_DFA(nfa):
    """ Transforms the given NFA into a DFA """

    # Initialize DFA; Initialize queue;
    dfa = nfa
    temp_list = list(dfa)

    # While new states in queue
    while temp_list:
        # print(f"temp_list: {temp_list}\n")
        current_state = temp_list.pop(0)
        # Extend current state
        # Add new states in queue
        # Add new states/ transitions in DFA
        dfa, temp_list = extend_dfa(dfa, temp_list, current_state)
    return dfa


NFA = {
    "A": ("B", "C", ""),
    "B": ("D", "C", ""),
    "C": ("", "", "AD"),
    "D": ("", "", ""),
}

DFA = NFA_to_DFA(NFA)
pprint(DFA)

