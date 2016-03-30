##Reverse Linked List

Write code to reverse a linked list, if you able to do it using loops, try to solve with recursion?

출처 : <http://www.csharpstar.com/top-20-google-amazon-programming-interview-questions>

Linked List를 Reverse하세요. (뒤집으세요.)

역으로 진행되도록 만드세요. 라고 이해하면 됩니다.

3번문제에서 만든 `LinkedNode<T>` class에 아래 2개의 method를 추가했습니다.

---

###C# 추가한 method

```C#
    public LinkedNode<T> GetLast()
    {
        if (DetectCirculation())
            throw new Exception("Circulation Linked Node");
        LinkedNode<T> findLast = this;

        while (findLast._next != null)
        {
            findLast = findLast._next;
        }

        return findLast;
    }
```
