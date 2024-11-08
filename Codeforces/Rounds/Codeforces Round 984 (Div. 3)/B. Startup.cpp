#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <utility>
#include <iomanip>
# include <numeric>
using namespace std;

int main(){
    int t; cin>>t;
    while (t--)
    {
        int shelves,bottles; cin>>shelves>>bottles;
        vector<int> costs(bottles);

        for(int i=0; i<bottles; i++){
            int a,b; cin>>a>>b;
            a-=1;
            costs[a] +=b;
        }
        sort(costs.rbegin(),costs.rend());
        cout<<accumulate(costs.begin(), costs.begin()+min(shelves,bottles),0) << endl;

    }
    return 0;
}
