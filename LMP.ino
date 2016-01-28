#include <Stepper.h>

int in1Pin = 12;
int in2Pin = 11;
int in3Pin = 10;
int in4Pin = 9;
int vOut = A0;

Stepper motor(512, in1Pin, in2Pin, in3Pin, in4Pin);


void setup() {
    pinMode(in1Pin, OUTPUT);
    pinMode(in2Pin, OUTPUT);
    pinMode(in3Pin, OUTPUT);
    pinMode(in4Pin, OUTPUT);


    Serial.begin(9600);
    motor.setSpeed(20);
}

void loop() {
    if(Serial.available()) {
        int rcv = Serial.read();
        int mode = rcv;
        if(mode == '1') {
            motor.step(-175);

            delay(3000);

            int sensorValue = analogRead(vOut);
            float scaleFactor = 5.0 / 1023.0;
            float voltage = sensorValue * scaleFactor;
            Serial.println(voltage);

            delay(1000);
            mode = 0;
        }
        if(mode == '2') {
            motor.step(1225);
            mode = 0;
        }
        if(mode == '3') {
            int sensorValue = analogRead(vOut);
            float scaleFactor = 5.0 / 1023.0;
            float voltage = sensorValue * scaleFactor;
            Serial.println(voltage);

            delay(1000);
            mode = 0;
        }
    }
}
