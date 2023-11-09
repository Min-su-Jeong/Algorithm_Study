import java.util.Map;
import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        // <선수명, 등수> Map 생성
        Map<String, Integer> rank = new HashMap<>();
        for (int i=0; i<players.length; i++) {
            rank.put(players[i], i);
        }
        
        for (String player : callings) {
            // 등수, 상위선수 호출
            int curRank = rank.get(player);
            String prePlayer = players[curRank-1];
            
            // player 배열 갱신
            players[curRank-1] = player;
            players[curRank] = prePlayer;
            
            // rank 갱신
            rank.put(player, curRank-1);
            rank.put(prePlayer, curRank);
        }
        return players;
    }   
}