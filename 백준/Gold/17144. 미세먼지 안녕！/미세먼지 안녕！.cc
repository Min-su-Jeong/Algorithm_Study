#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<vector<int>> Board;

struct Pos {
	int y;
	int x;
};

int r, c, t;
int dx[4] = { 0, 0, 1, -1 };
int dy[4] = { 1, -1, 0, 0 };
Pos upperAC;
Pos lowerAC;

void spreadDust(Board& board) {
	Board visited(r, vector<int>(c, 0));

	for (int y = 0; y < r; y++) {
		for (int x = 0; x < c; x++) {
			if (board[y][x] == -1) {
				visited[y][x] = -1;
				continue;
			}
			int cur_dust = board[y][x];
			int spread_dust = cur_dust / 5;
			int spread_cnt = 0;

			for (int i = 0; i < 4; ++i) {
				int ny = y + dy[i];
				int nx = x + dx[i];
				if (ny >= 0 && ny < r && nx >= 0 && nx < c && board[ny][nx] != -1) {
					visited[ny][nx] += spread_dust;
					spread_cnt++;
				}
			}
			visited[y][x] += cur_dust - (spread_dust * spread_cnt);
		}
	}
	board = visited;
}

void circulateCCW(Board& board) {
	for (int y = upperAC.y - 1; y > 0; --y) board[y][0] = board[y - 1][0];
	for (int x = 0; x < c - 1; ++x) board[0][x] = board[0][x + 1];
	for (int y = 0; y < upperAC.y; ++y) board[y][c - 1] = board[y + 1][c - 1];
	for (int x = c - 1; x > 1; --x) board[upperAC.y][x] = board[upperAC.y][x - 1];
	board[upperAC.y][1] = 0;
}

void circulateCW(Board& board) {
	for (int y = lowerAC.y + 1; y < r - 1; ++y) board[y][0] = board[y + 1][0];
	for (int x = 0; x < c - 1; ++x) board[r - 1][x] = board[r - 1][x + 1];
	for (int y = r - 1; y > lowerAC.y; --y) board[y][c - 1] = board[y - 1][c - 1];
	for (int x = c - 1; x > 1; --x) board[lowerAC.y][x] = board[lowerAC.y][x - 1];
	board[lowerAC.y][1] = 0;
}

ll getDustAmount(const Board& board) {
	ll result = 0;
	for (int y = 0; y < r; y++) {
		for (int x = 0; x < c; x++) {
			if (board[y][x] > 0) {
				result += board[y][x];
			}
		}
	}
	return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

	cin >> r >> c >> t;
	Board board(r, vector<int>(c, 0));
	bool foundAC = false;
	for (int y = 0; y < r; ++y) {
		for (int x = 0; x < c; ++x) {
			cin >> board[y][x];
			if (!foundAC && board[y][x] == -1) {
				upperAC = { y, x };
				lowerAC = { y + 1, x };
				foundAC = true;
			}
		}
	}

	for (int i = 0; i < t; ++i) {
		spreadDust(board);
		circulateCCW(board);
		circulateCW(board);
	}

	cout << getDustAmount(board);
	return 0;
}