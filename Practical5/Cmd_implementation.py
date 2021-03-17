def main():
    test_matrix1 = [
    [250, 16, 12, 5],
    [200, 16, 8, 3],
    [300, 32, 16, 4],
    [275, 32, 8, 4],
    [225, 16, 16, 2]
    ]

    n_rows = 5
    n_cols = 4

    weights = [0.25, 0.25, 0.25, 0.25]
    actions = ['-', '+', '+', '+']

    ##################### Calculate RMS values #########################


    rms_values_cols = [0 for _ in range(n_cols)]

    for col in range(n_cols):

        for row in range(n_rows):

            rms_values_cols[col] += (test_matrix1[row][col] ** 2)

    rms_values_cols = [(val ** 0.5) for val in rms_values_cols]

    ########################### Normalize the test matrix #############


    for row in range(n_rows):
        
        for col in range(n_cols):
            ## use the rms_values to normalize matrix
            test_matrix1[row][col] /= rms_values_cols[col]

            # multiply the matrix with weight of each col
            test_matrix1[row][col] *= weights[col]



    ############ find the ideal best value for each column
    ideal_best_values_for_cols = [0 for _ in range(n_cols)]

    ideal_worst_values_for_cols = [0 for _ in range(n_cols)]

    def get_best_val_func(action):

        return max if (action == '+') else min

    def get_worst_val_func(action):

        return max if (action == '-') else min


    for col in range(n_cols):

        # get the function producting best result
        best_val_func = get_best_val_func(actions[col])

        worst_val_func = get_worst_val_func(actions[col])

        # apply the function to jth column
        jth_col = [test_matrix1[row][col] for row in range(n_rows)]

        result_best = best_val_func(jth_col)

        result_worst = worst_val_func(jth_col)

        # update_value_of ideal_values_for_cols[jth_col] = result
        ideal_best_values_for_cols[col] = result_best

        ideal_worst_values_for_cols[col] = result_worst


    ####### Find the ideal worst value for each column

    # ideal_worst_values_for_cols = [0 for _ in range(n_cols)]

    # def get_worst_val_func(action):

    #     return max if (action == '-') else min


    # for col in range(n_cols):

    #     # get the function producting best result
    #     worst_val_func = get_worst_val_func(actions[col])

    #     # apply the function to jth column
    #     jth_col = [test_matrix1[row][col] for row in range(n_rows)]

    #     result = worst_val_func(jth_col)

    #     # update_value_of ideal_values_for_cols[jth_col] = result
    #     ideal_worst_values_for_cols[col] = result


    ## Find euclidean dist of each row from the ideal best value

    euclidean_dist_best = [0 for _ in range(n_rows)]

    euclidean_dist_worst = [0 for _ in range(n_rows)]

    for row in range(n_rows):

        for col in range(n_cols):

            euclidean_dist_best[row] += (test_matrix1[row][col] - ideal_best_values_for_cols[col]) ** 2

            euclidean_dist_worst[row] += (test_matrix1[row][col] - ideal_worst_values_for_cols[col]) ** 2


    euclidean_dist_best = [(val ** 0.5) for val in euclidean_dist_best]

    euclidean_dist_worst = [(val ** 0.5) for val in euclidean_dist_worst]


    ########### Calculate performance score #########################

    performance_score = [0 for _ in range(n_rows)]

    for row in range(n_rows):

        performance_score[row] = (euclidean_dist_worst[row] / (euclidean_dist_best[row] + euclidean_dist_worst[row]))


    ########## Find ranks ###################################3
    performance_score_copy = performance_score.copy()

    performance_score_copy.sort(reverse=True)

    score_to_rank = {}

    for rank, score in enumerate(performance_score_copy):
        score_to_rank[score] = rank + 1

    ranks = [score_to_rank[r] for r in performance_score]

    for row in range(n_rows):

        test_matrix1[row] = test_matrix1[row] + [performance_score[row], ranks[row]]

    for row in test_matrix1:
        print(row)


if __name__ == "__main__":
    main()