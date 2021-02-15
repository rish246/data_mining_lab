def calc_min_calls(input_stream) -> int:
    last_occurence = {0 : -1, 1 : -1}
    n_calls = {0 : 0, 1 : 0}

    for idx, direction in enumerate(input_stream):
        if last_occurence[direction] == -1:
            n_calls[direction] += 1
            last_occurence[direction] = idx 

        elif (idx - last_occurence[direction]) > 1:
            n_calls[direction] += 1

        last_occurence[direction] = idx

    return min(n_calls[0], n_calls[1])

def main():
    input_stream = [0,0,1,1,1,0,1,1,1,0,0,1,0]

    min_calls = calc_min_calls(input_stream)

    print(min_calls)

main()

# what happening was.. 2nd cap was not getting orders of getting flipped