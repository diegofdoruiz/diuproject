#include "SoftwareSerial.h"
#include "GFButton.h"

//crea las instancias de botones
GFButton button1(2);
GFButton button2(3);
GFButton button3(4);
GFButton button4(5);
const int analogPin = 0;

SoftwareSerial serial_connection(10, 11);//Create a serial connection with TX and RX on these pins
#define BUFFER_SIZE 64//This will prevent buffer overruns.
char inData[BUFFER_SIZE];//This is a character buffer where the data sent by the python script will go.
char inChar=-1;//Initialie the first character as nothing
int count=0;//This is the number of lines sent in from the python script
int i=0;//Arduinos are not the most capable chips in the world so I just create the looping variable once
void setup()
{
  Serial.begin(9600);//Initialize communications to the serial monitor in the Arduino IDE
  serial_connection.begin(9600);//Initialize communications with the bluetooth module
  serial_connection.println("Ready!!!");//Send something to just start comms. This will never be seen.
  Serial.println("Started");//Tell the serial monitor that the sketch has started.
}
void loop()
{
  //This will prevent bufferoverrun errors
  byte byte_count=serial_connection.available();//This gets the number of bytes that were sent by the python script

  //Read input analog 0
  int analog0 = analogRead(analogPin);
  
  if(analog0 > 50 && analog0 <= 150){
    Serial.println("1");
    serial_connection.println("1");
    delay(1000);
  }
  if(analog0 > 170 && analog0 <= 235){
    Serial.println("2");
    serial_connection.println("2");
    delay(1000);
  }
  if(analog0 > 270 && analog0 <= 340){
    Serial.println("3");
    serial_connection.println("3");
    delay(1000);
  }
  if(analog0 > 370 && analog0 <= 440){
    Serial.println("4");
    serial_connection.println("4");
    delay(1000);
  }
  if(analog0 > 470 && analog0 <= 550){
    Serial.println("5");
    serial_connection.println("5");
    delay(1000);
  }
  if(analog0 > 570 && analog0 <= 650){
    Serial.println("6");
    serial_connection.println("6");
    delay(1000);
  }
  if(analog0 > 670 && analog0 <= 750){
    Serial.println("7");
    serial_connection.println("7");
    delay(1000);
  }
  if(analog0 > 770 && analog0 <= 850){
    Serial.println("8");
    serial_connection.println("8");
    delay(1000);
  }
  if(analog0 > 890 && analog0 <= 970){
    Serial.println("9");
    serial_connection.println("9");
    delay(1000);
  }
  if(analog0 > 1000){
    Serial.println("10");
    serial_connection.println("10");
    delay(1000);
  }
    
  /*if(button1.wasPressed()){
    serial_connection.println("1");
  }
    
  if(button2.wasPressed()){
    serial_connection.println("2");
  }
    
  if(button3.wasPressed()){
    serial_connection.println("3");
  }
    
  if(button4.wasPressed()){
    serial_connection.println("4");
  }*/
  delay(100);//Pause for a moment 
}
