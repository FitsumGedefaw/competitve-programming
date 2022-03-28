class Solution {
    public String sortSentence(String s) {
        String result = "";
               String[] words = s.split("\\s");
               int n = words.length;
               String[] temp = new String[n];
               for(int i = 0; i < n; i++)
                    {
                        String word = words[i];
                        char c = word.charAt(word.length() - 1);
                        int num = Character.getNumericValue(c);
                        String trimmedString = word.replace((c+""), "");
                        temp[num - 1] = trimmedString;
                    }
                for(int i = 0; i < n; i++)
                    {
                        result = result + temp[i] + " ";
                    }
                String resultFinal = result.substring(0, result.length() - 1); 
                return resultFinal;
    }
}
