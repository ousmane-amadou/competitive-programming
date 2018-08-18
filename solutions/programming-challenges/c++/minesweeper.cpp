#include <iostream>
using namespace std;

const int MINE = -1;

/* Calculate the number of mines adjacent to the specified
square.

Precondition (s):
(1) mine_field != null
(2) 0 < square[0] <= size(mine_field)
(3) 0 < square[1] <= size(mine_field[0])
*/
int adj_mines(int mine_field[][], int square[]) {

}

int n, m;         // Represents the number of rows and columns in input matrix
int mine_field[100][100];       // Represents the input matrix
int adjcancey_field[100][100];      // Represents the output matrix
int main() {

  scanf("%d %d", &n, &m);

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (mine_field[i][j] != MINE) {
        adjcancey_field[i][j] = adj_mines(mine_field, {i, j});
      } else {
        adjcancey_field[i][j] = MINE;
      }
    }
  }
}
