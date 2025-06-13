#include <bits/stdc++.h>
using namespace std;

const int MAX = 1501;
const int dx[4] = {1, 0, -1, 0};
const int dy[4] = {0, -1, 0, 1};
int R, C, ret, y, x, swanY, swanX, visitedSwan[MAX][MAX], visitedWater[MAX][MAX];
char graph[MAX][MAX];
queue<pair<int, int>> waterQ, waterTmpQ, swanQ, swanTmpQ;
string s;

bool moveSwan() {
    while (swanQ.size()) {
        tie(y, x) = swanQ.front(); 
        swanQ.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= R || nx >= C || visitedSwan[ny][nx]) continue;
            visitedSwan[ny][nx] = 1;
            if (graph[ny][nx] == '.') swanQ.push({ny, nx});
            else if (graph[ny][nx] == 'X') swanTmpQ.push({ny, nx});
            else if (graph[ny][nx] == 'L') return true;
        }
    }
    return false;
}

void waterMelting() {
    while (waterQ.size()) {
        tie(y, x) = waterQ.front();
        waterQ.pop();
        for (int i=0; i<4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            if (ny < 0 || nx < 0 || ny >= R || nx >= C || visitedWater[ny][nx]) continue;
            if (graph[ny][nx] == 'X') {
                visitedWater[ny][nx] = 1;
                waterTmpQ.push({ny, nx});
                graph[ny][nx] = '.';
            }
        }
    }
}

void Qclear(queue<pair<int, int>> &q) {
    queue<pair<int, int>> empty;
    swap(q, empty);
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> R >> C;
    for (int i=0; i<R; i++) {
        cin >> s;
        for (int j=0; j<C; j++) {
            graph[i][j] = s[j];
            if (s[j] == 'L') { swanY = i, swanX = j; }
            if (s[j] == '.' || s[j] == 'L') { 
                visitedWater[i][j] = 1;
                waterQ.push({i, j});
            }
        }
    }
    swanQ.push({swanY, swanX});
    visitedSwan[swanY][swanX] = 1;
    while (true) {
        if (moveSwan()) break;
        waterMelting();
        swanQ = swanTmpQ; 
        waterQ = waterTmpQ; 
        Qclear(swanTmpQ);
        Qclear(waterTmpQ);
        ret++;
    }
    cout << ret << '\n';

    return 0;
}