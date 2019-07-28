#pragma once
#include <iostream>
#include <string>
#include <ctime>
#include <unistd.h>
#include "feature.h"
#include "alarm.h"
#include "clock.h"
#include "timer.h"
#include "stopwatch.h"
using namespace std;

class Interface {
    public:
        Interface();
        ~Interface();
        Alarm *ptrAlarm;
        Clock *ptrClock;
        Stopwatch *ptrStopwatch;
        Timer *ptrTimer; 
        void SetFeatureName(string name); //set name of feature
        void SetFeatureValue(Feature::s_time Value); //set value of feature
        void StartFeature(); //Turn on feature
        void PauseFeature(); //Pause feature
        void LapFeature(); //Record feature lap
        void StopFeature(); //Turn off feature
        void ShowFeature(); //Toggle feature display on
        void HideFeature(); //Toggle feature display off
        void ResetFeature(); //Reset feature properties
        void NextFeature(); //Iterate to next active feature
        void Execute(); //execution loop
    private:
        void ExecuteFeatures(); //Update feature values
        int iterFeature; //Feature iterator
        Feature *CurrentFeature; //Feature target
};

Interface::Interface()
{
    static Alarm al;
    static Clock cl;
    static Stopwatch sw;
    static Timer tmr;
    ptrAlarm = &al;
    ptrClock = &cl;
    ptrStopwatch = &sw;
    ptrTimer = &tmr;
    iterFeature = 0;
    CurrentFeature = ptrClock;
    CurrentFeature->SetShow();
}

Interface::~Interface()
{
    cout << "\033[1m\033[91m[" << "Killing Interface" << "]\033[0m" << endl;
}

void Interface::SetFeatureName(string name)
{
    CurrentFeature->SetName(name);
}

void Interface::SetFeatureValue(Feature::s_time Value)
{
    CurrentFeature->SetValue(Value);
}

void Interface::StartFeature()
{
    CurrentFeature->cStart=true;
}


void Interface::PauseFeature()
{
    CurrentFeature->cPause=true;
}


void Interface::LapFeature()
{
    CurrentFeature->cLap=true;
}


void Interface::StopFeature()
{
    CurrentFeature->Deactivate();
}


void Interface::ShowFeature()
{
    CurrentFeature->SetShow();
}


void Interface::HideFeature()
{
    CurrentFeature->SetHide();
}

void Interface::ResetFeature()
{
    CurrentFeature->cReset = true;
}

void Interface::NextFeature()
{
    if(iterFeature == 0)
    {
        CurrentFeature->SetHide();
        // Alarm *CurrentFeature = static_cast <Alarm *> (CurrentFeature);
        CurrentFeature = ptrAlarm;
        CurrentFeature->SetShow();
        iterFeature = 1;
    }
    else if(iterFeature == 1)
    {
        CurrentFeature->SetHide();
        // Stopwatch *CurrentFeature = static_cast <Stopwatch *> (CurrentFeature);
        CurrentFeature = ptrStopwatch;
        CurrentFeature->SetShow();
        iterFeature = 2;
    }
    else if(iterFeature == 2)
    {
        CurrentFeature->SetHide();
        // Timer *CurrentFeature = static_cast <Timer *> (CurrentFeature);
        CurrentFeature = ptrTimer;
        CurrentFeature->SetShow();
        iterFeature = 3;
    }
    else if(iterFeature == 3)
    {
        CurrentFeature->SetHide();
        // Clock *CurrentFeature = static_cast <Clock *> (CurrentFeature);
        CurrentFeature = ptrClock;
        CurrentFeature->SetShow();
        iterFeature = 0;
    }
}

void Interface::ExecuteFeatures()
{
    ptrClock->Execute();
    ptrAlarm->Execute();
    ptrStopwatch->Execute();
    ptrTimer->Execute();
}

void Interface::Execute()
{
    ExecuteFeatures();
}


