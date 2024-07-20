// C++ code
//
int rightEn = 3;
int forRight = 4;
int revRight = 5;
int leftEn = 6;
int forLeft = 7;
int revLeft = 8;
int TurnLeft = 9;
int TurnRight = 10;
int Forward = 11;
int Reverse = 12;
int STOP = 13;

  


void setup()
{
  pinMode(rightEn, OUTPUT);
  pinMode(forRight, OUTPUT);
  pinMode(revRight, OUTPUT);
  pinMode(leftEn, OUTPUT);
  pinMode(forLeft, OUTPUT);
  pinMode(revLeft, OUTPUT);
  
}

void loop()
{

 /* analogWrite(rightEn, 255);
  analogWrite(leftEn, 100);
   leftTurn();
   delay(5000);
  */
   
/*analogWrite(rightEn, 100);
  analogWrite(leftEn, 255);
   rightTurn();
   delay(5000);

    */
     
 /*  analogWrite(rightEn, 255);
   analogWrite(leftEn, 255);
   forward();
   delay(5000);
  */
      
/* analogWrite(rightEn, 255);
   analogWrite(leftEn, 255);
   reverse();
   delay(5000);
    */  

  
  analogWrite(rightEn, 0);
  analogWrite(leftEn, 0);
   Stop();
   
}
void rightFor(){
  digitalWrite(revRight, LOW);
  digitalWrite(forRight, HIGH);
  
}

void rightRev(){
  digitalWrite(revRight, HIGH);
  digitalWrite(forRight, LOW);
  
  
}

void leftFor(){
  digitalWrite(revLeft, LOW);
  digitalWrite(forLeft, HIGH);
  
}

void leftRev(){
  digitalWrite(revLeft, HIGH);
  digitalWrite(forLeft, LOW);
  
  
}

void forward(){
  rightFor();
  leftFor();
}

void reverse(){
  rightRev();
  leftRev();
}

void rightTurn(){
  rightRev();
  leftFor();
}

void leftTurn(){
  leftRev();
  rightFor();
  
}
void Stop(){
}