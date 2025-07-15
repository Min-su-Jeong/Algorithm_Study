#include <bits/stdc++.h>
using namespace std;

const int MAX = 64;
int N, a, b, c, visited[MAX][MAX][MAX];
int damage[6][3] = {
    {1, 3, 9},
    {1, 9, 3},
    {3, 1, 9},
    {3, 9, 1},
    {9, 1, 3},
    {9, 3, 1},
};
struct A {
    int a, b, c;
};

int go(int a, int b, int c) {
    queue<A> q;
    q.push({a, b, c});
    visited[a][b][c] = 1;
    
    while (q.size()) {
        int a = q.front().a;
        int b = q.front().b;
        int c = q.front().c;
        q.pop();
        if (visited[0][0][0]) break;
        for(int i=0; i<6; i++) {
            int na = max(0, a - damage[i][0]);
            int nb = max(0, b - damage[i][1]);
            int nc = max(0, c - damage[i][2]);
            if (visited[na][nb][nc]) continue;
            visited[na][nb][nc] = visited[a][b][c] + 1;
            q.push({na, nb, nc});
        }
    }
    return visited[0][0][0] - 1;
}

int main() {
    scanf("%d", &N);
    scanf("%d %d %d", &a, &b, &c);

    cout << go(a, b, c) << '\n';
    
    return 0;
}