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
        int n; cin>>n;
        int notes[n];
        for(int i =0; i<n; ++i){
            cin>>notes[i];
        }

        string ans = "YES";
        for(int i =1; i<n; ++i){
            int sum = abs(notes[i]- notes[i-1]);
            if (sum!=5 && sum!=7){
                ans = "NO";
                break;
            }
            
        }

        cout<<ans<<endl;
    }
    return 0;
}
