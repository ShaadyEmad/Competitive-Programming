# include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

int main(){
    int t; cin>>t;
    while(t--){
        int x,y,k; 
        cin>>x>>y>>k;  
        int a = (x+k-1)/k;
        int b = (y+k-1)/k;
        if (a>b){
            cout<<2*a-1<<endl;
        }
        else{
            cout<<2*b<<endl;
        }
    }
    return 0;
}
