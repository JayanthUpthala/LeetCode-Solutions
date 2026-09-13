class MinStack {
    Stack<Integer> minst;
    Stack<Integer> mainst;
    
    public MinStack() {
        minst = new Stack<>();
        mainst = new Stack<>();
    }
    
    public void push(int value) {
        mainst.push(value);
        if(minst.isEmpty()){
            minst.push(value);
        }
        else{
            if(minst.peek() >= value){
                minst.push(value);
            }
        }
    }
    
    public void pop() {
        if(!mainst.isEmpty()){
            int var = mainst.pop();
            if(minst.peek()==var){
                minst.pop();
            }
        }
        
    }
    
    public int top() {
        // if(!mainst.isEmpty()){
        return mainst.peek();
        // }
        // return 1;
    }
    
    public int getMin() {
        // if(!minst.isEmpty()){
        return minst.peek();
        // }
        // return 1;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(value);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */