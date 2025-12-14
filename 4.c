// Problem 4 : Binary Tree - Height & Diameter 

#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* left;
    struct Node* right;
};

int max(int a, int b) {
    return a > b ? a : b;
}

// Function to calculate height and update diameter
int height(struct Node* root, int* diameter) {
    if (root == NULL)
        return 0;

    int lh = height(root->left, diameter);
    int rh = height(root->right, diameter);

    // Update diameter
    if (lh + rh > *diameter)
        *diameter = lh + rh;

    return 1 + max(lh, rh);
}
