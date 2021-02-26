import sys

from feature_extraction import process_file, generate_result_and_log_writer

def main():

    # Take a file and an email from the command line
    filename = sys.argv[1]
    email = sys.argv[2]

    # generate result and log writer
    result_writer, log_writer = generate_result_and_log_writer()

    # call function process_file
    seq_no = process_file(filename, result_file_writer_obj=result_writer, log_file_writer_obj=log_writer, seq_no=1)
    # generate the file
    print(seq_no)


if __name__ == "__main__":
    main()