(*************************************
  Created: Monday, September 29, 2024

  Description:

*************************************)
if systemAuto and conveyor4PartPresent = 0 and cameraCountPass then // Allows conveyor 5 to run if the machine is in auto and there a correct number of parts on the conveyor
	conveyor5Premissive := 1;
end_if;
	
conveyor5Running := conveyor5Premissive; // starts conveyor 5

if conveyorFlag = 0 then // clears part count when the parts are out of pitch
	cameraCountPass := 0;
end_if;


if conveyor5Running and conveyorFlag then // triggers camera when parts are in pitch
	cameraTrigger := 1;
else
	cameraTrigger := 0;
end_if;


cameraCount := R00001;  // Number of components detected from cognex camera

if cameraCount = 5 then
	cameraCountPass := 1;
else
	camerCountPass := 0;
end_if;