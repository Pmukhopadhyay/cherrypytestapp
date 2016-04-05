import java.util.concurrent.BlockingQueue;
import java.util.concurrent.ArrayBlockingQueue;

class Message{
	private String messageText;
	Message(String message){
		this.messageText = message;
	}
	public String getMessage(){
		return this.messageText;
	}
}

class Producer implements Runnable{
	BlockingQueue queue;
	Producer(BlockingQueue queue){
		this.queue = queue;
	}

	public void run(){
		while(true){
			try{
				queue.put(produce());
			}catch(InterruptedException exception){
				exception.printStackTrace();
			}
			
		}
	}

	private Message produce() throws InterruptedException{
		Message message = new Message("From Producer#"+ System.currentTimeMillis());
		Thread.sleep(10);
		return message;
	}
}

class Consumer implements Runnable{
	BlockingQueue queue;
	Consumer(BlockingQueue queue){
		this.queue = queue;
	}

	public void run(){
		while(true){
			try{
				Message msg = (Message) queue.take();
				System.out.println("From Consumer#message>>"+msg.getMessage()+"|"+Thread.currentThread().getName());
			}catch(InterruptedException exception){
				exception.printStackTrace();
			}
		}
	}
}

public class Thrd{
	public static void main(String args[]){
		BlockingQueue<Message> queue = new ArrayBlockingQueue<Message>(10);
		Thread producerThread = new Thread(new Producer(queue),"P");
		Thread firstConsumer = new Thread(new Consumer(queue),"C1");
		Thread secondConsumer = new Thread(new Consumer(queue),"C2");
		producerThread.start();
		firstConsumer.start();
		secondConsumer.start();
	}
}