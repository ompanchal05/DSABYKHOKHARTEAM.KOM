// Problem 3 : Linked list - Detect loop

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int detectLoop(struct Node* head) {
    struct Node *slow = head, *fast = head;

    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;          // 1 step
        fast = fast->next->next;    // 2 steps

        if (slow == fast)
            return 1;   // Loop found
    }
    return 0;           // No loop
}
