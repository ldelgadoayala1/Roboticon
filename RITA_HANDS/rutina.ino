// =====================================
// MOVIMIENTOS PRINCIPALES
// =====================================

void like(){

  moverServo(PULGAR, 0);

  moverServo(INDICE, 0);
  moverServo(CORAZON, 0);
  moverServo(MENIQUE, 0);

  delay(500);

  moverServo(ANULAR, 0);
}

void tomar(){

  moverServo(PULGAR, 170);

  int i = 0;

  while (i <= 180) {

    moverServo(PULGAR, i - 80);

    moverServo(INDICE, 180 - i);
    moverServo(CORAZON, 180 - i);
    moverServo(MENIQUE, 180 - i);
    moverServo(ANULAR, 180 - i);

    delay(10);

    i++;
  }
}

void aguja(){

  moverServo(PULGAR, 1);
  moverServo(INDICE, 0);
}

void metal(){

  moverServo(PULGAR, 0);

  moverServo(MENIQUE, 180);
  moverServo(INDICE, 180);

  moverServo(CORAZON, 0);
  moverServo(ANULAR, 0);
}

void wleng() {

  moverServo(MENIQUE, 0);

  moverServo(ANULAR, 180);
  moverServo(CORAZON, 180);
  moverServo(INDICE, 180);
  moverServo(PULGAR, 180);
}

void ok(){

  moverServo(MENIQUE, 180);
  moverServo(ANULAR, 180);
  moverServo(CORAZON, 180);

  for(int i = 0; i <= 180; i++){

    moverServo(INDICE, 180 - i);
    moverServo(PULGAR, i);

    delay(5);
  }
}

void test(){

  moverServo(PULGAR, 0);
  delay(1000);

  moverServo(INDICE, 180);
  delay(1000);

  moverServo(CORAZON, 180);
  delay(1000);

  moverServo(ANULAR, 180);
  delay(1000);

  moverServo(MENIQUE, 180);
  delay(1000);
}

void reverse(){

  moverServo(MENIQUE, 0);
  delay(1000);

  moverServo(ANULAR, 0);
  delay(1000);

  moverServo(CORAZON, 0);
  delay(1000);

  moverServo(INDICE, 0);
  delay(1000);

  moverServo(PULGAR, 170);
  delay(1000);
}

void ven(){

  int var = 0;

  moverServo(PULGAR, 0);
  moverServo(INDICE, 180);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);

  moverServo(PULGAR, 50);

  delay(1000);

  while(var < 5){

    moverServo(INDICE, 50);
    delay(550);

    moverServo(INDICE, 180);
    delay(550);

    var++;
  }

  piedra();
}

void insulto(){

  moverServo(PULGAR, 170);

  moverServo(INDICE, 0);
  moverServo(CORAZON, 180);

  moverServo(ANULAR, 0);
  moverServo(MENIQUE, 0);

  delay(5000);

  piedra();
}

void restcachipunt(){

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);

  moverServo(INDICE, 0);
  moverServo(CORAZON, 0);

  moverServo(PULGAR, 100);
}

// =====================================
// DEDOS MAFIOSO
// =====================================

void dedos_close(){

  moverServo(PULGAR, 0);

  delay(1000);

  moverServo(MENIQUE, 0);
  delay(500);

  moverServo(ANULAR, 0);
  delay(500);

  moverServo(CORAZON, 0);
  delay(500);

  moverServo(INDICE, 0);
}

void dedos_on(){

  moverServo(MENIQUE, 180);
  delay(500);

  moverServo(ANULAR, 180);
  delay(500);

  moverServo(CORAZON, 180);
  delay(500);

  moverServo(INDICE, 180);
  delay(1000);

  moverServo(PULGAR, 0);
}

void mafioso(){

  int var = 0;

  while(var < 5){

    dedos_close();

    delay(1000);

    dedos_on();

    var++;
  }
}

// =====================================
// PISTOLA
// =====================================

void gun(){

  int var;

  moverServo(PULGAR, 0);
  moverServo(INDICE, 180);

  moverServo(CORAZON, 0);
  moverServo(ANULAR, 0);
  moverServo(MENIQUE, 0);

  delay(1000);

  var = 0;

  while(var < 5){

    moverServo(PULGAR, 180);
    delay(500);

    moverServo(PULGAR, 0);
    delay(500);

    moverServo(PULGAR, 0);
    delay(500);

    moverServo(PULGAR, 180);
    delay(500);

    moverServo(PULGAR, 0);

    var++;
  }
}

// =====================================
// DEMOSTRACION
// =====================================

void muestra(){

  int var = 0;

  while(var < 2){

    piedra();
    delay(2000);

    papel();
    delay(2000);

    tijera();
    delay(2000);

    like();
    delay(2000);

    wleng();
    delay(2000);

    ok();
    delay(2000);

    test();
    delay(2000);

    reverse();
    delay(2000);

    ven();
    delay(2000);

    dedos_close();
    delay(2000);

    dedos_on();
    delay(2000);

    mafioso();
    delay(2000);

    gun();
    delay(2000);

    var++;
  }
}