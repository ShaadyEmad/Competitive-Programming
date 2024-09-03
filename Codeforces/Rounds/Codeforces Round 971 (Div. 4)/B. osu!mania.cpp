# include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
using namespace std;

int main(){
    int t; cin>>t;
    while(t--){
        int n; cin >> n;  
        vector<int> columns(n);
        for (int i =0; i<n; ++i){
            string row;
            cin>>row;
            columns[i] = row.find("#")+1;
        }
        for (int i =n-1; i>=0; --i){
            cout<<columns[i]<<" ";
        }
        cout<<endl;
    }
    return 0;
}
