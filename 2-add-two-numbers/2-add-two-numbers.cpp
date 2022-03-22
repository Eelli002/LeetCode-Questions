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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        /*
        - carry = 0;
        - if sum (two numbers + carry) < 10 then result is stored, carry set to 0
        - else if carry != 0 then new node, val == carry
        */
        ListNode *l1curr = l1;
        ListNode *l2curr = l2;
        
        
        int carry = 0;
        int value;
        
        ListNode *totalList;
        ListNode *totalCurr;
        int positionalSum = (l1curr->val + l2curr->val);
        string positionalString;
        
        if (positionalSum > 9) {
            positionalString = to_string(positionalSum);
            carry = positionalString[0] - '0';
            value = positionalString[1] - '0';
            totalList = new ListNode(value);
        }
        else totalList = new ListNode(positionalSum);
        
        totalCurr = totalList;
        l1curr = l1curr->next;
        l2curr = l2curr->next;
        
        
        while (l1curr != nullptr && l2curr != nullptr) {
            positionalSum = (l1curr->val + l2curr->val + carry);
            if (positionalSum > 9) {
                positionalString = to_string(positionalSum);
                carry = positionalString[0] - '0';
                value = positionalString[1] - '0';
                ListNode *positionalValue = new ListNode(value);
                totalCurr->next = positionalValue;
            }
            else {
                ListNode *positionalValue = new ListNode(positionalSum);
                totalCurr->next = positionalValue;
                carry = 0;
            }
            l1curr = l1curr->next;
            l2curr = l2curr->next;
            totalCurr = totalCurr->next;
        }
        
        while(l1curr != nullptr) {
            positionalSum = (l1curr->val + carry);
            if (positionalSum > 9) {
                positionalString = to_string(positionalSum);
                carry = positionalString[0] - '0';
                value = positionalString[1] - '0';
                ListNode *positionalValue = new ListNode(value);
                totalCurr->next = positionalValue;
            }
            else {
                ListNode *positionalValue = new ListNode(positionalSum);
                totalCurr->next = positionalValue;
                carry = 0;
            }
            
            l1curr = l1curr->next;
            totalCurr = totalCurr->next;
        }

        
        while(l2curr != nullptr) {
            positionalSum = (l2curr->val + carry);
            if (positionalSum > 9) {
                positionalString = to_string(positionalSum);
                carry = positionalString[0] - '0';
                value = positionalString[1] - '0';
                ListNode *positionalValue = new ListNode(value);
                totalCurr->next = positionalValue;
            }
            else {
                ListNode *positionalValue = new ListNode(positionalSum);
                totalCurr->next = positionalValue;
                carry = 0;
            }
            
            l2curr = l2curr->next;
            totalCurr = totalCurr->next;
        }
        
        if (carry != 0) {
            ListNode *MSD = new ListNode(carry);
            totalCurr->next = MSD;
        }
        return totalList;
    }
};




