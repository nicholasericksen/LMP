int lightPin = 0;
int ledPin = 11;

void setup() {
    Serial.begin(9600);
    pinMode( ledPin, OUTPUT );
}

void loop() {
    Serial.println(analogRead(lightPin));
    analogWrite(ledPin, analogRead(lightPin)/2);

    delay(10);
}
