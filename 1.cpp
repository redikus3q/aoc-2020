#include <fstream>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
ifstream in("1.in");
int main(){

    int x[1000];
    int i=0;
    while(in>>x[i]){
        i++;
    }
    int j=i;
    j--;
    i=0;

    for(i=0;i<j;i++){
        for(int k=0;k<j;k++){
            for(int l=0;l<j;l++){
                if(x[i]+x[k]+x[l]==2020){
                    cout<<x[i]*x[k]*x[l];
                    return 0;
                }
            }
        }
    }
    in.close();
}
