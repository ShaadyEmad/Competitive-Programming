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
    int ans = 0;
    while(t--){
        int a,b,c;
        cin>>a>>b>>c;
        if (a+b+c >= 2){
            ans+=1;
        }
    }
    cout<<ans;
    return 0;
}
