# include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main(){
    int t; cin>>t;
    while(t--){
        int a, b, min;
        min =99999;
        cin >> a >> b;
        for(int n = a; n<=b; n++){
            int current_min =  (n-a)+(b-n);
            if (current_min<min){
                min = current_min;
            }
        }
        cout << min << endl;
    }
    return 0;
}
