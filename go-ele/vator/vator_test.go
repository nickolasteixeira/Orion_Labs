package vator

import "testing"

func TestInstantiate(t *testing.T) {
	v, err := NewVator([]string{"B2", "B1", "Lobby", "F1", "F2", "F3"}, 3)
	if err != nil {
		t.Errorf("Unexpected error: %v\n", err)
	}
	t.Logf("Order: %v\n", v.floors)
	t.Logf("Second: %v\n", v.Floors())
}
