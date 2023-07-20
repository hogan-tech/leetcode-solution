/**
 * // This is the ImmutableListNode's API interface.
 * // You should not implement it, or speculate about its implementation.
 * class ImmutableListNode {
 * public:
 *    void printValue(); // print the value of the node.
 *    ImmutableListNode* getNext(); // return the next node.
 * };
 */

class Solution
{
public:
    void printLinkedListInReverse(ImmutableListNode *head)
    {
        int count = 0;
        ImmutableListNode *t_current = head;
        // get Count
        while (t_current != NULL)
        {
            count++;
            t_current = t_current->getNext();
        }

        for (int i = count; i >= 1; i--)
        {
            ImmutableListNode *current = head;
            for (int j = 0; j < i - 1 && current != NULL; j++)
            {
                current = current->getNext();
            }
            current->printValue();
        }
    }
};