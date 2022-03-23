import java.util.*;
public class DominoPiling
    {
        public static void main(String[] args) {
            Scanner inputt = new Scanner(System.in);
            int height = inputt.nextInt();
            int width = inputt.nextInt();
            int numOfDomino = (height * width) / 2;
            System.out.println(numOfDomino);
        }
    }
