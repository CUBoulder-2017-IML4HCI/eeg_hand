
//You can set these variables in the scene because they are public 
public var RemoteIP : String = "127.0.0.1";
public var SendToPort : int = 6448;
public var ListenerPort : int = 12000;
public var controller : Transform; 
private var handler : Osc;
private var classification : int = 0;
private var regression : float = 0;


public function Start ()
{
	//Initializes on start up to listen for messages
	//make sure this game object has both UDPPackIO and OSC script attached
	
	var udp : UDPPacketIO = GetComponent("UDPPacketIO");
	udp.init(RemoteIP, SendToPort, ListenerPort);
	handler = GetComponent("Osc");
	handler.init(udp);
			

	//Tell Unity to call function Example1 when message /wek/outputs arrives
	handler.SetAddressHandler("/wek/outputs", Example1);
}
Debug.Log("OSC Running");

//Use the values from OSC to do stuff
function Update () {
	var go = GameObject.Find("female_hand_right");

	if(classification == 1){
		go.GetComponent.<Animation>().Play("Wave");
	}
	else if(classification == 2){
		go.GetComponent.<Animation>().Play("peace");
	}
	else if(classification == 3){
		go.GetComponent.<Animation>().Play("theBird");
	}
}	

//This is called when /wek/outputs arrives, since this is what's specified in Start()
public function Example1(oscMessage : OscMessage) : void
{	
	
	Debug.Log("Called Example One > " + Osc.OscMessageToString(oscMessage));
	Debug.Log("Message Values > " + oscMessage.Values[0] + " " + oscMessage.Values[1]);
	classification = oscMessage.Values[0];
	regression = oscMessage.Values[1];
	
} 