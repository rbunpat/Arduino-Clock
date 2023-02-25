#include "Wire.h"
#include "LiquidCrystal_I2C.h"

char a_byte = 0;
String a_str = ""; 


LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Serial.println("asdasd");
  lcd.begin(16, 2);
  lcd.clear();
  lcd.noBacklight();
  lcd.setCursor(1, 0);
  lcd.print("time.nist.gov");
  lcd.backlight();
}

void loop() {
  if (Serial.available() > 0) { 
    a_byte = Serial.read(); 
    if (a_byte != '\n') { 
      a_str += a_byte;
    } else {
      Serial.println(a_str);
      lcd.clear(); 
      lcd.setCursor(0, 0);  
      lcd.print(a_str);     
      a_str = "";
      Serial.println(""); 
    }
  }
}
