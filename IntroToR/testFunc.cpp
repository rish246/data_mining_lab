/*
	Make function sum( ( x - x' ) ^ 2 ) in C
	-- the above function is R syntax
*/


#include <iostream>
#include <vector>

float findMean(std::vector<float> &values)
{
	int nValues = (int) values.size();

	float sumValues = 0.0;

	for(float &value : values)
		sumValues += value;

	return (sumValues / nValues);
}

float RFunc(std::vector<float> &values)
{
	// Find mean of values


	float meanValue = findMean(values);

	float sumValues = 0.0;
	// Substract Each value with mean and square the value
	for(float &value : values) 
	{
		value = (value - meanValue);
		value *= value;

		sumValues += value;
	}


	return sumValues;
	// Find the sum of the vector
}


int main() 
{
	std::vector<float> values = { 1.5, 4.5, 3.0 };

	float result = RFunc(values);

	std::cout << result << std::endl;
}
