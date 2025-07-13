#include <stdio.h>
#define MAX_VERTICES 100 // 設置最大節點數
#define FALSE 0 // 未拜訪節點
#define TRUE 1 // 已拜訪節點

// 定義節點結構
typedef struct node *nodePointer;
typedef struct node {
    int vertex;
    nodePointer link;
} node;

// 圖的鄰接表與訪問紀錄
nodePointer graph[MAX_VERTICES];
short int visited[MAX_VERTICES];

// DFS 遞迴函數
void dfs(int v) {
    nodePointer w;
    visited[v] = TRUE;
    printf("%d ", v);  // 拜訪節點 v，印出它

    // 遍歷 v 的鄰接節點
    for (w = graph[v]; w; w = w->link) {
        if (!visited[w->vertex]) {
            dfs(w->vertex);  // 遞迴拜訪尚未拜訪的相鄰節點
        }
    }
}
