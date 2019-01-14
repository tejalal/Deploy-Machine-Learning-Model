import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;

public class IRIS {

	public static void main(String[] args) {
	
		Client client=ClientBuilder.newClient();
		double sl=1.2;
		double sw=2.2;
		double pl=2.2;
		double pw=1.2;
	    
		String query= "?sepallength="+sl+"&sepalwidth="+"sw"+"&petallength="+pl+"&petalwidth="+pw;
		String url="http://127.0.0.1:5000/predict"+query;
		
		WebTarget target=client.target(url);
		////target.request(MediaType.TEXT_XML).get(String.class)
		String resp=target.request(MediaType.APPLICATION_JSON).get(String.class);
		System.out.println(resp);
	}

}
