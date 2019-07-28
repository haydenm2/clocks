#include <iostream>
#include <string>
#include <ctime>
#include "feature.h"
#include "alarm.h"
#include "clock.h"
#include "timer.h"
#include "stopwatch.h"
#include "interface.h"
using namespace std;

//ALARM TESTS
int main()
{
    // INTERFACE TESTS
    Feature::s_time t_pass = {23,59,0}; //9:15pm
    Interface inter;
    inter.SetFeatureName("TestClock");
    inter.SetFeatureValue(t_pass);
    inter.StartFeature();
    for(int i = 0; i<20; i++)
    {
        inter.Execute();
    }
    inter.NextFeature();
    inter.SetFeatureName("TestAlarm");
    inter.SetFeatureValue(t_pass);
    inter.StartFeature();
    for(int i = 0; i<20; i++)
    {
        inter.Execute();
    }
    inter.NextFeature();
    inter.SetFeatureName("TestStopwatch");
    Feature::s_time t_time = {0,2,3};
    inter.SetFeatureValue(t_time);
    inter.StartFeature();
    for(int i = 0; i<20; i++)
    {
        inter.Execute();
    }
    inter.NextFeature();
    inter.SetFeatureName("TestTimer");
    inter.SetFeatureValue(t_time);
    inter.StartFeature();
    for(int i = 0; i<20; i++)
    {
        inter.Execute();
    }
    inter.NextFeature();
    for(int i = 0; i<10; i++)
    {
        inter.Execute();
    }
    inter.NextFeature();
    for(int i = 0; i<10; i++)
    {
        inter.Execute();
    }
    inter.NextFeature();
    for(int i = 0; i<10; i++)
    {
        inter.Execute();
    }
    
    // // FEATURE TESTS
    // Feature feat;
    // feat.SetName("TestFeature");
    // feat.Activate();
    // feat.Execute();

    // // ALARM TESTS
    // Alarm al;
    // al.SetName("TestAlarm");
    // Feature::s_time t_pass = {21,15,0}; //9:15pm
    // al.SetValue(t_pass);
    // al.Activate();
    // al.Execute();

    // // CLOCK TESTS
    // Clock cl;
    // cl.SetName("TestClock");
    // Feature::s_time t_pass = {0,0,5};
    // cl.SetValue(t_pass);
    // cl.Activate();
    // cl.Execute();

    // //TIMER TESTS
    // Timer tmr;
    // tmr.SetName("TestTimer");
    // Feature::s_time t_pass = {0,0,5};
    // tmr.SetValue(t_pass);
    // tmr.Activate();
    // tmr.Execute();

    // // STOPWATCH TESTS
    // Stopwatch sw;
    // sw.SetName("TestStopwatch");
    // sw.Activate();
    // sw.Execute();

    cout << "\033[1;92m-----TEST COMPLETE-----\033[0m            " << endl;
    return 0;
}