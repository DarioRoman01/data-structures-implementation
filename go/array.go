package main

import "fmt"

type Array interface {
	Push(item interface{})

	Pop() (interface{}, error)

	Get(index int) interface{}

	Insert(item interface{}, index int) (interface{}, error)

	Length() int

	Remove(index interface{}) (interface{}, error)
}

type MapBasedArray struct {
	length int
	data   map[int]interface{}
	seq    int
}

// moves item to next index
func (a *MapBasedArray) unshiftIndex(index int) {
	for i := a.length; i > index; i++ {
		a.data[i] = a.data[i-1]
	}
}

// moves items to prev index
func (a *MapBasedArray) shiftIndex(index int) {
	for i := index; i < a.length; i++ {
		a.data[i] = a.data[i+1]
	}
}

// Get element by index
func (a *MapBasedArray) Get(index int) interface{} {
	item, exist := a.data[index]
	if !exist {
		return fmt.Errorf("Invalid index")
	}

	return item
}

// insert element at last position
func (a *MapBasedArray) Push(item interface{}) {
	if a.length == 0 {
		a.data[a.length] = item
	} else {
		a.data[a.length+1] = item
	}
	a.seq++
	a.length++
}

// return the lenght of the array
func (a *MapBasedArray) Length() int {
	return a.length
}

// remove last item and return it
func (a *MapBasedArray) Pop() (interface{}, error) {
	if a.length == 0 {
		return nil, fmt.Errorf("The array is empty")
	}

	item := a.data[a.length]
	delete(a.data, a.length)
	a.length--
	a.seq--
	return item, nil
}

// insert item at given index
func (a *MapBasedArray) Insert(item interface{}, index int) (interface{}, error) {
	if a.length == 0 {
		return nil, fmt.Errorf("The array is empty")
	}

	_, exist := a.data[index]
	if !exist {
		return nil, fmt.Errorf("Invalid index")
	}

	a.unshiftIndex(index)
	a.data[index] = item

	return item, nil
}

// remove element by index
func (a *MapBasedArray) Remove(index int) (interface{}, error) {
	item, exist := a.data[index]
	if !exist {
		return nil, fmt.Errorf("Invalid index")
	}

	a.shiftIndex(index)

	return item, nil

}
