
 
// this code is prototype for a AUV 
// Include NewPing Library
#include "NewPing.h"
#include "PID_v1_bc.h"

 
#define TRIGGER_PIN  10 //trigger is wired to pin 10
#define ECHO_PIN     13 // echo is wired to pin 13
#define MAX_DISTANCE 400
#define Green_LED 2 // green led is wired to pin 2
#define Blue_LED 3 // blue led is wired to pin 3
#define Red_LED 4 // red led is wired to pin 4
#define Fan 9 // fan speed
float Multiplier = 5;
float placeholder;


NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);
 
float distance; // sets distance to floating integer to allow decimals
 
void setup() {
  Serial.begin (9600);  // serial coms
  pinMode(Green_LED, OUTPUT); //sets pin 2,3,4 to outputs
  pinMode(Blue_LED, OUTPUT);
  pinMode(Red_LED, OUTPUT);

}
 
void loop() {

  distance = sonar.ping_cm(); // sets distance = to instruction from new ping

    placeholder = distance * Multiplier; // takes distance from new ping and multiplys it by 5 

  //Writes number via PWM to change the speed of the fan based off the distance detected by the ultrasonic
  analogWrite(Fan, placeholder);
  
  // Send results to Serial Monitor also provides feedback from fan
  Serial.print("Distance = ");
  if (distance >= 30000 || distance < 0) {
    Serial.println("Out of range");
  }
  else {
    Serial.print(distance);
    Serial.println(" cm");
    Serial.println(placeholder);
    delay(250);
  }

  //scan delay
  delay(50);

    // sets the output for the lights, green is high fan speed, blue is medium speed, and red is low fan speed.
    // all values are set to cm by new ping
if (distance > 0 && distance < 10) { // if the distance is less than 10 and greater than zero turn on red light
    digitalWrite(Red_LED, HIGH);
    digitalWrite(Blue_LED, LOW);
    digitalWrite(Green_LED, LOW);
  } else if (distance >= 10 && distance < 25) { // if the distance is greater than or equal to 10 and less the 25 turn on blue light
    digitalWrite(Red_LED, LOW);
    digitalWrite(Blue_LED, HIGH);
    digitalWrite(Green_LED, LOW);
  } else if (distance >= 25) { // if the distance is greater than or equal to 25 turn on green light
    digitalWrite(Red_LED, LOW);
    digitalWrite(Blue_LED, LOW);
    digitalWrite(Green_LED, HIGH);
  }

}
