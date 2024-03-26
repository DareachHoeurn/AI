from search import Problem, Trial_Error, Node
from collections import deque


def convert_state_to_list(state_tuple):
    return [list(x) for x in state_tuple]


def convert_state_to_tuple(state_list):
    return tuple([tuple(x) for x in state_list])


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


class FourQueensProblem(Problem):
    def __init__(self):
        super().__init__(((0, 0, 0, 0),
                          (0, 0, 0, 0),
                          (0, 0, 0, 0),
                          (0, 0, 0, 0)))

    def actions(self, state):
        acts = []
        for i in range(4):
            for j in range(4):
                if state[i][j] == 0:
                    acts.append("o {} {}".format(i + 1, j + 1))
        return acts

    def result(self, state, action):
        i, j = int(action.split(' ')[1]) - 1, int(action.split(' ')[2]) - 1
        new_state = convert_state_to_list(state)

        for l in range(4):
            for k in range(4):
                if l == i and k == j:
                    new_state[l][k] = 1
                elif (l == i or k == j or abs(i - l) == abs(j - k)) and not (l == i and k == j):
                    new_state[l][k] = 2

        return convert_state_to_tuple(new_state)

    def goal_test(self, state):
        bool_state = convert_state_to_list(state)

        for i in range(4):
            for j in range(4):
                bool_state[i][j] = state[i][j] == 1

        return all([any(bool_state[i]) for i in range(4)])


def breadth_first_tree_search(problem):
    frontier = deque([Node(problem.initial)])
    res_path = []
    while frontier:
        node = frontier.popleft()
        res_path.append(node.state)
        if problem.goal_test(node.state):
            print(res_path)
            return node
        frontier.extend(node.expand(problem))

    return None


def breadth_first_graph_search(problem):
    frontier = deque([Node(problem.initial)])
    res_path = []
    explored = set()
    while frontier:
        node = frontier.popleft()
        res_path.append(node)
        if problem.goal_test(node.state):
            print(res_path)
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child not in frontier and child.state not in explored:
                frontier.append(child)

    return None


def depth_first_tree_search(problem):
    frontier = [Node(problem.initial)]
    res_path = []
    while frontier:
        node = frontier.pop()
        res_path.append(node)
        if problem.goal_test(node.state):
            print(res_path)
            return node
        frontier.extend(node.expand(problem))

    return None


def depth_first_graph_search(problem):
    frontier = [Node(problem.initial)]
    res_path = []
    explored = set()
    while frontier:
        node = frontier.pop()
        res_path.append(node)
        if problem.goal_test(node.state):
            print(res_path)
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
    return None

def main():
    f_queen = FourQueensProblem()

    my_state = ((0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0),
                (0, 0, 0, 0))

    print(len(f_queen.actions(my_state)))

    print_matrix(f_queen.result(my_state, "o 4 4"))

    my_goal_state = ((0, 1, 0, 0),
                     (0, 0, 0, 1),
                     (1, 0, 0, 0),
                     (0, 0, 1, 0))
    print()
    print_matrix(my_goal_state)
    print(f_queen.goal_test(my_goal_state))

    print()
    print("Trying to solve with Trial Error method")
    print(Trial_Error(f_queen))

    print()
    print("Solving with breadth first tree search")
    print(breadth_first_tree_search(f_queen))

    print()
    print("Solving with breadth first graph search")
    print(breadth_first_graph_search(f_queen))

    print()
    print("Solving with depth first tree search")
    print(depth_first_tree_search(f_queen))

    print()
    print("Solving with depth first graph search")
    print(depth_first_graph_search(f_queen))


main()