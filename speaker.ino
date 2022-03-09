void setup() {
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
<<<<<<< HEAD
  pinMode(13,OUTPUT); // use led because we can't use serial port in both IDE
=======
  pinMode(13,OUTPUT);
>>>>>>> 5f53692640f556a3bb8f5714fc2b378c6c552011

}

void loop() {

  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
   unsigned  int  incomingByte = Serial.read();
<<<<<<< HEAD
=======

    // say what you got:
    
>>>>>>> 5f53692640f556a3bb8f5714fc2b378c6c552011
    digitalWrite(13,HIGH);
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
    digitalWrite(13,LOW);
  }
<<<<<<< HEAD
}
=======
}
>>>>>>> 5f53692640f556a3bb8f5714fc2b378c6c552011
