# include <iostream>
#include <algorithm>
using namespace std;

int main(){
    long long a1,b1,a2,b2;
    cin >> a1 >> b1 >> a2 >> b2;
    if (b1 < a2 && a1<a2){
        cout << -1;
    }
    else{
        cout << max(a1,a2) << " " << min(b1,b2);
    }
    
    return 0;
}
