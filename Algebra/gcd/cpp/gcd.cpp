#include <iostream>
using namespace std;

int main(){
    int num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;   
    while(num1 != num2){
        if(num1 > num2)
            num1 -= num2;
        else
            num2 -= num1;
    }
    cout << "HCF = " << num1;
    return 0;
}
