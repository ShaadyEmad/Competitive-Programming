# include <iostream>
#include <algorithm>
using namespace std;

int main(){
    int t; cin>>t;
    while(t--){
        int a, b;
        cin >> a >> b;
        if(!a){
            if(b%2==0) cout<<"YES"<<endl;
            else cout<<"No"<<endl;
        }
        else{
            if (a%2==0) cout<<"YES"<<endl;
            else cout<<"No"<<endl;
        }   
    }
    return 0;
}
