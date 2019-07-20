#pragma once
#include <iostream>
#include <string>
#include <ctime>
#include <unistd.h>
#include "feature.h"

using namespace std;

class Clock : public Feature
{
    public:
        Clock();
        bool Name;
        string killmsg;
};

Clock::Clock()
{
    Name = "Clock";
    killmsg = "Deleting Clock";
}