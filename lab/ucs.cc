#include<bits/stdc++.h>
using namespace std;
int main(){
    unordered_map<char,vector<pair<char, int>>> graph;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
    unordered_map<char,bool> visited;
    unordered_map<char, int> cost;
    
    // making graph
    graph['A'] = {{'B', 2}, {'C', 3}};
    graph['B'] = {{'E', 5}, {'F', 6}};
    graph['C'] = {{'A', 3}, {'D', 2}, {'E', 4}};
    graph['D'] = {{'C', 2}, {'E', 3}, {'F',2}};
    graph['E'] = {{'B', 5}, {'C', 4}, {'D',3}};
    graph['F'] = {{'B', 6}, {'D', 2}};


    char start = 'A', goal = 'F';
    vector<pair<vector<char>, int>> ans = solve(graph,start,goal,visited,cos);
}