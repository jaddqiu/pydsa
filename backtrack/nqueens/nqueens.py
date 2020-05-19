import copy
def check(res=[]):
    length = len(res)
    for i in range(length):
        for k in range(i+1, length):
            if res[i]+i == res[k]+k or res[i] - i == res[k] - k or res[i] == res[k]:
                return False
    return True

def nqueen(n):
    numbers = range(1,n+1)
    track = []
    res = []
    backtrack(numbers, track, res)
    return res

def backtrack(numbers=[], track=[], res=[]):

    for i in range(len(numbers)):
        track.append(numbers[i])
        if check(track):
            if len(track)==len(numbers):
                res.append(copy.copy(track))
            else:
                backtrack(numbers, track, res)
        track.pop()

if __name__ == '__main__':
    n = 8
    res=nqueen(n)
    print("There are total  {} nqueens solution when n is {}".format(len(res), n))
    print("Solutions are:")
    print(res)
