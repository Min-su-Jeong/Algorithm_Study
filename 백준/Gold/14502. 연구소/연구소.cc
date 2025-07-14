#include <bits/stdc++.h>
using namespace std;

const int MAX = 10;
const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};
int N, M, ret, graph[MAX][MAX];
bool visited[MAX][MAX];
vector<pair<int, int>> virusList, wallList;

void dfs(int y, int x) {
    // 바이러스 퍼트리기
    for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= M || ny >= N || visited[ny][nx] || graph[ny][nx] == 1) continue;
        visited[ny][nx] = 1;
        dfs(ny, nx);
    }
    return;
}

int solve() {
    // visited : 바이러스 위치 1로 삽입
    fill(&visited[0][0], &visited[0][0] + MAX * MAX, 0);
    for (pair<int, int> v : virusList) {
        visited[v.first][v.second] = 1;
        dfs(v.first, v.second);
    }

    int cnt = 0;
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (graph[i][j] == 0 && !visited[i][j]) cnt++;
        }
    }
    
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> N >> M;

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            cin >> graph[i][j];
            if (graph[i][j] == 2) virusList.push_back({i, j});
            if (graph[i][j] == 0) wallList.push_back({i, j});
        }
    }

    for (int i=0; i<wallList.size(); i++) {
        for (int j=0; j<i; j++) {
            for (int k=0; k<j; k++) {
                // 벽 3개 세우기
                graph[wallList[i].first][wallList[i].second] = 1;
                graph[wallList[j].first][wallList[j].second] = 1;
                graph[wallList[k].first][wallList[k].second] = 1;
                
                // 안전 영역 크기 계산
                ret = max(ret, solve());

                // 벽 초기화
                graph[wallList[i].first][wallList[i].second] = 0;
                graph[wallList[j].first][wallList[j].second] = 0;
                graph[wallList[k].first][wallList[k].second] = 0;
            }
        }
    }
    cout << ret << '\n';

    return 0;
}