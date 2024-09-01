# include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main(){
    int t; cin>>t;
    while(t--){
        int l, r;
        cin >> l >> r;
        long long max_sum = r-l;
        long long k = (long long)(-1 + sqrt(1 + 8 * max_sum)) / 2;
        cout << k+1 << endl;
    }
    return 0;
}
