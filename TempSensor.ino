#include <LiquidCrystal.h>

// Initialize the library with the numbers of the interface pins
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

const int tempPin = A0; // Temperature sensor connected to A0
const int greenLedPin = 8; // Green LED connected to pin 8
const int redLedPin = 9; // Red LED connected to pin 9

int tempValue = 0; // Variable to store the temperature value
float temperatureC = 0.0; // Variable to store the temperature in Celsius
float temperatureF = 0.0; // Variable to store the temperature in Fahrenheit

void setup() {
  // Set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("Temp: ");

  // Initialize the LED pins as outputs
  pinMode(greenLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
}

void loop() {
  // Read the value from the temperature sensor
  tempValue = analogRead(tempPin);

  // Convert the analog reading to voltage
  float voltage = tempValue * (5.0 / 1023.0);

  // Convert the voltage to temperature in Celsius (assuming a TMP36 sensor)
  temperatureC = (voltage - 0.5) * 100.0;

  // Convert the temperature to Fahrenheit
  temperatureF = temperatureC * 9.0 / 5.0 + 32.0;

  // Clear the previous temperature display
  lcd.setCursor(0, 0); // Set the cursor to the beginning of the first line
  lcd.print("Temp:          "); // Clear the line by printing spaces

  // Print the new temperature to the LCD
  lcd.setCursor(6, 0); // Set the cursor to column 6, row 0
  lcd.print(temperatureF); // Print the temperature
  lcd.print(" F"); // Print the unit

  // Turn on the appropriate LED based on the temperature
  if (temperatureF < 90) {
    digitalWrite(greenLedPin, HIGH);
    digitalWrite(redLedPin, LOW);
  } else {
    digitalWrite(greenLedPin, LOW);
    digitalWrite(redLedPin, HIGH);
  }

  // Wait for a bit before taking another reading
  delay(1000);
}
