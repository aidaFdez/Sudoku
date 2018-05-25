import java.util.ArrayList;
import java.util.Random;
import java.util.Arrays;

public class sudoSolver {

    //addOne function as the one I created in Python in the other file.
    public static int addOne (int num){
        if (num == 9){
            return 1;
        }
        else{
            return num+1;
        }
    }

    public static boolean checkPossible(int position, int num,int[] sudo){
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
        while (k < position){
            if (num == sudo[k]){
                return false;
            }
            k++;
        }

        //Checks that the number does not happen in the same square
        k = ((int)(position/27))*27;
        k = k + ((int)(numB/3))*3;

        j = 0;
        int b = 0;
        while ((k < position) && (j < 3) && (b < position)){
            b = k;
            l = 0;
            while(l <3){
                if(num == sudo[b]){
                    return false;
                }
                b++;
                l++;
            }
            k+= 9;
            j++;
        }

        return true;
    }

    //Add a number to the sudoku in the first possible cell
    public static int[] addNum(int[] sudo, int num){
        for (int i = 0; i <81; i++){
            if (sudo[i] == 0){
                sudo [i] = num;
                return sudo;
            }
        }
        return sudo;
    }

    //First instance of 0 in the sudoku
    public static int firstZero (int[] sudo){
        for (int i = 0; i<sudo.length; i++){
            if (sudo[i] == 0){
                return i;
            }
        }
    }

    //List of the possible next states given another
    public static ArrayList<int[]> nextOnes(int num, int[] sudo, ArrayList<int[]> visit){
        ArrayList<int[]> sudoDup = sudo;
        int l = 0;
        ArrayList<int[]> toRet = new ArrayList<int[]>();
        int ind = firstZero(sudo);
        while (l<9){
            if (checkPossible(ind, num, sudoDup)){
                //Do not add if it has been visited
                //Esto está duplicando los números en sudo, modifícalo!
                if (!(visit.contains(addNum(sudo, num)))){
                    toRet.add(addNum(sudo, num));
                }
            }
            num = addOne(num);
            l++;
        }
        return toRet;
    }

    public static void main (String [] args){
        int [] a = {1,2,3,4,5,6,7,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
        ArrayList<int[]> queue = new ArrayList<int[]>();
        ArrayList<int[]> visited = new ArrayList<int[]>();
        ArrayList<int[]> b = (nextOnes(9,a,visited));
        //for (int i = 0; i<b.size();i++){
        //    for (int j = 0; j<b.get(i).length; i++){
        //        System.out.print(b.get(i)[j]);
        //    }
        //}
        //System.out.println(Arrays.deepToString(b.toArray()));
    }
}
