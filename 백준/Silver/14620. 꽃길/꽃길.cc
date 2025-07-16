#include <bits/stdc++.h>
using namespace std;

const int MAX = 14;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {1, 0, -1, 0};
int N, graph[MAX][MAX], ret=INT_MAX;
bool visited[MAX][MAX];

bool check(int y, int x) {
    if (visited[y][x]) return false;
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || nx < 0 || ny >= N || nx >= N || visited[ny][nx]) return false;
    }
    return true;
}

int setFlower(int y, int x) {
    visited[y][x] = 1;
    int s = graph[y][x];

    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        s += graph[ny][nx];
        visited[ny][nx] = 1;
    }
    return s;
}

void eraseFlower(int y, int x) {
    visited[y][x] = 0;
    for (int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        visited[ny][nx] = 0;
    }
}

void flower(int depth, int hap) {
    if (depth == 3) {
        ret = min(ret, hap);
        return;
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (check(i, j)) {
                flower(depth+1, hap+setFlower(i, j));
                eraseFlower(i, j);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> N;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> graph[i][j];
        }
    }

    flower(0, 0);

    cout << ret << '\n';
    return 0;
}