#pragma once
#include <iostream>
#include <string>
#include <ctime>
#include <unistd.h>
#include "feature.h"
using namespace std;

class Stopwatch : public Feature
{
    public:
        Stopwatch();
        s_time Elapsed;
        s_time Start;
        bool cPause;
        bool cLap;
        s_time Laps[100];
        int lap_iter;
        void Update();
        void CheckFlags();
        void Activate();
        void Pause();
        void Lap();
};

Stopwatch::Stopwatch()
{
    Name = "Stopwatch";
    Start = {0,0,0};
    Elapsed = {0,0,0};
    cPause = false;
    cLap = false;
    killmsg = "Deleting Stopwatch";
    lap_iter = 0;
}

//Update Time and Elapsed Time 
void Stopwatch::Update()
{
    GetSysTime();
    Elapsed = SubTime(Time,Start);
    PrintTime = Elapsed;
}

//Turn on Stopwatch and Initialize Offset Start Time
void Stopwatch::Activate()
{
    On = true;
    GetSysTime();
    Start = SubTime(Time,Elapsed);
}

//Pause Stopwatch
void Stopwatch::Pause()
{
    On = false;
}

//Record Lap Time in Container
void Stopwatch::Lap()
{
    Laps[lap_iter] = Elapsed;
    lap_iter++; 
}