#pragma once
#include <iostream>
#include <string>
#include <ctime>
#include <unistd.h>
#include "feature.h"

class Timer : public Feature
{
    public:
        Timer();
        s_time Diff;
        s_time Finish;
        s_time Length;
        void SetValue(s_time Value);
        void Update();
        void CheckFlags();
        s_time AddTime(s_time Time1, s_time Time2);
        void Activate();
        void Pause();
};

Timer::Timer()
{
    Name = "Timer";
    Diff = {0,0,0};
    Finish = {0,0,0};
    Length = {0,0,0};
    cPause = false;
    endmsg = "Timer Passed";
    killmsg = "Deleting Timer";
}

//Set Length of Timer
void Timer::SetValue(s_time Value)
{
    Length = Value;
}

//Update Time and Time Remaining  
void Timer::Update()
{
    GetSysTime();
    Diff = SubTime(Finish,Time);
    PrintTime = Diff;
}

//Add Two Time Arrays
Timer::s_time Timer::AddTime(s_time Time1, s_time Time2)
{
    s_time Add = {Time1.hour+Time2.hour,Time1.min+Time2.min,Time1.sec+Time2.sec};
    if(Add.sec>60)
    {
        Add.sec=Add.sec%60;
        Add.min=Add.min+(Add.min/60);
    }
    if(Add.min>60)
    {
        Add.min=Add.min%60;
        Add.hour=Add.hour+(Add.hour/60);
    }
    if(Add.hour>23)
    {
        Add.hour=Add.hour%24;
    }
    return Add;
}

//Turn on Timer and Redefine Finish Time
void Timer::Activate()
{
    On = true;
    GetSysTime();
    Finish = AddTime(Time,Length);
}

//Pause Timer
void Timer::Pause()
{
    Length=Diff;
    On = false;
}