
package felipez33;

import java.util.Scanner;


public class Felipez33 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double[] numeros = new double[10];

        System.out.println("Ingrese 10 números separados por espacio:");
        for (int i = 0; i < numeros.length; i++) {
            numeros[i] = sc.nextDouble();
        }

        Estadistica est = new Estadistica(numeros);

        System.out.printf("El promedio es %.2f%n", est.promedio());
        System.out.printf("La desviacion estandar es %.5f%n", est.desviacion());
    }

    
    
    
}
