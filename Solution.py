#include <bits/stdc++.h>

using namespace std;

void solution() {
     int n, z;
     cin>>n;
     for(int i=0; i<n; i++){
         cin>>z;
         if(z>=38 && z%5>=3){
            while(z%5!=0){
                z++;
                }
            } 
            cout<<z<<"\n";
        }  
    }
    int main () {
        solution(); 
        return 0;        
} 
