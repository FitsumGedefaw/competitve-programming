public static void bubbleSort(List<Integer> arr)
            {
                int n = arr.size();
                int numOfswaps = 0;
                for(int i = n - 2; i >= 0; i--)
                    {
                        for(int j = 0; j <= i; j++)
                            {
                                int a = arr.get(j);
                                int b = arr.get(j+1);
                                if(a > b)
                                    {
                                        arr.set(j, b);
                                        arr.set(j+1, a);
                                        numOfswaps++;
                                    }
                            }
                    }
              System.out.println("Array is sorted in " + numOfswaps + " swaps."); 
              System.out.println("First element: " + arr.get(0)); 
              System.out.println("Last element: " + arr.get(n - 1)); 
            }
