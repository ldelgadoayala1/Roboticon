 //para whiles
void piedra(){
  pulgar.write(100);
  menique.write(180);
  anular.write(180);
  corazon.write(180);
  indice.write(180);
  delay(500);

    
}

void papel() {

  indice.write(0);
  corazon.write(0);
  menique.write(0);
  anular.write(0);
  pulgar.write(0);
  delay(500);
  pulgar.write(0);
}


void tijera() {
  pulgar.write(0);
  delay(500);
  indice.write(0);
  corazon.write(0);
  anular.write(180);
  menique.write(180);
  delay(500);
  pulgar.write(170);

}
void like(){
  pulgar.write(0);
  indice.write(0);
  corazon.write(0);
  menique.write(0);
  delay(500);
  anular.write(0);

}

void tomar(){
  pulgar.write(170);
  int i = 0;
  while (i <= 180) {
    pulgar.write(i - 80);
    indice.write(180 - i);
    corazon.write(180 - i);
    menique.write(180 - i);
    anular.write(180 - i);
    delay(10);
    i++;

  }
}

void aguja(){
  pulgar.write(1);
  indice.write(0);
}

void metal(){
  pulgar.write(0);
  menique.write(180);
  indice.write(180);
  corazon.write(0);
  anular.write(0); 
}

void wleng() {
  menique.write(0);
  anular.write(180);
  corazon.write(180);
  indice.write(180);
  pulgar.write(180);

}

void ok(){
  menique.write(180);
  anular.write(180);
  corazon.write(180);
  for(int i=0;i<=180;i++){
    indice.write(180-i);
    pulgar.write(i);  
  }
  
}

void test(){
  pulgar.write(0);
  delay(1000);
  indice.write(180);
  delay(1000);
  corazon.write(180);
  delay(1000);
  anular.write(180);
  delay(1000);
  menique.write(180);
  delay(1000);
  
}
void reverse(){
  menique.write(0);
  delay(1000);
  anular.write(0);
  delay(1000);
  corazon.write(0);
  delay(1000);
  indice.write(0);
  delay(1000);
  pulgar.write(170);
  delay(1000);
}
void ven(){
  int var;
  pulgar.write(0);
  indice.write(180);
  menique.write(0);
  anular.write(0);
  corazon.write(0);
  pulgar.write(50);
  delay(1000);
  while(var < 5){
    indice.write(50);
    delay(550);
    indice.write(180);
    delay(550);
    var++;
  }
  piedra(); 

  
}
void insulto(){
  pulgar.write(170);
  indice.write(0);
  corazon.write(180);
  anular.write(0);
  menique.write(0);
  delay(5000);
  piedra();
  
}
void restcachipunt(){
  menique.write(0);
  anular.write(0);
  indice.write(0);
  corazon.write(0);
  pulgar.write(100);
}
//movimiento de dedos modo mafioso
void dedos_close(){ //dedos cerrados
  pulgar.write(0); //pulgar abierto
  delay(1000);
  menique.write(0);
  delay(500);
  anular.write(0);
  delay(500);
  corazon.write(0);
  delay(500);
  indice.write(0);
}
void dedos_on(){ //dedos abiertos
  
  menique.write(180);
  delay(500);
  anular.write(180);
  delay(500);
  corazon.write(180);
  delay(500);
  indice.write(180);
  delay(1000);
  pulgar.write(0); //pulgar abierto
}
//movimiento de dedos modo mafioso
void mafioso(){
  int var;
  while(var < 5 ){
    dedos_close();
    delay(1000);
    dedos_on();
    var++;
  }
}
//pistola
void gun(){
  int var;
  pulgar.write(0);
  indice.write(180);
  corazon.write(0);
  anular.write(0);
  menique.write(0);
  delay(1000);
  var = 0;
  while(var < 5){
    pulgar.write(180);
    delay(500);
    pulgar.write(0);
    delay(500);
    pulgar.write(0);
    delay(500);
    pulgar.write(180);
    delay(500);
    pulgar.write(0);
    var++;
  }
}
void muestra(){
  int var;
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
  }
}
