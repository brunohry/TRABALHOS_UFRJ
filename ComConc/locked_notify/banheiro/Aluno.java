package lab5;

public class Aluno extends Thread{
	Banheiro ban;
	int ID;
	
	public Aluno(Banheiro ban,int ID){
		this.ban=ban;
		this.ID=ID;
	}
	
	public void run (){
		System.out.println("Thread ID: "+ ID + " na fila do vaso");
		try {
			ban.usoDoVaso(ID);
		} catch (InterruptedException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		System.out.println("Thread ID: "+ ID + " na fila do da pia");
		try {
			ban.usoDaPia(ID);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println("Thread ID: "+ ID + " Aliviada");
		
	}
			
		
	
	
	

}