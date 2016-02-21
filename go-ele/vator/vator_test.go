package vator

import "testing"

func TestInstantiate(t *testing.T) {
	_, err := NewVator([]string{"B2", "B1", "Lobby", "F1", "F2", "F3"}, 3)
	if err == nil {
		t.Errorf("Expected error!")
	}
}
