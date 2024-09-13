#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <utility>
using namespace std;

int main(){
    char s; cin>>s;
    int n; cin>>n;
    int arr[50];
    for (int i = 0; i<n; i++){
        int new_num; cin>>new_num; 
        arr[i]=new_num;
    }

    for (int i =0; i<n; i++){
        for(int j =0; j<arr[i]; j++){
            cout<<s;
        }
        cout<<endl;
    }
    return 0;
}
