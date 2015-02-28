import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int R = in.nextInt(); // the length of the road before the gap.
        int G = in.nextInt(); // the length of the gap.
        int L = in.nextInt(); // the length of the landing platform.

        // game loop
        while (true) {
            int S = in.nextInt(); // the motorbike's speed.
            int X = in.nextInt(); // the position on the road of the motorbike.
            
            //Avant le gouffre
            if( X < R){
                //On peut plus accelerer: donc on fait soit SLOW soit JUMP
                if( S > R - X ){
                    //Vitesse plus que nécessaire et on a le temps de relantir
                    if( S > G + 1 && X < R- S){
                        System.out.println("SLOW");
                    //Pas de temps pour ralentir donc fait saute
                    }else{
                        System.out.println("JUMP");
                    }
                }else{
                    //Vitesse faible et gouffre assez loin pour accelerer
                    if( S < R - X && S < G + 1){
                        System.out.println("SPEED");
                    //Vitesse minimale nécessaire atteinte, gouffre assez proche
                    }else if( S == G + 1){
                        System.out.println("WAIT");
                    //Vitesse plus que nécessaire on ralenti
                    }else{
                        System.out.println("SLOW");
                    }
                }
            //Après le gouffre
            }else{
                System.out.println("SLOW");
            }
        }
    }
}