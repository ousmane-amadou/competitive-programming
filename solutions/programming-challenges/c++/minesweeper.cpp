/*
Programming Challenges; 1.6.2 Minesweeper
Problem Type: Ad hoc
*/
#include <iostream>
using namespace std;

const int MAX_SIZE = 100;
const int EMPTY = 1;
const int MINE = -1;

/* Calculate the number of mines adjacent to the specified
square.

Precondition (s):
(1) mine_field != null
(2) 0 < square[0] <= size(mine_field)
(3) 0 < square[1] <= size(mine_field[0])
*/
int adj_mines(int *mine_field, int square[]) {
  int row = square[0];
  int col = square[1];
  int num_mines = 0;

  if (*mine_field)[row+1][col] == MINE) {
    num_mines++;
  }

  if (mine_field[row][col + 1] == MINE) {
    num_mines++;
  }

  if (col != 0) {
    if (mine_field[row][col - 1] == MINE) {
      num_mines++;
    }
  }

  if (row != 0) {
    if (mine_field[row - 1][col] == MINE) {
      num_mines++;
    }
  }
  return num_mines;
}

// Self notes
// 1. Arrays size must be known at compile time
// 2. Items in an array are defult initialized.
// 3. Array literals: {1, 2, 3, 4}

int n, m; // Represents the number of rows and columns in input matrix
int mine_field[MAX_SIZE][MAX_SIZE];      // Represents the input matrix
int adjcancey_field[MAX_SIZE][MAX_SIZE]; // Represents the output matrix

int main() {
  char input;
  scanf("%d %d", &n, &m);
  // Step 1: Process Input Matrix (mine_field)
  // Runtime complexity: O(1)
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> input;
      if (input == '*') {
        mine_field[i][j] = MINE;
      } else {
        mine_field[i][j] = EMPTY;
      }
    }
  }

  // Step 2: Calculate Output Matrix (adjacency_field)
  // Runtime complexity: 0(1)
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (mine_field[i][j] != MINE) {
        adjcancey_field[i][j] = adj_mines(mine_field, {i, j});
      } else {
        adjcancey_field[i][j] = MINE;
      }
    }
  }
}
