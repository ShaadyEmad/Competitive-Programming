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
    long long v,F,M,T; cin>>v>>F>>M>>T;
    while(true){
        if (v<F){
            cout << "F" << endl;
            break;
        }
        v-=F;

        if (v<M){
            cout << "M" << endl;
            break;
        }
        v-=M;

        if (v<T){
            cout << "T" << endl;
            break;
        }
        v-=T;
    }
    return 0;
}
