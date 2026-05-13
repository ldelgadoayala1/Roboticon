int var; // para whiles

void A() {
  moverServo(PULGAR, 0);
  delay(500);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);
  moverServo(INDICE, 0);

  moverServo(PULGAR, 20);
}

void B() {

  moverServo(MENIQUE, 180);
  moverServo(ANULAR, 180);
  moverServo(CORAZON, 180);
  moverServo(INDICE, 180);
  moverServo(PULGAR, 0);

  delay(500);

  moverServo(PULGAR, 150);
}

void C() {

  moverServo(PULGAR, 20);

  moverServo(MENIQUE, 140);
  moverServo(ANULAR, 140);
  moverServo(CORAZON, 140);
  moverServo(INDICE, 140);
}

void D() {

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);
  moverServo(INDICE, 180);

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(PULGAR, 150);
}

void E() {

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(INDICE, 0);
}

void F1(){

  moverServo(PULGAR, 0);

  delay(1000);

  moverServo(MENIQUE, 180);
  moverServo(ANULAR, 180);
  moverServo(CORAZON, 180);
  moverServo(INDICE, 0);

  delay(1000);

  moverServo(PULGAR, 150);
}

void G() {

  moverServo(PULGAR, 0);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);

  moverServo(INDICE, 150);

  delay(1000);

  moverServo(PULGAR, 150);
}

void H() {
  tijera();
}

void I() {

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(INDICE, 0);
  moverServo(CORAZON, 0);
  moverServo(ANULAR, 0);

  moverServo(MENIQUE, 180);

  delay(500);

  moverServo(PULGAR, 170);
}

void J() {

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(INDICE, 0);
  moverServo(CORAZON, 0);
  moverServo(ANULAR, 0);

  moverServo(MENIQUE, 180);

  delay(500);

  moverServo(PULGAR, 170);
}

void K() {

  moverServo(PULGAR, 30);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);

  moverServo(CORAZON, 135);
  moverServo(INDICE, 180);
}

void L() {

  moverServo(PULGAR, 0);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);

  moverServo(INDICE, 180);
}

void M() {

  moverServo(PULGAR, 150);

  moverServo(MENIQUE, 0);

  moverServo(ANULAR, 120);
  moverServo(CORAZON, 120);
  moverServo(INDICE, 120);
}

void N() {

  moverServo(PULGAR, 150);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);

  moverServo(CORAZON, 140);
  moverServo(INDICE, 140);
}

void O() {
  piedra();
}

void P() {

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);

  moverServo(CORAZON, 120);
  moverServo(INDICE, 20);

  moverServo(PULGAR, 150);
}

void Q() {

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(MENIQUE, 10);
  moverServo(ANULAR, 10);
  moverServo(CORAZON, 10);
  moverServo(INDICE, 10);

  moverServo(PULGAR, 50);
}

void R() {

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);

  moverServo(CORAZON, 180);
  moverServo(INDICE, 160);

  moverServo(PULGAR, 150);
}

void S() {

  moverServo(PULGAR, 0);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);

  moverServo(INDICE, 180);

  delay(500);

  moverServo(PULGAR, 150);
}

void T() {

  moverServo(PULGAR, 150);

  moverServo(MENIQUE, 0);
  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);
  moverServo(INDICE, 0);
}

void U() {

  moverServo(PULGAR, 150);

  moverServo(MENIQUE, 180);

  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);

  moverServo(INDICE, 180);
}

void V() {
  tijera();
}

void W() {
  wleng();
}

void X() {
  S();
}

void Y() {

  moverServo(PULGAR, 0);

  delay(500);

  moverServo(MENIQUE, 180);

  moverServo(ANULAR, 0);
  moverServo(CORAZON, 0);
  moverServo(INDICE, 0);
}

void Z() {
  S();
}