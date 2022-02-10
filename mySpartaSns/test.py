array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []

    # if array.length >=1 && array.length =< 100

    for comm in commands:
        i = comm[0] - 1
        j = comm[1]
        k = comm[2] - 1

        if i == j:
            new_array = array[[i]]


        else:
            new_array = array[i:j]

        new_array.sort()

        answer.append(new_array[k])
    return answer

result = solution(array, commands)

print(result)