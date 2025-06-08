#include<bits/stdc++.h>
using namespace std;
#define y1 yyyy

const int MAX = 301;
const int SEP = 1000;
const int dx[4] = {0, 1, 0, -1};
const int dy[4] = {1, 0, -1, 0};
char graph[MAX][MAX];
int N, M, x1, y1, x2, y2, cnt, visited[MAX][MAX];
queue<int> q;

int main() {
    scanf("%d %d", &N, &M);
    scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
    y1--; x1--; y2--; x2--;
    for (int i=0; i<N; i++) {
        scanf("%s", graph[i]);
    }
    q.push(SEP*y1+x1);
    visited[y1][x1] = 1;
    while (graph[y2][x2] != '0') {
        cnt++;
        queue<int> tmp;
        while (q.size()) {
            int y = q.front() / SEP;
            int x = q.front() % SEP;
            q.pop();
            for (int i=0; i<4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (ny < 0 || nx < 0 || ny >= N || nx >= M || visited[ny][nx]) continue;
                visited[ny][nx] = cnt;
                if (graph[ny][nx] != '0') {
                    graph[ny][nx] = '0';
                    tmp.push(SEP * ny + nx);
                } else {
                    q.push(SEP * ny + nx);
                }
            }
        }
        q = tmp;
    }
    printf("%d\n", visited[y2][x2]);

    return 0;
}
