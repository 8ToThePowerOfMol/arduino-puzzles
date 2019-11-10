const int injector_fill = 4;
const int injector_pop = 3;
const int tank_pop = 2;
const int tank_fill = 1;
//const int nothing = 0;     
const int tank_1 = 9;
const int tank_2 = 8;
const int tank_3 = 7;
const int tank_4 = 6;        
const int tank_5 = 5;
const int injector_1 = 12;
const int injector_2 =  11;
const int injector_3 = 10;
const int buzz = 13;  

const int tanks[] = {tank_1, tank_2, tank_3, tank_4, tank_5};
const int injectors[] = {injector_1, injector_2, injector_3};

const int after_delay = 1500;
const int butt_timeout = 600;

int butt_injc_fill, butt_injc_pop, butt_tank_pop, butt_tank_fill;

int tank, injector;

void set_tank(int count)
{
  for(int i = 0; i < count; i++)
    digitalWrite(tanks[i], HIGH);
  for(int i = count; i < 5; i++)
    digitalWrite(tanks[i], LOW);
}

void set_injector(int count)
{
  for(int i = 0; i < count; i++)
    digitalWrite(injectors[i], HIGH);
  for(int i = count; i < 3; i++)
    digitalWrite(injectors[i], LOW);
}

void setup()
{
    // init
    pinMode(injector_fill, INPUT);
    pinMode(injector_pop, INPUT);
    pinMode(tank_pop, INPUT);
    pinMode(tank_fill, INPUT);
    pinMode(tank_1, OUTPUT);
    pinMode(tank_2, OUTPUT);
    pinMode(tank_3, OUTPUT);
    pinMode(tank_4, OUTPUT);
    pinMode(tank_5, OUTPUT);
    pinMode(injector_1, OUTPUT);
    pinMode(injector_2, OUTPUT);
    pinMode(injector_3, OUTPUT);
    pinMode(buzz, OUTPUT);
    
    for(int i = 0; i < 5; i++)
      digitalWrite(tanks[i], LOW);

    for(int i = 0; i < 3; i++)
      digitalWrite(injectors[i], LOW);
          

    injector = 0;
    tank = 0;

    // beep
    digitalWrite(buzz, HIGH);
    delay(150);
    digitalWrite(buzz, LOW);
}

void fill_tank()
{
  tank = 5;
}

void empty_tank()
{
  tank = 0;
}

void fill_injector()
{
  injector = 3;
}

void empty_injector()
{
  injector = 0;
}

void pop_tank()
{
  int space_left = 3 - injector;

  if(space_left > tank)
    space_left = tank;

  tank -= space_left;
  injector += space_left; 
  
  if(injector > 3)
    injector = 3;
}

void pop_injector()
{
  int space_left = 5 - tank;

  if(space_left > injector)
    space_left = injector;

  injector -= space_left;
  tank += space_left; 
  
  if(tank > 5)
    tank = 5;
}

void ending()
{
  set_tank(tank);
  set_injector(injector);
  while(1)
  {
    digitalWrite(buzz, HIGH);
    delay(800);
    digitalWrite(buzz, LOW);
    delay(500);
  }  
}

void beep()
{
  digitalWrite(buzz, HIGH);
  delay(50);
  digitalWrite(buzz, LOW);
}

void loop()
{
  digitalWrite(buzz, LOW);

  if(tank == 4)
    ending();
  
  butt_tank_fill = digitalRead(tank_fill);
  butt_injc_fill = digitalRead(injector_fill);
  butt_tank_pop = digitalRead(tank_pop);
  butt_injc_pop = digitalRead(injector_pop);

  if(((butt_tank_fill == LOW) && (butt_injc_fill == LOW)) && ((butt_tank_pop == LOW) && (butt_injc_pop == LOW)))
  {
    set_tank(tank);
    set_injector(injector);
  }
  else if(((butt_tank_fill == HIGH) && (butt_injc_fill == LOW)) && ((butt_tank_pop == LOW) && (butt_injc_pop == LOW)))
  {
    int butt_pressed = 0;
    unsigned long startedWaiting = millis();
    while((millis() - startedWaiting) <= butt_timeout)
    {
      butt_tank_pop = digitalRead(tank_pop);
      if(butt_tank_pop == HIGH)
        butt_pressed = 1;
    }

    if(butt_pressed == 1)
      fill_tank();
    else
      empty_tank();
    delay(after_delay);
    beep();
  }
  else if(((butt_tank_pop == HIGH) && (butt_tank_fill == LOW)) && ((butt_injc_fill == LOW) && (butt_injc_pop == LOW)))
  {
    int butt_pressed = 0;
    unsigned long startedWaiting = millis();
    while((millis() - startedWaiting) <= butt_timeout)
    {
      butt_tank_fill = digitalRead(tank_fill);
      if(butt_tank_fill == HIGH)
        butt_pressed = 1;
    }
    
    if(butt_pressed == 1)
      fill_tank();
    else
      pop_tank();
    delay(after_delay);
    beep();
  }
  else if(((butt_injc_fill == HIGH) && (butt_tank_fill == LOW)) && ((butt_tank_pop == LOW) && (butt_injc_pop == LOW)))
  {
    int butt_pressed = 0;
    unsigned long startedWaiting = millis();
    while((millis() - startedWaiting) <= butt_timeout)
    {
      butt_injc_pop = digitalRead(injector_pop);
      if(butt_injc_pop == HIGH)
        butt_pressed = 1;
    }
    
    if(butt_pressed == 1)
      fill_injector();
    else
      empty_injector();
    delay(after_delay);
    beep();
  }
  else if(((butt_injc_pop == HIGH) && (butt_tank_fill == LOW)) && ((butt_injc_fill == LOW) && (butt_tank_pop == LOW)))
  {
    int butt_pressed = 0;
    unsigned long startedWaiting = millis();
    while((millis() - startedWaiting) <= butt_timeout)
    {
      butt_injc_fill = digitalRead(injector_fill);
      if(butt_injc_fill == HIGH)
        butt_pressed = 1;
    }
    
    if(butt_pressed == 1)
      fill_injector();
    else
      pop_injector();
    delay(after_delay);
    beep();
  }/*
  else if(((butt_tank_fill == HIGH) && (butt_tank_pop == HIGH)) && ((butt_injc_fill == LOW) && (butt_injc_pop == LOW)))
  {
    fill_tank();
    delay(after_delay);
    beep();
  }
  else if(((butt_injc_fill == HIGH) && (butt_injc_pop == HIGH)) && ((butt_tank_fill == LOW) && (butt_tank_pop == LOW)))
  {
    empty_tank();
    delay(after_delay);
    beep();
  }*/
  else
    digitalWrite(buzz, HIGH);

  
  
}
