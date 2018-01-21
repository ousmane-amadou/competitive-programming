#include <iostream>

using namespace std;

const int MAX_SIZE  = 100;

typedef struct {
  int items[MAX_SIZE];  // Contents of stack
  int first;            // Index of first element in stack
  int last;             // Index of last element in stack
  int size;             // Size of stack
} stack;

void initStack(stack *s) {
  // Initialize a new stack with empty attributes.
  s->first = 0;
  s->last = 0;
  s->size = 0;
}
bool isFull(stack *s) { return (s->size >= MAX_SIZE); }
bool isEmpty(stack *s) { return (s->size == 0); }

void push(stack* s, int item) {
  if (s->size < MAX_SIZE) {
    s->items[++s->size] = item;
    s->last = s->size;
  }
}
int pop(stack*s) {
  if(s->size > 0) {
    int i = s->items[s->size];
    s->items[s->size] = 0; // Delete top item
    s->size--; s->last--;
    return i;
  } return -1;
}

int main() {}
