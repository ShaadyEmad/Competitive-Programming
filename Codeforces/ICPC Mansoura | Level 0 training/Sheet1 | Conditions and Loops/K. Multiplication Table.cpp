# include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <utility>
using namespace std;

int main(){
    int n; cin>>n;
    int t=1;
    for(int i =1; i<11; i++){
        cout<< i << " x " << n << " = " << i*n << endl;
    }
    return 0;
}
