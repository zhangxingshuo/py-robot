// CONTINUOUS

#include <Servo.h>

//Initialize servos
Servo left;
Servo right;
int servoL = 9;
int servoR = 10;

void setup() {
  // Attach servos
  left.attach(servoL);
  right.attach(servoR);
  
  left.write(90); // initialize as stationary
  right.write(90);

  //Initialize serial port
  Serial.begin(115200);
  Serial.write(B1); // Tell script that serial is connected
}

void loop() {
  if (Serial.available() > 0) {

    // read the duration and command from serial
    char input = (char) Serial.read();

    // commands: 
    //  'l': pivot left
    //  'r': pivot right
    //  'f': forward
    //  'b': backward
    //  's': stop
    
    switch(input) {
      case 'l':
        pivotL();
        break;
      case 'r':
        pivotR();
        break;
      case 'f':
        forward();
        break;
      case 'b':
        reverse();
        break;
      case 's':
        brake();
        break;
      default:
        brake();
        break;
    }
    
    Serial.write('0');
    Serial.flush();
  }
}

void forward() {
  left.write(180);
  right.write(0);
}

void reverse() {
  left.write(0);
  right.write(180);
}

void pivotR() {
  left.write(180);
  right.write(180);
}

void pivotL() {
  left.write(0);
  right.write(0);
}

void brake() {
  left.write(90);
  right.write(90);
}

