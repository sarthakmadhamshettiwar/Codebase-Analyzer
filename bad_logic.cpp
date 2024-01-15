#include<iostream.h>
using namespace std;
int main()
{
  int n;
cin>>n;

int arr[n-1];
for(int i=0; i<n-1; i++){
cin>>arr[i];
}

int sum = 0;
      for(int i=0; i<n; i++){
sum += arr[i];
}
cout<<sum/n-1;

return 0;
}
