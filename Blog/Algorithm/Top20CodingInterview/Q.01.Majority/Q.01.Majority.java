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
