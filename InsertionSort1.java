public class InsertionSort1
    {
        public static void insertionSort1(int n, List<Integer> arr)
            {
                int num = arr.get(n - 1);
                for(int i = n - 2; i >= 0; i--)
                    {
                        int val = arr.get(i);
                        if((val > num) && !(i == 0))
                            {
                                arr.set(i+1, val);
                                for (Integer x : arr) {
                                    System.out.print(x + " ");
                                }
                                    System.out.println("");
                            }
                        else if((val > num) && (i == 0))
                            {
                                arr.set(i+1, val);
                                for (Integer x : arr) {
                                    System.out.print(x + " ");
                                }
                                System.out.println("");
                                arr.set(i, num);
                                for (Integer x : arr) {
                                    System.out.print(x + " ");
                                }
                            }
                        else
                            {
                                arr.set(i+1, num);
                                for (Integer x : arr) {
                                    System.out.print(x + " ");
                                }
                                break;
                            }
                    }
            }
 }
