#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void DFS(int v, vector<bool>& visited,vector<vector<int>> & adj_list)
{
    // Mark the current node as visited and
    // print it
    visited[v] = true;
    cout << v << " ";

    for (auto i = adj_list[v].begin(); i != adj_list[v].end(); ++i)
        if (!visited[*i])
            DFS(*i, visited,adj_list);
}


int main()
{
    int v,e,t1,t2;
    //Enter no. of Vertices
    cin>>v;
    //Enter no. of Edges of Directed Graph
    cin>>e;
    vector<vector<int>> adj_list(v);
    for(int i =0;i<e;i++)
    {
        cin>> t1;
        cin>> t2;
        adj_list[t1].push_back(t2);
    }
    vector<bool> visited(v,false);
    DFS(0,visited,adj_list);
}
