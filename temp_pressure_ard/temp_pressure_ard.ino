#include <Adafruit_MAX31865.h>

Adafruit_MAX31865 max = Adafruit_MAX31865(10, 11, 12, 13);
// The value of the Rref resistor. Use 430.0 for PT100 and 4300.0 for PT1000  
#define RREF      430.0
// The 'nominal' 0-degrees-C resistance of the sensor
// 100.0 for PT100, 1000.0 for PT1000
#define RNOMINAL  100.0
float val = 0;
int analogPin = A5;
void setup() {
  Serial.begin(9600);
  max.begin(MAX31865_2WIRE);  // set to 2WIRE or 4WIRE as necessary
}


void loop() {
  uint16_t rtd = max.readRTD();
  float ratio = rtd;
  ratio /= 32768;
  float temp = max.temperature(RNOMINAL, RREF) + 273.15;
  val = analogRead(analogPin);
  Serial.println(temp);
  Serial.println(val);
  delay(10000); 


}
