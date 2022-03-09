void setup() {
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
  pinMode(13,OUTPUT);

}

void loop() {

  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
   unsigned  int  incomingByte = Serial.read();

    // say what you got:
    
    digitalWrite(13,HIGH);
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
    digitalWrite(13,LOW);
  }
}