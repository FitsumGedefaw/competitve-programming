class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> myList = new ArrayList<String>();
                    for(int i = 1; i <= n; i++)
                        {
                            if(!((i%3) == 0) && !((i%5) == 0))
                                myList.add("" + i);
                            else if((i%3) == 0 && !((i%5) == 0))
                                myList.add("Fizz");
                            else if(!((i%3) == 0) && (i%5) == 0)
                                myList.add("Buzz");
                            else
                                myList.add("FizzBuzz");

                        }
                    return myList;
    }
}
