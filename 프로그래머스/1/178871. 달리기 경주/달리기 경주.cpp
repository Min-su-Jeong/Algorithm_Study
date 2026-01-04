#include <string>
#include <vector>
#include <map>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    map<string, int> mp;
    for (int i=0; i<players.size(); i++) mp[players[i]] = i;
    
    for (string cur_player: callings) {
        int rank = mp[cur_player];
        
        string prev_player = players[rank-1];
        players[rank-1] = players[rank];
        players[rank] = prev_player;
        
        mp[cur_player] = rank - 1;
        mp[prev_player] = rank;
    }
    return players;
}