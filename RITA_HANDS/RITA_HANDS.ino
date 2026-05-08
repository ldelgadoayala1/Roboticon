#include <Servo.h>
// Declaramos cada servomotor
Servo menique;
Servo anular;
Servo corazon;
Servo indice;
Servo pulgar;
Servo muneca;
//Declaramos variables


char input;



void setup() {

  Serial.begin(9600);//sentecia para ver parametros en una pantalla virtual o fisica

  menique.attach(4); //sentencia para habilitar pin 13
  anular.attach(5); //sentencia para habilitar pin 12
  corazon.attach(6); //sentencia para habilitar pin 11
  indice.attach(7); //sentencia para habilitar pin 10
  pulgar.attach(3); //sentencia para habilitar pin 9
 // muneca.attach(13);
}



void loop() { //PROGRAMA PRINCIPAL
  //Ejecutamos la accion
  
  input = Serial.read();
  
  
  switch(input){
    case ('1'):
      piedra();
      break;
    case ('2'): 
      papel();
      break;
    case('3'):
      tijera();
      break;
    case('q'):
      like(); 
      break;
    case('w'):
      tomar();    
      break;
    case('e'):
      metal();    
      break;
    case('a'):
      wleng();
      break;
    case('s'):
      ok();
      break;
    case('d'):
      test();
      break;
    case('z'):
      reverse();
      break;
    case('x'):
      ven();
      break;
    case('c'):
      insulto(); 
      break;
    case('4'):
      restcachipunt();    
      break;
    case('5'):
      dedos_close();    
      break;
    case('6'):
      dedos_on();
      break;
    case('r'):
      mafioso(); 
      break;
    case('t'):
      gun();    
      break;
    case('y'):
      
      muestra();
      break;
  
  //lenguaje señas
    case('A'):
      A();
      break;
    case('B'):
      B();
      break;
    case('C'):
      C();
      break;
    case('D'):
      D();
      break;
    case('E'):
      E();
      break;
    case('F'):
      F1();
      break;
    case('G'):
      G();
      break;
    case('H'):
      H();
      break;
    case('I'):
      I();
      break;
    case('J'):
      J();
      break;
    case('K'):
      K();
      break;
    case('L'):
      L();
      break;
    case('M'):
      M();
      break;
    case('N'):
      N();
      break;
    case('O'):
      O();
      break;
    case('P'):
      P();
      break;
    case('Q'):
      Q();
      break;
    case('R'):
      R();
      break;
    case('S'):
      S();
      break;
    case('T'):
      T();
      break;
    case('U'):
      U();
      break;
    case('V'):
      V();
      break;
    case('W'):
      W();
      break;
    case('X'):
      X();
      break;
    case('Y'):
      Y();
      break;
    case('Z'):
      Z();
      break;
  //clases
    case('+'):
      grupo1();
      break;
    case('{'):
      grupo2();
      break;
    case('}'):
      grupo3();
      break;
    case(','):
      grupo4();
      break;
    case('.'):
      grupo5();
      break;
    }
}
