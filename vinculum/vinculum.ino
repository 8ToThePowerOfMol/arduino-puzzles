const int red = 8;
const int green = 9;
const int buzz =  13;
const int button = 7;     
      
int buttonState = 0;

int rnd;
int dif;

void turnRed() {
    digitalWrite(green, LOW);
    digitalWrite(red, HIGH);
}

void turnGreen() {
    digitalWrite(red, LOW);
    digitalWrite(green, HIGH);
}

void setup() {
    pinMode(red, OUTPUT);
    pinMode(green, OUTPUT);
    pinMode(buzz, OUTPUT);
    pinMode(button, INPUT);

    for(int i = 0; i<5; i++) {
        digitalWrite(buzz, HIGH);
        delay(150);
        digitalWrite(buzz, LOW);
        delay(100);
    }

    turnRed();
    delay(5000);
    turnGreen();
}

int setRnd(int count){
    if(count%3 == 0) return 1;
    else if(count%4 == 0) return 250;
    else if(count%5 == 0) return 399;
    else if(count%7 == 0) return 300;
    else if(count%11 == 0) return 350;
    else return 110;
}

void offalert() {
    int pocet = 250;
    //int rnd;
    //int dif;
    for(int i = 0; i<pocet; i++) {
        digitalWrite(buzz, HIGH);
        delay(500);
        digitalWrite(buzz, LOW);

        //delay(50);
        //rnd = random(0,400);
        //rnd =(analogRead(0)%400)+0;
        rnd = setRnd(i)/2;
        dif = 400-rnd/2;
        delay(rnd);
        digitalWrite(green, HIGH);
        delay(dif);
        digitalWrite(green, LOW);
        delay(rnd);
        digitalWrite(green, HIGH);
        delay(dif);
        digitalWrite(green, LOW);
        //delay(50);
    } 
}

void loop() {
  buttonState = digitalRead(button);
  if (buttonState == LOW) {
    turnRed();
    offalert();
    turnRed();
  }
}
