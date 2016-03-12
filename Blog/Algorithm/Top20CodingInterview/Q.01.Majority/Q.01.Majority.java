import java.util.*;

public class Q01_Majority {

	public static int FindMajority(List<Integer> nList) throws Exception
	{
		int nSize = nList.size();
		int nMajority = nSize / 2;
		HashMap<Integer, Integer> mFind = new HashMap<Integer, Integer>();
		
		for (int i = 0; i < nSize; i++)
		{
			int nElement = nList.get(i);
			Integer nValue = mFind.get(nElement);
			if (nValue != null)
			{
				nValue++;
				if (nValue >= nMajority)
					return nElement;
				mFind.put(nElement, nValue);
			}
			else
			{
				mFind.put(nElement, 1);
			}
		}

		throw new Exception("No Majority");
	}
	
	public static void main(String[] args) 
	{
		List<Integer> nList1 = Arrays.asList(1,2,3,4,4,4,4,4,3,3);
		List<Integer> nList2 = Arrays.asList(1,2,3,4,5,6,7,8,9,0);
		
		try 
		{
			System.out.println(FindMajority(nList1));
			System.out.println(FindMajority(nList2));
		}
		catch (Exception e)
		{
			System.out.println(e.getMessage());
		}
	}
}
