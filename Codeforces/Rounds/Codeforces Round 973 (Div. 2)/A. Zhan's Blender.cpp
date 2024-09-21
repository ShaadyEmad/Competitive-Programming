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
    int t; cin>>t;
    while (t--)
    {
        long long n; cin>>n;
        long long x,y; cin>>x>>y;  
        cout << (long long) ceil((double)n/min(x,y))<< endl;
    }
    return 0;
}
