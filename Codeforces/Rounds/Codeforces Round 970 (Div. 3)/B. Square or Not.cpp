# include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
using namespace std;

int main(){
    int t; cin>>t;
    while(t--){
        int l, root, borders, zeros, zeros_count;
        string s;
        cin >> l >> s;
        root = sqrt(l);
        // check if square
        if (root*root != l){
            cout << "NO"<< endl;
        }
        else{
            borders = 4*(root - 1);
            zeros = l-borders;
            zeros_count = count(s.begin(), s.end(), '0');
            if (borders == l || zeros_count==zeros) cout << "YES"<< endl;
            else cout << "NO"<< endl;
        }
    }
    return 0;
}
