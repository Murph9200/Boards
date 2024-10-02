(*************************************
  Created: Monday, September 29, 2024

  Description: ST to replace LD

**************************)



AI0051 := DINT; // Analog value from Banner LE250
laser_mm := REAL; //Allowing for decimal places
GRN_Lt := BOOL; //Banner stacklight green
YLW_Lt := BOOL; //Banner stacklight yellow
RED_Lt := BOOL; //Banner stacklight red

laser_mm := AI0051; // move analog value into laser_mm

if laser_mm >= 75 then //looks for laser value to be high than 75mm to turn green
	GRN_Lt := 1;
	YLW_Lt := 0;
	RED_Lt := 0;
end_if;

if laser_mm >= 30 and laser_mm <= 74 then // looks for laser value to be between 30 and 74 mm
	GRN_Lt := 0;
	YLW_Lt := 1;
	RED_Lt := 0;
end_if;

if laser_mm >= 0 and laser_mm <= 29 then //looks for laser value to be between 0 and 29 mm
	GRN_Lt := 0;
	YLW_Lt := 0;
	RED_Lt := 1;
end_if;