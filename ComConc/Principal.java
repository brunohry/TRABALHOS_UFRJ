package lab5;

public class Principal {
	public static void main(String[] args){
	Banheiro ban = new Banheiro();
	for (int i = 1 ; i <= 10; i++ ){
		Aluno alun = new Aluno(ban, i);
		alun.setPriority(i);
		alun.start();
		
		
	}
	}

}
