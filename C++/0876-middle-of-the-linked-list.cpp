/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *p = head;
        int counter = 0;
        cout << endl;
        while(p != NULL){
            p = p->next;
            counter ++;
        }
        counter /= 2;
        while(counter -- > 0){
            head = head->next;
        }
        return head;
    }
};