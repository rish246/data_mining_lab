'''
Command line implementation of the TOPSIS algorithm

Author: Rishabh Katna
'''
def merge_matrix_and_scores(test_matrix1, n_rows, performance_score, ranks):
    
    for row in range(n_rows):
    
        test_matrix1[row] = test_matrix1[row] + [performance_score[row], ranks[row]]


def get_ranks(performance_score):

    performance_score_copy = performance_score.copy()

    performance_score_copy.sort(reverse=True)

    score_to_rank = {}

    for rank, score in enumerate(performance_score_copy):
        score_to_rank[score] = rank + 1

    ranks = [score_to_rank[r] for r in performance_score]

    return ranks

def get_performance_score(euclidean_dist_best, euclidean_dist_worst, n_rows):
    performance_score = [0 for _ in range(n_rows)]

    for row in range(n_rows):

        performance_score[row] = (euclidean_dist_worst[row] / (euclidean_dist_best[row] + euclidean_dist_worst[row]))

    return performance_score


def get_euclidean_dists(test_matrix1, ideal_best_values_for_cols, ideal_worst_values_for_cols, n_rows, n_cols):
    euclidean_dist_best = [0 for _ in range(n_rows)]

    euclidean_dist_worst = [0 for _ in range(n_rows)]

    for row in range(n_rows):

        for col in range(n_cols):

            euclidean_dist_best[row] += (test_matrix1[row][col] - ideal_best_values_for_cols[col]) ** 2

            euclidean_dist_worst[row] += (test_matrix1[row][col] - ideal_worst_values_for_cols[col]) ** 2


    euclidean_dist_best = [(val ** 0.5) for val in euclidean_dist_best]

    euclidean_dist_worst = [(val ** 0.5) for val in euclidean_dist_worst]

    return euclidean_dist_best, euclidean_dist_worst



def get_ideal_values(test_matrix1, actions, n_rows, n_cols):
    ideal_best_values_for_cols = [0 for _ in range(n_cols)]

    ideal_worst_values_for_cols = [0 for _ in range(n_cols)]

    def get_best_val_func(action):

        return max if (action == '+') else min

    def get_worst_val_func(action):

        return max if (action == '-') else min


    for col in range(n_cols):

        jth_col = [test_matrix1[row][col] for row in range(n_rows)]


        # get the ideal best result of the column
        best_val_func = get_best_val_func(actions[col])

        result_best = best_val_func(jth_col)

        ideal_best_values_for_cols[col] = result_best


        # get the ideal worst result of the column
        worst_val_func = get_worst_val_func(actions[col])

        result_worst = worst_val_func(jth_col)

        ideal_worst_values_for_cols[col] = result_worst

    
    return ideal_best_values_for_cols, ideal_worst_values_for_cols


def normalize_matrix(test_matrix1, n_rows, n_cols, rms_values_cols, weights):
    for row in range(n_rows):
        
        for col in range(n_cols):
            ## use the rms_values to normalize matrix
            test_matrix1[row][col] /= rms_values_cols[col]

            # multiply the matrix with weight of each col
            test_matrix1[row][col] *= weights[col]


def get_rms_for_cols(test_matrix1, n_rows, n_cols):
    
    rms_values_cols = [0 for _ in range(n_cols)]
    
    for col in range(n_cols):
    
        for row in range(n_rows):
    
            rms_values_cols[col] += (test_matrix1[row][col] ** 2)
    
    rms_values_cols = [(val ** 0.5) for val in rms_values_cols]
    
    return rms_values_cols

def apply_TOPSIS(test_matrix1, weights, actions):
    ## calculate n_rows and n_cols here #######
    n_rows = len(test_matrix1)

    n_cols = len(test_matrix1[0])

    rms_values_cols = get_rms_for_cols(test_matrix1, n_rows, n_cols)

    ########################### Normalize the test matrix #############
    normalize_matrix(test_matrix1, n_rows, n_cols, rms_values_cols, weights)
    
    # get ideal best and worst values for all columns
    ideal_best_values_for_cols, ideal_worst_values_for_cols = get_ideal_values(test_matrix1, actions, n_rows, n_cols)

    # get euclidean distances of each row from ideal best cases and ideal worst values
    euclidean_dist_best, euclidean_dist_worst = get_euclidean_dists(test_matrix1, ideal_best_values_for_cols, ideal_worst_values_for_cols, n_rows, n_cols)


    performance_score = get_performance_score(euclidean_dist_best, euclidean_dist_worst, n_rows)

    ########## Find ranks ###################################3
    ranks = get_ranks(performance_score)

    merge_matrix_and_scores(test_matrix1, n_rows, performance_score, ranks)


def main():
    test_matrix1 = [
    [250, 16, 12, 5],
    [200, 16, 8, 3],
    [300, 32, 16, 4],
    [275, 32, 8, 4],
    [225, 16, 16, 2]
    ]

    weights = [0.25, 0.25, 0.25, 0.25]
    actions = ['-', '+', '+', '+']

    apply_TOPSIS(test_matrix1, weights, actions)

    for row in test_matrix1:
        print(row)





if __name__ == "__main__":
    main()