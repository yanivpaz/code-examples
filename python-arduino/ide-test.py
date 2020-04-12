//Blinking_LED
//turn on the LED for half a second,then off for half a second,repeatedly
/************************************************/
const int ledPin = 13;//the number of the LED pin
/************************************************/
void setup()
{
  pinMode(ledPin,OUTPUT);//initialize the digital pin as an output
}
/************************************************/
//the loop routine runs over and over again forever
void loop()
{
  digitalWrite(ledPin,HIGH);//turn the LED on 
  delay(500);               //wait for half a second
  digitalWrite(ledPin,LOW); //turn the LED off
  delay(500);               //wait for half a second
}
