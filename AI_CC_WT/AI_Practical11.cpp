#include <iostream>
#include <queue>
using namespace std;

class graph {
    int v;
    int** adj;
public:
    graph(int v);
    void addedge(int v, int w);
    void dfs(int v, bool visited[]);
    void bfs(int s);
};

graph::graph(int v) {
    this->v = v;
    adj = new int*[v];
    for (int i = 0; i < v; i++) {
        adj[i] = new int[v];
        for (int j = 0; j < v; j++)
            adj[i][j] = 0; // initially no edges
    }
}

void graph::addedge(int v, int w) {
    adj[v][w] = 1;
    adj[w][v] = 1; // for undirected graph
}

void graph::dfs(int v, bool visited[]) {
    visited[v] = true;
    cout << v << " ";
    for (int u = 0; u < this->v; u++) {
        if (adj[v][u] && !visited[u])
            dfs(u, visited);
    }
}

void graph::bfs(int s) {
    bool* visited = new bool[v]{false};
    queue<int> q;
    visited[s] = true;
    q.push(s);

    while (!q.empty()) {
        int v = q.front();
        q.pop();
        cout << v << " ";
        for (int u = 0; u < this->v; u++) {
            if (adj[v][u] && !visited[u]) {
                visited[u] = true;
                q.push(u);
            }
        }
    }
}

int main() {
    graph g(4);
    g.addedge(0, 1);
    g.addedge(0, 2);
    g.addedge(1, 2);
    g.addedge(2, 3);

    cout << "dfs starting from vertex 2:\n";
    bool visited[4] = {false};
    g.dfs(2, visited);

    cout << "\nbfs starting from vertex 2:\n";
    g.bfs(2);

    return 0;
}
