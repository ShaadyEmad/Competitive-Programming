# include <iostream>
using namespace std;

int main(){
    int a,b,c;
    cin >> a >> b >> c;
    if (a+b>=a+c && a+b>=b+c && a+b>=a+c){
        cout << a+b;
    }
    else if (a+c>=a+b && a+c>=a+b && a+c>=b+c){
        cout << a+c;
    }
    else{
        cout << b+c;
    }
    return 0;
}
