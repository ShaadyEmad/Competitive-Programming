#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <utility>
using namespace std;

int main(){
    int t; cin>>t;
    while(t--){
        long long a,b,c;
        cin>>a>>b>>c;
        if (a+b==c || a+c==b || b+c==a){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
    return 0;
}
