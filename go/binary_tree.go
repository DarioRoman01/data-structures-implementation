package main

import "fmt"

type TreeNode struct {
	data  int
	left  *TreeNode
	right *TreeNode
}

func NewTree(root int) *TreeNode {
	t := &TreeNode{root, nil, nil}
	return t
}

func BuildTree(items []int) *TreeNode {
	root := &TreeNode{items[0], nil, nil}

	for _, item := range items[1:] {
		root.AddChild(root, item)
	}

	return root
}

func (t *TreeNode) AddChild(root *TreeNode, val int) {
	if root.data == val {
		return // node already exists
	}

	if root.data > val {
		if root.left != nil {
			t.AddChild(root.left, val)
		} else {
			root.left = &TreeNode{val, nil, nil}
		}
	} else if root.data < val {
		if root.right != nil {
			t.AddChild(root.right, val)
		} else {
			root.right = &TreeNode{val, nil, nil}
		}
	}
}

// return an array of sorted elements of the tree
func (t *TreeNode) InOrderTransversal() []int {
	var elements []int

	if t.left != nil {
		elements = append(elements, t.left.InOrderTransversal()...)
	}

	elements = append(elements, t.data)

	if t.right != nil {
		elements = append(elements, t.right.InOrderTransversal()...)
	}

	return elements
}

// search for a value in the tree
func (t *TreeNode) Search(val int) (*TreeNode, error) {
	if t.data == val {
		return t, nil
	}

	if t.data > val {
		if t.left != nil {
			return t.left.Search(val)
		} else {
			return nil, fmt.Errorf("Value not found")
		}
	}

	if t.data < val {
		if t.right != nil {
			return t.right.Search(val)
		} else {
			return nil, fmt.Errorf("Value not found")
		}
	}

	return t, nil
}

// return the min value in the node
func (t *TreeNode) FindMin() int {
	values := t.InOrderTransversal()
	return values[0]
}

// return the max value in the tree
func (t *TreeNode) FindMax() int {
	values := t.InOrderTransversal()
	return values[len(values)-1]
}

// remove an element from the list and return it
func (t *TreeNode) Remove(item int) *TreeNode {
	if t.data > item {
		if t.left != nil {
			return t.left.Remove(item)
		}

	} else if t.data < item {
		if t.right != nil {
			return t.right.Remove(item)
		}

	} else {
		tmp := *t
		*t = *t.right
		t.left = tmp.left
	}

	return t
}

func main() {
	x := []int{6, 2, 3, 7, 9}
	root := BuildTree(x)
	root.Remove(7)
	fmt.Println(root.InOrderTransversal())
}
