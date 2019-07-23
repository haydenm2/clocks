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
        struct s_time{
            int hour;
            int min;
            int sec;
            int msec;
        };
        Interface();
        ~Interface();
        s_time TimeInput;
        string StringInput;
        void CreateFeature(Feature::Feature); //create instance
        void SetFeatureName(string name); //set name of feature
        void SetFeatureValue(s_time Value); //set value of feature
        void StartFeature(Feature::Feature); //Turn on feature
        void PauseFeature(Feature::Feature); //Pause feature
        void LapFeature(Feature::Feature); //Record feature lap
        void StopFeature(Feature::Feature); //Turn off feature
        void ShowFeature(Feature::Feature); //Toggle feature display on
        void HideFeature(Feature::Feature); //Toggle feature display off
        void ResetFeature(Feature::Feature); //Reset feature properties
        void Execute(); //execution loop
    private:
        void UpdateFeatures(); //Update feature values
};

Interface::Interface()
{
    TimeInput = {0,0,0};
    StringInput = "";
}

Interface::~Interface()
{
    cout << "\033[1m\033[91m[" << Name << "]: " << killmsg << "\033[0m" << endl;
}


void Interface::CreateFeature(Feature::Feature)
{

}

void Interface::SetFeatureName(string name)
{

}


void Interface::SetFeatureValue(Interface::s_time Value)
{

}


void Interface::StartFeature(Feature::Feature)
{

}


void Interface::PauseFeature(Feature::Feature)
{

}


void Interface::LapFeature(Feature::Feature)
{

}


void Interface::StopFeature(Feature::Feature)
{

}


void Interface::ShowFeature(Feature::Feature)
{

}


void Interface::HideFeature(Feature::Feature)
{

}


void Interface::ResetFeature(Feature::Feature)
{

}


void Interface::UpdateFeatures()
{

}


