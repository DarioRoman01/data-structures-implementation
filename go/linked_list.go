package main

import "fmt"

type Node struct {
	data interface{}
	prev *Node
	next *Node
}

type LinkedList struct {
	head *Node
}

// insert element at the end of the list
func (l *LinkedList) InsertAtEnd(val interface{}) {
	if l.head.data == nil {
		l.head = &Node{val, nil, nil}
	}

	itr := l.head

	for itr.next != nil {
		itr = itr.next
	}

	itr.next = &Node{val, itr, nil}
}

// insert element at beginign of the list
func (l *LinkedList) InsertAtBegining(val interface{}) {
	if l.head.data == nil {
		l.head.data = val
	}

	node := &Node{val, nil, l.head}
	l.head = node
}

// get last element of the list
func (l *LinkedList) GetLastNode() (interface{}, error) {
	if l.head.data == nil {
		return nil, fmt.Errorf("The list is empty")
	}

	itr := l.head

	for itr.next != nil {
		itr = itr.next
	}

	return itr, nil
}

// verify if the list contains a value
func (l *LinkedList) Contains(val interface{}) bool {
	itr := l.head

	for itr.next != nil {
		if itr.data == val {
			return true
		}

		itr = itr.next
	}

	return false
}

// return the size of the list
func (l *LinkedList) Size() int {
	count := 0
	itr := l.head

	for itr.next != nil {
		count++
		itr = itr.next
	}

	return count
}

// insert element after specified value
func (l *LinkedList) InsertAt(at int, val interface{}) error {
	itr := l.head

	if itr.data == at {
		l.InsertAtBegining(val)
	}

	for itr.next != nil {
		if itr.data == at {
			itr = &Node{val, itr, itr.next}
			return nil
		}
		itr = itr.next
	}

	return fmt.Errorf("The value to insert at does not exist")
}

// return item if exist
func (l *LinkedList) GetItem(item interface{}) (interface{}, error) {
	itr := l.head

	if itr.data == item {
		return itr.data, nil
	}

	for itr.next != nil {
		if itr.data == item {
			return itr.data, nil
		}
		itr = itr.next
	}

	return nil, fmt.Errorf("The item does not exist")
}

// remove item from the list and return it
func (l *LinkedList) RemoveItem(item interface{}) (interface{}, error) {
	itr := l.head

	var tmp *Node
	if itr.data == nil {
		return nil, fmt.Errorf("The list is empty")
	} else if itr.data == item {
		itr = itr.next
		return itr, nil
	}

	for itr.next != nil {
		if itr.data == item {
			tmp = itr
			itr.prev.next = itr.next
			if itr.next != nil {
				itr.next.prev = itr.prev
			}
			break
		}
		itr = itr.next
	}

	return tmp, nil
}
