#pragma once
#include <iostream>
#include <string>
#include <ctime>
#include "feature.h"
using namespace std;

class Alarm : public Feature {
    public:
        s_time Finish;
        s_time Diff;
        void SetValue(s_time);
        void Update();
        Alarm();
};

Alarm::Alarm()
{
    Name = "Alarm";
    Finish = {0,0,0,0}; 
    Diff = {0,0,0,0}; 
    preprintmsg = "Time to "; 
    endmsg = "Alarm Passed"; 
    killmsg = "Deleting Alarm";
}
void Alarm::SetValue(s_time rec_time)
{
    Finish = rec_time;
}

//Update Time and Time Remaining
void Alarm::Update()
{
    GetSysTime();
    Diff = SubTime(Finish,Time);
    PrintTime = Diff;
}