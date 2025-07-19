#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> ret;
    stack<int> stk;
    
    for (int i=0; i<arr.size(); i++) {
        if (stk.size() && stk.top() == arr[i]) {
            stk.pop();
        }
        stk.push(arr[i]);
    }
    while (stk.size()) {
        ret.push_back(stk.top());
        stk.pop();
    }
    reverse(ret.begin(), ret.end());
    

    return ret;
}