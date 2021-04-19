package main

import "fmt"

type Stack interface {

	// push a new element in the stack
	push(interface{}) error

	// remove the top element en retunr it
	pop() (interface{}, error)

	// return the size of the stack
	size() int

	// return the top element of the stack
	peek() (interface{}, error)

	// return if list is empty
	is_empty() bool

	// remove all elements of the stack
	empty()
}

type SliceBasedStack struct {
	data []interface{}
}

func NewStack() Stack {
	s := &SliceBasedStack{}
	return s
}

func (s *SliceBasedStack) peek() (interface{}, error) {
	if len(s.data) == 0 {
		return nil, fmt.Errorf("The stack is empty")
	}

	return s.data[len(s.data)-1], nil
}

func (s *SliceBasedStack) push(val interface{}) error {
	s.data = append(s.data, val)
	return nil
}

func (s *SliceBasedStack) is_empty() bool {
	if len(s.data) == 0 {
		return true
	} else {
		return false
	}
}

func (s *SliceBasedStack) pop() (interface{}, error) {
	if s.is_empty() {
		return nil, fmt.Errorf("The stack is empty")
	}

	index := len(s.data) - 1
	tmp := s.data[index]
	s.data = append(s.data[:index], s.data[index+1:]...)

	return tmp, nil
}

func (s *SliceBasedStack) size() int {
	return len(s.data)
}

func (s *SliceBasedStack) empty() {
	if len(s.data) == 0 {
		return
	}
	for len(s.data) > 0 {
		s.pop()
	}
}
