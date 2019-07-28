#pragma once
#include <iostream>
#include <string>
#include <ctime>
#include <unistd.h>
using namespace std;

class Feature {
    public:
        struct s_time{
            int hour;
            int min;
            int sec;
            int msec;
        };
        s_time Time;
        time_t now;
        tm *ltm;
        string Name;
        bool Show;
        bool cDest;
        bool cStart;
        bool cReset;
        bool cLap;
        bool cPause;
        bool On;
        string preprintmsg;
        s_time PrintTime;
        unsigned int t_Update; //in microseconds
        string endmsg;
        string killmsg;
        Feature();
        ~Feature();
        void GetSysTime();
        void SetName(string name);
        void SetShow();
        void SetHide();
        virtual void SetValue(s_time Value);
        void Execute();
        virtual void Update();
        void Print(string title,s_time Time);
        void CheckFlags();
        s_time SubTime(s_time Time1,s_time Time2);
        s_time AddTime(s_time Time1,s_time Time2);
        virtual void Pause();
        virtual void Lap();
        virtual void Activate();
        void Deactivate();
        void Reset();
};

Feature::Feature()
{
    Time = {0,0,0};
    Name = "Feature";
    Show = true;
    cDest = false;
    cStart = false;
    cReset = false;
    cLap = false;
    cPause = false;
    On = false;
    preprintmsg = "";
    PrintTime = {0,0,0};
    t_Update = 50000; //in microseconds
    endmsg = "Invalid Subtraction";
    killmsg = "Deleting Feature";
}

Feature::~Feature()
{
    cout << "\033[1m\033[91m[" << Name << "]: " << killmsg << "\033[0m" << endl;
}


// store time from system clock
void Feature::GetSysTime()
{
    now = time(0);
    ltm = localtime(&now);
    Time.sec = ltm->tm_sec;
    Time.min = ltm->tm_min;
    Time.hour = ltm->tm_hour;
}

//Set Feature Name
void Feature::SetName(string name)
{
    Name = name;
}

//Show Print Output
void Feature::SetShow()
{
    Show = true;
}

//Hide Print Output
void Feature::SetHide()
{
    Show = false;
}

//Set Feature Value (if applicable)
void Feature::SetValue(s_time Value){}

//Execution Loop
void Feature::Execute()
{
    if(!cDest) //set to while loop for individual feature tests
    {
        if(On)
        {
            CheckFlags();
            Update();
            if(Show)
            {
                Print(preprintmsg+Name,PrintTime);
            }
        }
        else
        {
            CheckFlags();
        }
    }
}

//Variable Updates
void Feature::Update()
{
    GetSysTime();
    PrintTime = Time;
}

//Print Output
void Feature::Print(string title,s_time Time)
{
    cout << "\033[1m\033[92m[" << title << "]: \033[0m" << Time.hour << ':' << Time.min << ':' << Time.sec << "                          \r";
    cout.flush();
}

//Check for Interrupt Flags
void Feature::CheckFlags()
{
    if(cLap)
    {
        Lap();
        cLap = false;
    }
    if(cPause)
    {
        Pause();
        cPause = false;
    }
    if(cReset)
    {
        Reset();
        cReset = false;
    }
    if(cStart)
    {
        Activate();
        cStart = false;
    }
    usleep(t_Update);
}

//Subtract Two Time Arrays
Feature::s_time Feature::SubTime(s_time Time1,s_time Time2)
{
    s_time Sub = {Time1.hour-Time2.hour,Time1.min-Time2.min,Time1.sec-Time2.sec};
    if(Sub.sec<0)
    {
        Sub.min-=(1+(Sub.sec/60));
        Sub.sec+=60*(1+(Sub.sec/60));
    }
    if(Sub.min<0)
    {
        Sub.hour-=(1+(Sub.min/60));
        Sub.min+=60*(1+(Sub.min/60));
    }
    if(Sub.hour<0)
    {
        Sub={0,0,0};
        cout << "\n\033[1m\033[94m[" << Name << "]: " << endmsg << "\033[0m             " << endl;
        On = false;
    }
    return Sub;
}

Feature::s_time Feature::AddTime(s_time Time1,s_time Time2)
{}

//Pause Feature
void Feature::Pause()
{}

//Record Feature Lap
void Feature::Lap()
{}

//Activate Feature
void Feature::Activate(void)
{
    GetSysTime();
    On = true;
}

//Deactivate Feature
void Feature::Deactivate(void)
{
    On = false;
}

//Reset Feature
void Feature::Reset(void)
{
    Time = {0,0,0};
    Name = "Feature";
    Show = true;
    cDest = false;
    cStart = false;
    cReset = false;
    On = false;
    preprintmsg = "";
    PrintTime = {0,0,0};
    t_Update = 50000; //in microseconds
    endmsg = "Invalid Subtraction";
}
