package main

import "fmt"

type Queue interface {
	// return the front element of the queue
	Front() (interface{}, error)

	// return the last element of the queue
	Back() (interface{}, error)

	// return if queue is empty
	IsEmpty() bool

	// remove all elements of the queue
	Empty() error

	// add element at the front of the queue
	Push(val interface{}) error

	// remove the top element in the queue
	Pop() (interface{}, error)
}

type SliceBasedQueue struct {
	data []interface{}
}

func NewQueue() Queue {
	s := &SliceBasedQueue{}
	return s
}

func (s *SliceBasedQueue) IsEmpty() bool {
	if len(s.data) == 0 {
		return true
	} else {
		return false
	}
}

func (s *SliceBasedQueue) Front() (interface{}, error) {
	if s.IsEmpty() {
		return nil, fmt.Errorf("The queue is empty")
	}

	return s.data[0], nil
}

func (s *SliceBasedQueue) Back() (interface{}, error) {
	if s.IsEmpty() {
		return nil, fmt.Errorf("The queue is empty")
	}

	return s.data[len(s.data)-1], nil
}

func (s *SliceBasedQueue) Push(val interface{}) error {
	s.data = append(s.data, val)
	return nil
}

func (s *SliceBasedQueue) Pop() (interface{}, error) {
	if s.IsEmpty() {
		return nil, fmt.Errorf("The queue is empty")
	}

	tmp := s.data[0]
	index := 0
	s.data = append(s.data[:index], s.data[index+1:]...)
	return tmp, nil
}

func (s *SliceBasedQueue) Empty() error {
	if s.IsEmpty() {
		return fmt.Errorf("The queue is already empty")
	}

	for len(s.data) > 0 {
		s.Pop()
	}

	return nil
}
