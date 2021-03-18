 
'''
Command line implementation of the TOPSIS algorithm
Author: Rishabh Katna
'''
import sys

'''
Errors and exceptions
'''
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, message):
        self.message = message



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

    # merge_matrix_and_scores(test_matrix1, n_rows, performance_score, ranks)
    return performance_score, ranks


def generate_matrix(data):
    input_matrix = data[1 : ]

    input_matrix = [row.split(',') for row in input_matrix]

    input_matrix = [row[1 : ] for row in input_matrix]
    # apply float to each element of input_matrix
    for row in range(len(input_matrix)):
        
        for col in range(len(input_matrix[0])):
        
            input_matrix[row][col] = float(input_matrix[row][col])

    return input_matrix


def main():

    try:
        # check for right number of arguements
        if len(sys.argv) < 4:
            raise InputError("Please pass all the parameters through command line")


        ############## Number of arguements are correct ###########################
        ############### Now check for the validity of arguements ##################
        input_filename = sys.argv[1]

        weights = [float(val) for val in sys.argv[2].split(',')]

        impacts = sys.argv[3].split(',')

        output_filename = sys.argv[4]



        ########### Last test --> Impacts has only + - #################
        def is_valid_impact(i):
            return i in ['+', '-']

        invalid_impacts = [val for val in impacts if (not is_valid_impact(val))]

        if (len(invalid_impacts) > 0):
            raise InputError("Impacts should have values + | - ... no space before them")
        ################################################################



        input_data = open(input_filename).read().strip('\n').split('\n')

        input_data_copy = input_data.copy()

        input_matrix = generate_matrix(input_data)

        ##########3 check for columns > 3
        if len(input_matrix[0]) < 3:
            raise InputError("Input file should have more than 3 columns")


        ########### check for dimensionality of impacts, input_data and weights
        if (len(weights) != len(impacts)) or (len(weights) != len(input_matrix[0])):
            raise InputError("Weights, Impacts and Input Data should have same number of columns")


        

        # use the matrix to generate output
        performance_score, ranks = apply_TOPSIS(input_matrix, weights, impacts)
        # print(performance_score)

        input_data_copy[0] += ',Topsis Score,Ranks'

        for i in range(1, len(input_data_copy)):

            input_data_copy[i] += f',{performance_score[i-1]},{ranks[i-1]}'


        # write to the output file
        with open(output_filename, 'w') as op_file:

            for line in input_data_copy:
                op_file.write(line + '\n')
            
    except InputError as ip_err:
        print(f"Input Error : {ip_err.message}")

    except FileNotFoundError as file_err:
        print(f'File not found : ', file_err)

    except ValueError:
        print(f'Non numerical values found in data')




if __name__ == "__main__":
    main()

### this is working now #############
### Looking for some errors now #####