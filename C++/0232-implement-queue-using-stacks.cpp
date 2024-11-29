class MyQueue {
  stack<int> stack_q;
  stack<int> buffer_q;

 public:
  void push(int x) { stack_q.push(x); }
  int pop() {
    if (buffer_q.empty()) {
      while (!stack_q.empty()) {
        buffer_q.push(stack_q.top());
        stack_q.pop();
      }
    }
    int temp = buffer_q.top();
    buffer_q.pop();
    return temp;
  }
  int peek() {
    int temp = 0;
    if (!buffer_q.empty()) {
      temp = buffer_q.top();
    } else {
      while (!stack_q.empty()) {
        buffer_q.push(stack_q.top());
        stack_q.pop();
      }
      temp = buffer_q.top();
    }
    return temp;
  }
  bool empty() {
    if (buffer_q.empty() && stack_q.empty())
      return true;
    else
      return false;
  }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */