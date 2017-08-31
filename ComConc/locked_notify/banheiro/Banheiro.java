package lab5;

public class Banheiro {
	private boolean isLockedBan = false;
	private boolean isLockedPia = false;
	
	public synchronized void usoDoVaso(int id) throws InterruptedException{
		while(isLockedBan){
			wait();
		}
		isLockedBan = true;
		Thread.sleep(500);
		System.out.println(" thread "+ id +" no vaso");
		isLockedBan = false;
		notify();
		
		
	}
	
	public synchronized void usoDaPia(int id) throws InterruptedException{
		while(isLockedPia){
			wait();
		}
		isLockedPia = true;
		System.out.println(" thread "+ id +" na pia");
		Thread.sleep(200);
		
		isLockedPia = false;
		notify();
	}

}
