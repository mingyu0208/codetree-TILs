#include <stdio.h>

int main() {
    int arr[10];
    for (int i=0; i<10; i++){
        scanf("%d", &arr[i]);
    }
    printf("%d", arr[2]+arr[4]+arr[9]);
    
    
    return 0;
}