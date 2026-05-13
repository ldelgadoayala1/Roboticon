#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// ======================================================
// PCA9685
// ======================================================

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x40);

// ======================================================
// CONFIGURACION PWM
// ======================================================

#define SERVOMIN 150
#define SERVOMAX 600

// ======================================================
// CANALES PCA9685
// ======================================================

#define MENIQUE 0
#define ANULAR 1
#define CORAZON 2
#define INDICE 3
#define PULGAR 4
#define MUNECA 7

char input;

// ======================================================
// MOVER SERVO
// ======================================================

void moverServo(uint8_t canal, int angulo) {

  int minA = 0;
  int maxA = 180;

  switch(canal) {

    case MENIQUE:
      minA = 0;
      maxA = 180;
      break;

    case ANULAR:
      minA = 0;
      maxA = 180;
      break;

    case CORAZON:
      minA = 0;
      maxA = 180;
      break;

    case INDICE:
      minA = 0;
      maxA = 180;
      break;

    case PULGAR:
      minA = 0;
      maxA = 180;
      break;

    case MUNECA:
      minA = 20;
      maxA = 100;
      break;
  }

  angulo = constrain(angulo, minA, maxA);

  int pulso = map(angulo, 0, 180, SERVOMIN, SERVOMAX);

  pwm.setPWM(canal, 0, pulso);
}

// ======================================================
// LIBERAR SERVOS
// ======================================================

void liberarServos() {

  pwm.setPWM(MENIQUE, 0, 0);
  pwm.setPWM(ANULAR, 0, 0);
  pwm.setPWM(CORAZON, 0, 0);
  pwm.setPWM(INDICE, 0, 0);
  pwm.setPWM(PULGAR, 0, 0);
  pwm.setPWM(MUNECA, 0, 0);
}

// ======================================================
// MOVER MANO COMPLETA
// ======================================================

void moverMano(
  int meniqueAng,
  int anularAng,
  int corazonAng,
  int indiceAng,
  int pulgarAng
) {

  moverServo(MENIQUE, meniqueAng);
  moverServo(ANULAR, anularAng);
  moverServo(CORAZON, corazonAng);
  moverServo(INDICE, indiceAng);
  moverServo(PULGAR, pulgarAng);

  delay(1000);

  liberarServos();
}

// ======================================================
// MOVIMIENTO MUNECA
// ======================================================

void moverMuneca(int angulo) {

  moverServo(MUNECA, angulo);

  delay(400);

  pwm.setPWM(MUNECA, 0, 0);
}

// ======================================================
// GESTOS
// ======================================================

void piedra() {

  moverMano(
    140,
    140,
    140,
    140,
    110
  );
}

void papel() {

  moverMano(
    30,
    30,
    30,
    30,
    40
  );
}

void tijera() {

  moverMano(
    140,
    140,
    30,
    30,
    110
  );
}

// ======================================================
// SETUP
// ======================================================

void setup() {

  Serial.begin(9600);

  pwm.begin();

  pwm.setPWMFreq(50);

  delay(1000);

  Serial.println("=================================");
  Serial.println("RITA HANDS INICIADA");
  Serial.println("1 = Piedra");
  Serial.println("2 = Papel");
  Serial.println("3 = Tijera");
  Serial.println("4 = Muneca Izquierda");
  Serial.println("5 = Muneca Derecha");
  Serial.println("6 = Muneca Centro");
  Serial.println("=================================");

  papel();

  moverMuneca(90);
}

// ======================================================
// LOOP
// ======================================================

void loop() {

  if (Serial.available() > 0) {

    input = Serial.read();

    Serial.print("Comando recibido: ");
    Serial.println(input);

    switch(input) {

      case '1':

        Serial.println("PIEDRA");

        piedra();

        break;

      case '2':

        Serial.println("PAPEL");

        papel();

        break;

      case '3':

        Serial.println("TIJERA");

        tijera();

        break;

      case '4':

        Serial.println("MUNECA IZQUIERDA");

        moverMuneca(20);

        break;

      case '5':

        Serial.println("MUNECA DERECHA");

        moverMuneca(160);

        break;

      case '6':

        Serial.println("MUNECA CENTRO");

        moverMuneca(90);

        break;
    }
  }
}