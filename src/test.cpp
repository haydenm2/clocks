#include <iostream>
#include <string>
#include <ctime>
#include "feature.h"
#include "alarm.h"
#include "clock.h"
#include "timer.h"
#include "stopwatch.h"
using namespace std;

//ALARM TESTS
int main()
{
    Feature feat;
    feat.SetName("TestFeature");
    feat.Activate();
    feat.Execute();

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

    cout << "\033[1;92m-----TEST COMPLETE-----\033[0m" << endl;
    return 0;
}