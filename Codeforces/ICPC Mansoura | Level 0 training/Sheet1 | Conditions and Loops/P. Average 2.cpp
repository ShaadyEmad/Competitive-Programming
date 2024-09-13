#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <utility>
#include <iomanip>
using namespace std;


int main(){
    float a,b,c;
    cin>>a>>b>>c;
    float average = (a*2+b*3+c*5)/10;
    cout<<fixed<<setprecision(1)<<"MEDIA = "<<average;
    return 0;
}
