class DLLNode:
    def __init__(self, url: str):
        self.data = url
        self.prev, self.next = None, None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.linkedListHead = DLLNode(homepage)
        self.current = self.linkedListHead

    def visit(self, url: str) -> None:
        newNode = DLLNode(url)
        self.current.next = newNode
        newNode.prev = self.current
        self.current = newNode

    def back(self, steps: int) -> str:
        while steps and self.current.prev:
            self.current = self.current.prev
            steps -= 1
        return self.current.data

    def forward(self, steps: int) -> str:
        while steps and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.data


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))
browserHistory.visit("linkedin.com")
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))


'''
0 1 2 3
leetcode google facebook youtube linkedin

0 1 2 3 2 1 2 4


back
0 1  
forward
3 4 2

facebook
google
facebook

BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
'''