(*************************************
  Created: Monday, September 29, 2024

  Description:

*************************************)

if TestPP = 1 then // conveyor part present
	Andon1_PP := 1;
else
	Andon1_PP := 0;
end_if;

if Andon_CycleTimePremissive = 1 and Andon1_CycleComplete = 0 and Andon1_PP = 1 then // sets start signal of cycle time
	Andon1_CycleTimeStart := 1;
end_if;

if TestPulCord = 1 then // sets cycle time reset high
	Andon1_CycleComplete := 1;
end_if;

if Andon1_CycleTimeStart = 1 then // looks at start signal to start cycle time
	Andon1_CycleTimeStartOns := 1;
end_if;

if Andon1_CycleTimeStartOns = 1 then // one shot to start cycle time
	Andon1_CycleTimeLast := Andon1_CycleTimeCurrent;
end_if;

Andon1_CycleTimeCurrent := Andon1_CycleTimeAcc / 10; // moving decimal places on current cycle time

if 	Andon1_CycleTimeReset = 1 then // resets cycle time percentage
	Andon1_CycleTimePercentage := 0;
end_if;

if Andon1_CycleTimePercentage < Andon_AudibleAlarm then // calculates the elasped cycletime in %
	(Andon1_CycleTimeCurrent / Andon_TaktTime) * 100 = Andon1_CycleTimePercentage;
end_if;

if Andon_CycleTimePermissive and Andon1_CycleComplete or Andon1_CycleTimeStart and Andon1_CycleTimePercentage < Andon_GreenLight then // turns green light on
	Andon1_GreenLight := 1;
end_if;

if Andon_CycleTimePermissive and Andon1_CycleComplete and Andon1_CycleTimePercentage > Andon_GreenLight and Andon1_CycleTimePercentage < Andon_YellowLight then // turns yellow light on
	Andon1_YellowLight := 1;
end_if;

if Andon_CycleTimePermissive and Andon1_CycleComplete and Andon1_CycleTimePercentage > Andon_RedLight then // turns red light on
	Andon1_RedLight := 1;
end_if;
