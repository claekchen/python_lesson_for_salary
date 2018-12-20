import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def get_length(self,head):
        p=head
        count=1
        while p.next is not None:
            p=p.next
            count=count+1
        return count
    def reverseList(self, head):
        p=head
        if head==None:
            return None
        else:
            new=None
            length=self.get_length(head) 
            if self.get_length(head)==1:
                return head 
            else:  
                while self.get_length(head)>0:
                    p=head
                    if self.get_length(head)==length:
                        while self.get_length(p)>2:
                            p=p.next
                        pop=p.next
                        p.next=None
                        new=pop
                        t=new
                    else:
                        if self.get_length(head)==1:
                            t.next=p
                            break
                        else:
                            while self.get_length(p)>2:
                                p=p.next
                            pop=p.next
                            p.next=None
                            t.next=pop
                            t=t.next
            return new

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            
            ret = Solution().reverseList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()