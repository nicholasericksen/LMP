int vOut = A0;


void setup() {
    Serial.begin(9600);
}

void loop() {
    int rcv = Serial.read();
    int mode = rcv;
    if(mode == '1') {
        int sensorValue = analogRead(vOut);
        float scaleFactor = 5.0 / 1023.0;
        float voltage = sensorValue * scaleFactor;
        Serial.println(voltage);

        delay(1000);
        mode = 0;
    }
}
