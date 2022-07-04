from enum import Enum
import copy


def main():
    print(goalTest(goalState))
    acts = actions(goalState)

    nexts = results(goalState, acts)
    for i in range(len(nexts)):
        for idx in range(len(nexts[i])):
            print(nexts[i][idx])
        print()


Actions = Enum("Actions", "up down left right")

goalState = [
    ['1', '2', '3', '4'],
    ['5', '6', '7', '8'],
    ['9', '10', '11', '12'],
    ['13', '14', '15', 'E']
]


def goalTest(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == goalState[i][j]:
                continue
            else:
                return False
    return True


def results(s, acts):
    results = []
    for a in range(len(acts)):
        idx, jdx = 0, 0
        cp = copy.deepcopy(s)
        for i in range(len(cp)):
            for j in range(len(cp[i])):
                if cp[i][j] == 'E':
                    idx = i
                    jdx = j
                    break
        if acts[a] == Actions.up:
            cp[idx][jdx] = cp[idx-1][jdx]
            cp[idx-1][jdx] = 'E'
        elif acts[a] == Actions.down:
            cp[idx][jdx] = cp[idx+1][jdx]
            cp[idx+1][jdx] = 'E'
        elif acts[a] == Actions.left:
            cp[idx][jdx] = cp[idx][jdx-1]
            cp[idx][jdx-1] = 'E'
        else:
            cp[idx][jdx] = cp[idx][jdx+1]
            cp[idx][jdx] = 'E'
        results.append(cp)
    return results


def actions(s):
    a = [Actions.up, Actions.down, Actions.left, Actions.right]
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == "E":
                if i == 0:
                    a.remove(Actions.up)
                elif i == 3:
                    a.remove(Actions.down)
                if j == 0:
                    a.remove(Actions.left)
                elif j == 3:
                    a.remove(Actions.right)
    return a


if __name__ == '__main__':
    main()
