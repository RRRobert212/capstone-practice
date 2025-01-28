#capstone2.py

#capture all unique states on plates
#count how many from each state and list in descending order

def loadToList():
    data = open(r"congestion.txt","r")
    lines = data.readlines()
    lines.pop(0)

    return lines


def states(data):
    states = []
    for l in data:
        x = l.split(',')
        states.append(x[1])
    return states

def unique_states(states):
    unique_states = []
    for s in states:
        if s not in unique_states:
            unique_states.append(s)

    unique_states.sort()
    print(unique_states)


def state_count(states):

    all = [[state, states.count(state)] for state in states]
    count_list = []
    for a in all:
        if a not in count_list:
            count_list.append(a)
    count_list.sort(reverse= True, key = lambda x: x[1])

    return count_list



def main():
    
    parsed_data = loadToList()
    state_list = states(parsed_data)
    #unique_states(state_list)
    print(state_count(state_list))

    return



if __name__ == '__main__':
    main()