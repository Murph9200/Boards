(*************************************
  Created: Tuesday, September 30, 2024

  Description:

*************************************)

//List of call stations that determine route call for each tugger

Station1PB := I00001;
Station2PB := I00002;
Station3PB := I00003;
Station4PB := I00004;
Q00001 := GotoStation1;
Q00002 := GotoStation2;
Q00003 := GotoStation3;


//Intersection zone sensors from tugger
if I00005 = 1 then
	Zone1Active := 1;
end_if;

if I00006 = 1 then
	Zone2Active := 1;
end_if;

//monitors tugger being at start position
if I00007 = 1 then
	TuggerHome := 1;
end_if;

//tugger has assignment monitor
if I00008 = 1 then
	TuggerHasRoute := 1;
end_if;


// respond to Station1 request to get parts
if Station1PB and TuggerHome and TuggerHasRoute = 0 and Zone1Active = 0 then
	GotoStation1 := 1;
end_if;

// respond to Station1 request to get parts
if Station2PB and TuggerHome and TuggerHasRoute = 0 and Zone2Active = 0 then
	GotoStation2 := 1;
end_if;                                            

// respond to Station1 request to get parts
if Station3PB and TuggerHome and TuggerHasRoute = 0 and Zone3Active = 0 then
	GotoStation3 := 1;
end_if;
