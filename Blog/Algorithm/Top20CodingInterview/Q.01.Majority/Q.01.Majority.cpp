#include <iostream>
#include <vector>
#include <unordered_map>
#include <exception>

class exception_noMajority : public std::exception
{
public:
	const char * what() const throw()
	{
		return "No Majority";
	}
};

int FindMajority(std::vector<int> p_nVec)
{
	size_t nMajority = p_nVec.size() / 2;

	std::unordered_map<int, int> mFind;

	for (int nElement : p_nVec)
	{
		auto it = mFind.find(nElement);
		if (it != mFind.end())
		{
			mFind.at(it->first) = it->second + 1;
			if (mFind.at(it->first) >= nMajority)
				return it->first;
		}
		else
		{
			mFind.insert(std::make_pair<int, int>(std::move(nElement), 1));
		}
	}

	throw exception_noMajority();
}

int main()
{
	try
	{
		std::cout << FindMajority({ 1,2,3,4,5,6,7,8,9,0 }) << std::endl;
	}
	catch (exception_noMajority& e)
	{
		std::cout << e.what() << std::endl;
	}

	try
	{
		std::cout << FindMajority({ 1,4,3,4,4,4,5,8,4,0 }) << std::endl;
	}
	catch (exception_noMajority& e)
	{
		std::cout << e.what() << std::endl;
	}
}

