import java.util.ArrayList;

public class sudoSolver {
    private ArrayList<Integer[]> queue = new ArrayList<Integer[]>();
    private ArrayList<Integer[]> visited = new ArrayList<Integer[]>();

    //addOne function as the one I created in Python in the other file.
    public static int addOne (int num){
        if (num == 9){
            return 1;
        }
        else{
            return num+1;
        }
    }

    public static boolean checkPossible(int[] sudo, int position, int num){
        int numB = position % 9;
        int j = numB;

        //Checks that number does not happen in the same column.
        while (j< position){
            if (num == sudo[j]){
                return false;
            }
            j = j + 9;
        }
        int k = ((int) (position/9))*9; //Sets the beginning of the row in k
        int l = k + 9; //Sets the ending of the row in l

        //Checks that the number does not happen in the row

        return true;
    }

    public static void main (String [] args){
        int a = (int) 3.2;
        System.out.println(a);
    }
}
