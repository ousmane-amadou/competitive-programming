#include <iostream>

using namespace std;

const int MAX_SIZE  = 100;

typedef struct {
  int items[MAX_SIZE];  // Contents of stack
  int first;  // Index of first element in stack
  int last;   // Index of last element in stack
  int size;   // Size of stack
} stack;

void initStack(stack *s);
bool isFull(stack *s);
bool isEmpty(stack *s);
void push(stack* s, int item);
int pop(stack*s);

int main() {}
