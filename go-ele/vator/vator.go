package vator

import "fmt"

// Vator - modeled elevator
type Vator struct {
	floors       []string
	lookupFloors map[string]string
	lookupCars   map[string]string
	carAtFloor   map[string]string
}

// NewVator - instantiate a new elevator model
func NewVator(floors []string, carCt int8) (*Vator, error) {
	return nil, fmt.Errorf("Not Yet Implemented!")
}
