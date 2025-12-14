// Problem 2 : Queue : sliding window maximum 

#include <stdio.h>

int main() {
    int arr[] = {1, 3, -1, -3, 5, 3, 6, 7};
    int n = 8, k = 3;

    int dq[20];
    int front = 0, rear = -1;

    for (int i = 0; i < n; i++) {

        // Remove elements outside window
        if (front <= rear && dq[front] <= i - k)
            front++;

        // Remove smaller elements
        while (front <= rear && arr[dq[rear]] < arr[i])
            rear--;

        // Add current index
        dq[++rear] = i;

        // Print max when window is ready
        if (i >= k - 1)
            printf("%d ", arr[dq[front]]);
    }

    return 0;
}
