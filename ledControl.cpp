#include<iostream>
#include<pigpio.h>
#include<unistd.h>
const int LED_PIN=18; //GPIO pin number
const int BLINK_DELAY=2000000; //2 second microseconds
int main(){
if (gpioInitialise()<0){
    std::cerr<<"pigpio initialization failed"<<std::endl;
    return 1;
}
//Set de LED pin  as an output
gpioSetMode(LED_PIN,PIN_OUTPUT);
std::cout<<"LED blinking.Press Ctrl+C to stop"<<std::endl;
try{
    while(true){
        gpioWrite(LED_PIN,1);//Turn LED on
        std::cout<<"LED ON"<<std::endl;
        usleep(BLINK_DELAY);
        gpioWrite(LED_PIN,0);//Turn LED off
        std::cout<<"LED OFF"<<std::endl;
        usleep(BLINK_DELAY);
    }    
}catch(const std::exception& e){
    std::cerr<<"An Error Ocurred: "<<e.what()<<std::endl;
}
gpioTerminate();
return 0;

}


