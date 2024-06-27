import pytest
from linkedlist import*
    # Append a single element to an empty LinkedList
def test_append_single_element_to_empty_list():
    ll = LinkedList()
    ll.append(10)
    assert ll.head is not None
    assert ll.head.value == 10
    assert ll.head.next is None

    # Retrieve an element from an empty LinkedList
def test_retrieve_element_from_empty_list():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll[0]
        
    # Append multiple elements to the LinkedList
def test_append_multiple_elements():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert len(ll) == 3
    assert ll.head.value == 10
    assert ll.head.next.value == 20
    assert ll.head.next.next.value == 30
    
    
    # Get the length of the LinkedList with multiple elements
def test_get_length_with_multiple_elements():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert len(ll) == 3