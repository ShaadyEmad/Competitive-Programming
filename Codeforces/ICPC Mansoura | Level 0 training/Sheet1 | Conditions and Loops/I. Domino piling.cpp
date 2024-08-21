# include <iostream>
#include <algorithm>
using namespace std;

int main(){
    double r, fractional_part;
    int m, n, result, int_part;
    cin >> m >> n;
    r = m/2.0;
    int_part  = int(r);
    fractional_part = r-int_part;
    result = (fractional_part * n) + (int_part * n);
    cout<<result;
    return 0;
}
