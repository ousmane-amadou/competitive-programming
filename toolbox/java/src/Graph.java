import java.lang.reflect.Array;
import java.util.ArrayList;

public class Graph {
  public static final int MAX_VERTICES = 100;
  public static final int MAX_DEGREE = 50;

  private ArrayList<Integer> a[];
  private int[][] edges;
  private int[] degree;
  private int num_vertices;
  private int num_edges;

  public Graph() {
    this.edges = new int[MAX_VERTICES + 1][MAX_DEGREE];
    this.degree = new int[MAX_VERTICES + 1];
    this.num_vertices = 0;
    this.num_edges = 0;
  }


  /**
   * Add an edge between node x, and node y.
   *
   * @param x source node.
   * @param y destination node.
   * @return true if the edge was inserted without error, false otherwise.
   */
  public boolean insert_edge(int x, int y, boolean directed) {

    if (this.degree[x] >= MAX_DEGREE) {
      System.out.printf("Warning: insertion(%d,%d) exceeds max degree\n", x, y);
      return false;
    }

    this.edges[x][this.degree[x]] = y;
    this.degree[x]++;

    if (directed == false) {
        insert_edge(y, x, true);
    } else {
        this.num_edges++;
    }

    return true;
  }

  public String toString() {
      StringBuilder representation = new StringBuilder();
      int i,j;

      for (i=1; i<=this.num_vertices; i++) {
          representation.append(i);

      }

      return representation.toString();
  }

}
