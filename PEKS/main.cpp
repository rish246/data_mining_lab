/*
 * main.c
 *
 *  Created on: Jul 7, 2015
 *      Author: mahind
 */

#include <iostream>
#include <vector>

#include "peks.hpp"

//#define DEBUG 1
// #define TEST 2

struct testcase
{
	const char *_word_one;
	const char *_word_two;
	int _result;

	testcase() {}

	testcase(const char *word_one, const char *word_two, int result)
		: _word_one(word_one), _word_two(word_two), _result(result) {}
};

bool are_same(const std::string &first, const std::string &second)
{
	return first == second;
}

std::vector<testcase> generate_testcases(int n_tests)
{
	const char *first_words[20] = {"hello", "Hello", "World", "stkksklkdjfksldjf", "stkksklkdjfksldjf"};
	const char *second_words[20] = {"hello", "hello", "World", "stkksklkdjfksldjf", "tkksklkdjfksldjf"};

	std::vector<testcase> test_cases(n_tests);

	for (int i = 0; i < n_tests; i++)
	{
		int cur_result = are_same(first_words[i], second_words[i]);
		test_cases[i] = testcase(first_words[i], second_words[i], cur_result);
	}

	return test_cases;
}

void test()
{
	// We make 20 strings and test our function on that
	int passed_tests = 0;

	int n_test_cases = 5;

	std::vector<testcase> test_cases = generate_testcases(n_test_cases);

	for (testcase test : test_cases)
	{
		int cur_res = peks_scheme((char *)test._word_one, (char *)test._word_two); // peks_scheme (our own)

		passed_tests += (cur_res == test._result);
	}

	std::cout << passed_tests << " test cases passed" << std::endl;
}

int main(int argc, char *argv[])
{
#ifndef TEST
	if (argc != 3)
	{
		printf("Usage: %s <word1> <word2>\n", argv[0]);
		return 1;
	}

	char *W1, *W2;
	W1 = argv[1];
	W2 = argv[2];

	int match;
	match = peks_scheme(W1, W2);

	if (match)
		printf("Equal\n");
	else
		printf("Not equal\n");
#endif

#if defined(TEST)

	test();

#endif

	return 0;
}
