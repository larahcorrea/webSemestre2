package teste;

import java.util.Scanner;

public class Exemploo17 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner ler = new Scanner(System.in);

		float peso, altura, imc;
		String sexo;
		
	

		System.out.printf("digitar peso  ");
		peso = ler.nextFloat();

		System.out.printf(" digitar altura ");
		altura = ler.nextFloat();
	
		System.out.printf("digitar sexo f/m  ");
		sexo = ler.nextLine();

		imc = peso / (altura * altura);

		if (sexo == "f") {
			if (imc < 19) {
				System.out.printf("Abaixo do ideal!");

			} else if (imc < 24) {
				System.out.printf("Peso ideal!");
			} else {
				System.out.printf("Acima do peso!");
			}
		} else {
			if (imc < 20) {
				System.out.printf("Abaixo do ideal!");
			} else if (imc < 25) {
				System.out.printf("Peso ideal!");
			} else
				System.out.printf("Acima do peso!");
		}
	}
}
