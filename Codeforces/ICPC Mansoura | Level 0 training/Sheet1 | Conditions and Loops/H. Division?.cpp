# include <iostream>
#include <algorithm>
using namespace std;

int main(){
    long long n, a;
    cin >> n;
    while (n!=0){
        cin >> a;
        if (a >= 1900){
            cout << "Division 1\n";
        }
        else if(1899 >= a && a >= 1600){
            cout << "Division 2\n";
        }
        else if(1599 >= a && a >= 1400){
            cout << "Division 3\n";
        }
        else{
            cout << "Division 4\n";
        }
        n--;
    }
    return 0;
}
