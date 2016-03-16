##Majority

Given an unsorted array which has a number in the majority (a number appears more than 50% in the array), find that number?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

정렬되지 않은 숫자배열을 받아서 Majority를 찾는 문제입니다.

- Majority : 배열 내에서 50% 이상을 차지하는 숫자

이 문제의 핵심은 List와 Map에 대한 특성을 이해하고 그것을 활용가능한지를 묻는 문제 같습니다.

각 언어별로 제가 구현한 것은 다음과 같습니다.

###C\# 

```C#
using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    private static int FindMajority(List<int> vNumbers)
    {
        int nMajority = vNumbers.Count() / 2;

        Dictionary<int, int> mExsitingNumber = new Dictionary<int, int>();

        foreach(int number in vNumbers)
        {
            if (mExsitingNumber.ContainsKey(number))
            {
                mExsitingNumber[number] += 1;
                if (mExsitingNumber[number] >= nMajority)
                {
                    return number;
                }
            }
            else
            {
                mExsitingNumber.Add(number, 1);
            }
        }

        throw new Exception("There is no Majority");
    }

    static void Main(string[] args)
    {
        List<int> vNumbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        try
        {
            int nMajority = FindMajority(vNumbers);

            System.Console.WriteLine(nRet);
        }
        catch (Exception e)
        {
            System.Console.WriteLine(e.Message);
        }

        try
        {
            System.Console.WriteLine(
                FindMajority(
                    new List<int> { 1, 2, 3, 3, 3, 3, 4, 5, 3 }));
        }
        catch (Exception e)
        {
            System.Console.WriteLine(e.ToString());
        }
    }
}
```

###C++

```C++
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

int FindMajority(std::vector<int> p_vnNumbers)
{
	size_t nMajority = p_vnNumbers.size() / 2;

	std::unordered_map<int, int> mExistingNumbers;

	for (int nNumber : p_vnNumbers)
	{
		auto it = mExistingNumbers.find(nNumber);
		if (it != mExistingNumbers.end())
		{
			mExistingNumbers.at(it->first) = it->second + 1;
			if (mExistingNumbers.at(it->first) >= nMajority)
				return it->first;
		}
		else
		{
			mExistingNumbers.insert(std::make_pair<int, int>(std::move(nNumber), 1));
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
```

###Python

```Python
class NoMajority(Exception):
    def __init__(self):
        self.value = "No Majority"

    def __str__(self):
        return self.value

def FindMajority(listNumbers):
    mExsitingNumbers = dict()
    nMajority = len(listNumbers) / 2
    for nNumber in listNumbers:
        if nNumber in mExsitingNumbers:
            mExsitingNumbers[nNumber] += 1
            if mExsitingNumbers[nNumber] >= nMajority:
                return nNumber
        else:
            mExsitingNumbers[nNumber] = 1
    raise NoMajority

listNumbers = [ 1,2,3,4,5,6,7,8,9,0]

try:
    print(FindMajority(listNumbers))
except NoMajority as err:
    print(err)

try:
    print(FindMajority([1,2,3,4,4,4,4,6,3,4]))
except NoMajority as err:
    print(err)
```

###Java

```Java
import java.util.*;

public class Q01_Majority {

	public static int FindMajority(List<Integer> vNumbers) throws Exception
	{
		int nSize = vNumbers.size();
		int nMajority = nSize / 2;
		HashMap<Integer, Integer> mExistingNumbers = new HashMap<Integer, Integer>();
		
		for (int i = 0; i < nSize; i++)
		{
			int nNumber = vNumbers.get(i);
			Integer nValue = mExistingNumbers.get(nNumber);
			if (nValue != null)
			{
				nValue++;
				if (nValue >= nMajority)
					return nNumber;
				mExistingNumbers.put(nNumber, nValue);
			}
			else
			{
				mExistingNumbers.put(nNumber, 1);
			}
		}

		throw new Exception("No Majority");
	}
	
	public static void main(String[] args) 
	{
		List<Integer> nNumbers1 = Arrays.asList(1,2,3,4,4,4,4,4,3,3);
		List<Integer> nNumbers2 = Arrays.asList(1,2,3,4,5,6,7,8,9,0);
		
		try 
		{
			System.out.println(FindMajority(nNumbers1));
			System.out.println(FindMajority(nNumbers2));
		}
		catch (Exception e)
		{
			System.out.println(e.getMessage());
		}
	}
}
```
