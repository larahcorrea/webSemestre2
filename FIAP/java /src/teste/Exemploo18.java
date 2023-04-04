package teste;

import java.util.Scanner;

public class Exemploo18 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner ler = new Scanner(System.in);

		int v, i, a, t;

		System.out.println("Digite a velicidade inicial  ");
		i = ler.nextInt();

		System.out.println("Digite a aceleração  ");
		a = ler.nextInt();

		System.out.println("Digite o tempo  ");
		t = ler.nextInt();

		v = i + (a * t);

		if (v < 40 || v == 40) {
			System.out.println("Veículo muito lento");
		} else if (v < 60) {
			System.out.println("Velocidade permitida");
		}
		else if 
	

	}
}