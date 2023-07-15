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
  ListNode *removeNthFromEnd(ListNode *head, int n) {
    ListNode *ptr;
    ptr = head;
    int total = 0;
    while (ptr != NULL) {
      ptr = ptr->next;
      total++;
    }
    int delete_index = total - n - 1;
    if (delete_index < 0) {
      head = head->next;
      return head;
    }
    ptr = head;
    while (delete_index--) {
      ptr = ptr->next;
    }
    if ((ptr->next)->next) {
      ptr->next = (ptr->next)->next;
    } else {
      ptr->next = NULL;
    }
    return head;
  }
};