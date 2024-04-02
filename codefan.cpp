//Include thư viện
#include <OneWire.h>
#include <DallasTemperature.h>

// Chân nối với Arduino
#define ONE_WIRE_BUS 2
//Thiết đặt thư viện onewire
OneWire oneWire(ONE_WIRE_BUS);
//Mình dùng thư viện DallasTemperature để đọc cho nhanh
DallasTemperature sensors(&oneWire);
int led = 12;

void setup(void)
{
  Serial.begin(9600);
  sensors.begin();
  pinMode(led, OUTPUT); 
}

void loop(void)
{ 
  sensors.requestTemperatures();  
  Serial.print("Nhiet do");
  Serial.println(sensors.getTempCByIndex(0)); // vì 1 ic nên dùng 0
 
  if(sensors.getTempCByIndex(0) > 30)
  {
     digitalWrite(led, HIGH);   // bật đèn led sáng
  }
  else
  {
    digitalWrite(led, LOW);    // tắt đèn led
  }
  //chờ 1 s rồi đọc để bạn kiệp thấy sự thay đổi
  delay(1000);
}
