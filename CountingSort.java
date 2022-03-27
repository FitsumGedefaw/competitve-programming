import java.util.ArrayList;
import java.util.List;
public class CountingSort1
    {
        static List<Integer> countingSort(List<Integer> arr)
            {
                List<Integer> result = new ArrayList<Integer>();
                for(int i = 0; i < 100; i++)
                    {
                        result.add(0);
                    }
                for(int i = 0; i < arr.size(); i++)
                    {
                        int num = arr.get(i);
                        int val = result.get(num);
                        result.set(num, val+1);
                    }
                return result;
            }
  }
