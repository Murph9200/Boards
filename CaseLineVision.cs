(*************************************
  Created: Monday, September 29, 2024

  Description:

*************************************)


	
	if I00023 or Q00001 and M01209 = 0 and I00004 = 0 then // waits for part present then send trigger to cognex camera, seals in circuit until part leaves
		Q00001 := 1;
		Camera1_Step := Camera1_Step + 1;
		if Camera1_Step = 10 then
			Camera1_Step := 0;
			end_if;
	end_if;
	
	if Camera1UpdateFail and I00021 then // if there is a failure from the cognex system it sends signal to conveyor PLC to send to reject
		M01194 := 1;
	end_if;
	
		if Camera1_Step = 1 then // shift camera data by one position every trigger
 	Camera1Data10 := Camera1Data9;
 	end_if;
 	

	if Camera1_Step = 2 then
 	Camera1Data9 := Camera1Data8;
	end_if;

	if Camera1_Step = 3 then
	Camera1Data8 := Camera1Data7;
	end_if;  
	
	if Camera1_Step = 4 then
	Camera1Data7 := Camera1Data6;
	end_if; 
	
	if Camera1_Step = 5 then
	Camera1Data6 := Camera1Data5;
	end_if; 
	
	if Camera1_Step = 6 then
	Camera1Data5 := Camera1Data4;
	end_if; 
	
	if Camera1_Step = 7 then
	Camera1Data4 := Camera1Data3;
	end_if; 
	
	if Camera1_Step = 8 then
	Camera1Data3 := Camera1Data2;
	end_if; 
	
	if Camera1_Step = 9 then
	Camera1Data2 := Camera1Data1;
	end_if; 
	
	if Camera1_Step = 10 then
	Camera1Data := "Pass";
	Camera1Data1 := Camera1Data;
	end_if; 
	
	if Camera1_Step = 21 then
	Camera1Data10 := Camera1Data9;
	end_if; 
	
	if Camera1_Step = 22 then
	Camera1Data9 := Camera1Data8;
	end_if; 
	
	if Camera1_Step = 23 then
	Camera1Data8 := Camera1Data7;
	end_if; 
	
	if Camera1_Step = 24 then
	Camera1Data7 := Camera1Data6;
	end_if; 
	
	if Camera1_Step = 25 then
	Camera1Data6 := Camera1Data5;
	end_if; 
	
	if Camera1_Step = 26 then
	Camera1Data5 := Camera1Data4;
	end_if; 
	
	if Camera1_Step = 27 then
	Camera1Data4 := Camera1Data3;
	end_if; 
	
	if Camera1_Step = 28 then
	Camera1Data3 := Camera1Data2;
	end_if; 
	
	if Camera1_Step = 29 then
	Camera1Data2 := Camera1Data1;
	end_if; 
	
	if Camera1_Step = 30 then
	Camera1Data := "Fail";
	Camera1Data1 := Camera1Data;
	end_if; 