#include <iostream>
using namespace std;
int main(){
cout << "*****************************************"<<endl;
cout << "* Bienvenido al juego de la adivinanza! *"<<endl;
cout << "*****************************************"<<endl;

int numero_secreto=42;
cout<< "el numero secreto es ..."<< numero_secreto << ". no se lo diga a nadie"<<endl;

int adivina;
cout<<"cual es el numero?";
cin>>adivina;
cout<<"Su numero ingresado es: "<<adivina<<endl;
if(adivina==numero_secreto){
cout<<"Correcto, .. adivino el numero secreto"<<endl;
}
else if(adivina>numero_secreto){
cout<<"El numero ingresado es mayor al numero secreto"<<endl;
}
else if(adivina<numero_secreto){
cout<<"El numero ingresado es menor al  numero secreto"<<endl;
}

}
