import serial
class Arduino:
	def __init__(self, port):
		self.port = port;
		self.socket = serial.Serial(self.port);
		self.R = 0
		self.G = 0
		self.B = 0;
	def registerLEDs(self,R,G,B):
		self.R = R
		self.G = G
		self.B = B
		self.socket.write("1 "+str(R)+" "+str(G)+" "+str(B)+"\n");

