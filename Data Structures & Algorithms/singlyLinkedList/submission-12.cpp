struct node {
    public:
        int value;
        node* next;
        node(int v) : value(v), next(nullptr) {}
};

class LinkedList {
private:
    node* head;
public:
    LinkedList() {
        head = nullptr;
    }

    int get(int index) {
        node* curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr->next;
            if (!curr) {
                return -1;
            }
        }
        if (curr) {
            return curr->value;
        } else { return -1; }
        
    }

    void insertHead(int val) {
        if (!head) {
            head = new node(val);
        } else {
            node* newNode = new node(val);
            newNode->next = head;
            head = newNode;
        }
    }
    
    void insertTail(int val) {
        if (!head) {
            head = new node(val);
        } else {
            node* curr = head;
            while (curr->next) {
                curr = curr->next;
            }
            curr->next = new node(val);
        }
    }

    bool remove(int index) {
        if (index == 0) {
            if (!head) {
                return false;
            } else {
                node* temp = head;
                head = head->next;
                delete temp;
                return true;
            }
        } else {
            node* curr = head;
            node* prev = nullptr;
            for (int i = 0; i < index; i++) {
                if (!curr) {
                    return false;
                }
                prev = curr;
                curr = curr->next;
            }
            if (curr) {
                prev->next = curr->next;
                delete curr;
                return true;
            } else {
                return false;
            }
        }
    }

    vector<int> getValues() {
        vector<int> values;
        node* curr = head;
        while (curr) {
            values.push_back(curr->value);
            curr = curr->next;
        }
        return values;
    }
};
