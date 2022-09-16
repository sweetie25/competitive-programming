#include <iostream>
using namespace std;
int main()
{
    int m,n,squares;
    cout<<"Please Enter a number";
    cin>>m>>n;
    
    int area=m*n;
    int num2 = m%2;
    
     if (area%2==0)
     { 
       squares=area/2;
       cout<<squares;
     }
     else
     {
        squares=(area-1)/2;
        cout<<squares;
     }

    return 0;
}
