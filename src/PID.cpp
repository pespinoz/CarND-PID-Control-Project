#include <array>
#include "PID.h"
#include <chrono>

using namespace std;

/*
* TODO: Complete the PID class.
*/

PID::PID() {}

PID::~PID() {}

void PID::Init(double Kp, double Ki, double Kd) {
    this->Kp = Kp;
    this->Ki = Ki;
    this->Kd = Kd;

    p_error = 0.0;
    i_error = 0.0;
    d_error = 0.0;
}

void PID::UpdateError(double cte, double delta_timestamp) {
    d_error = (cte - p_error) / delta_timestamp;
    p_error = cte;
    i_error += cte;
}

double PID::TotalError() {
    double control_value = Kp*p_error + Kd*d_error + Ki*i_error;
    if(control_value > 1){
        control_value = 1.0;
    }else if(control_value < -1){
        control_value = -1.0;
    }
    return control_value;
}
