# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyOriginalSolution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        numbers1 = self.linked_list_to_number_array(l1)
        numbers2 = self.linked_list_to_number_array(l2)
        summed_number = self.add_number_lists(numbers1, numbers2)
        return self.number_array_to_linked_list(summed_number)

    def linked_list_to_number_array(self, head):
        array = [head.val]

        while head.next is not None:
            head = head.next
            array.append([head.val])

        return list(reversed(array))

    def number_array_to_linked_list(self, number_array):
        head = ListNode(number_array[0])
        previous_node = head

        for val in number_array:
            current_node = ListNode(val)
            previous_node.next = current_node
            previous_node = current_node

        return head

    def add_number_lists(self, num1, num2):
        output = []

        if len(num2) > len(num1):
            num_a, num_b = num2, num1
        else:
            num_a, num_b = num1, num2

        carry = False
        for index in range(len(num_b)):
            pair_sum = num_a[index] + num_b[index] + carry
            carry = pair_sum >= 10
            output.append([pair_sum % 10])

        # iffy variable assignment here but len(num_b) >= 1 every time.
        for index in range(index + 1, len(num_a)):
            pair_sum = num_a[index] + carry
            carry = pair_sum >= 10
            output.append([pair_sum % 10])

        if carry:
            output.append([1])

        return output


class Solution():
    # Improvement on the original as it there are no intermediate arrays.
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0)
        current_node = temp
        carry = False

        while any((l1, l2, carry)):
            if l1 is not None:
                l1_val = l1.val
            else:
                l1_val = 0

            if l2 is not None:
                l2_val = l2.val
            else:
                l2_val = 0

            pair_sum = l1_val + l2_val + carry
            carry = pair_sum >= 10
            current_node.next = ListNode(pair_sum // 10)

            current_node = current_node.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return temp.next
