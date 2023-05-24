#include <iostream>
using namespace std;
void maxHeap(int *a,int i,int n){
    int largest=i;
    int left=2*i+1;
    int right=2*i+2;
    
    if(left<n && a[largest]<a[left]){
        largest=left;
    }
    
    if(right<n && a[largest]<a[right]){
        largest=right;
    }
    
    if(largest!=i){
        swap(a[largest],a[i]);
        maxHeap(a,largest,n);
    }
}

void minHeap(int *a,int i,int n){
    int largest=i;
    int left=2*i;
    int right=2*i+1;
    
    if(left<n && a[largest]>a[left]){
        largest=left;
    }
    
    if(right<n && a[largest]>a[right]){
        largest=right;
    }
    
    if(largest!=i){
        swap(a[largest],a[i]);
        minHeap(a,largest,n);
    }
}
void build_min(int *a,int n){
    for(int i=n/2;i>=0;i--){
        minHeap(a,i,n);
    }
}

void build_max(int *a,int n){
    for(int i=n/2;i>=0;i--){
        maxHeap(a,i,n);
    }
}

int main(){
    int n;
    cout<<"Enter the number of elements"<<endl;
    cin>>n;
    int a[n];
    
    for(int i=0;i<n;i++){
       cin>>a[i]; 
    }
    int ch;
    do{
        cout<<"Enter choice:-\n 1)Min Heap 2)Max heap"<<endl;
        cin>>ch;
        switch(ch){
            case 1:
               build_min(a,n);
               for(int i=0;i<n;i++){
                   cout<<a[i]<<" ";
               }
               cout<<endl; 
               break;
             case 2:
               build_max(a,n);
               for(int i=0;i<n;i++){
                   cout<<a[i]<<" ";
               } cout<<endl;  
               break;
        }
    }while(ch<=2);
    return 0;
}
