package main

import (
	"fmt"
	"net/http"

	"github.com/go-swagger/go-swagger/errors"
	"github.com/go-swagger/go-swagger/httpkit"
	"github.com/go-swagger/go-swagger/httpkit/middleware"

	"github.com/onbeep/elevator-server/go-ele/restapi/operations"

	"github.com/onbeep/elevator-server/go-ele/vator"
)

// This file is safe to edit. Once it exists it will not be overwritten

func configureAPI(api *operations.LiftyAPI) http.Handler {
	// configure the api here
	api.ServeError = errors.ServeError

	api.JSONConsumer = httpkit.JSONConsumer()

	api.JSONProducer = httpkit.JSONProducer()

	// Declare the object for the Elevator
	v, err := vator.NewVator([]string{"B1", "F1", "F2", "F3"}, 3)
	if err != nil {
		panic(err)
	}

	api.CurrentFloorHandler = operations.CurrentFloorHandlerFunc(func(params operations.CurrentFloorParams) middleware.Responder {
		f := v.Current(params.CarID)
		body := operations.CurrentFloorOKBodyBody{ID: f.ID, Name: f.Name}
		return operations.NewCurrentFloorOK().WithPayload(body)
	})
	api.FloorCountHandler = operations.FloorCountHandlerFunc(func() middleware.Responder {
		return operations.NewFloorCountOK().WithPayload(operations.FloorCountOKBodyBody{
			Count: int32(len(v.Floors())),
		})
	})
	api.InventoryHandler = operations.InventoryHandlerFunc(func(params operations.InventoryParams) middleware.Responder {
		if params.Pwd != "p4ssw3rd" {
			return operations.NewInventoryUnauthorized()
		}

		body := []*operations.InventoryOKBodyItems0{}
		for _, floor := range v.Floors() {
			fid := floor.ID
			fname := floor.Name
			body = append(body, &operations.InventoryOKBodyItems0{
				ID:   &fid,
				Name: &fname,
			})
		}
		for _, car := range v.Cars() {
			cid := car.ID
			cname := car.Name
			body = append(body, &operations.InventoryOKBodyItems0{
				ID:   &cid,
				Name: &cname,
			})
		}

		return operations.NewInventoryOK().WithPayload(body)
	})
	api.WelcomeHandler = operations.WelcomeHandlerFunc(func() middleware.Responder {
		// return middleware.NotImplemented("operation .Welcome has not yet been implemented")
		return operations.NewWelcomeOK().WithPayload(operations.WelcomeOKBodyBody{"Welcome to the Elevator Server"})
	})

	api.ServerShutdown = func() {
		fmt.Printf("Shutting Down!\n")
	}
	// api.CommandLineOptionsGroups = []swag.CommandLineOptionsGroup{ ... }

	return setupGlobalMiddleware(api.Serve(setupMiddlewares))
}

// The middleware configuration is for the handler executors. These do not apply to the swagger.json document.
// The middleware executes after routing but before authentication, binding and validation
func setupMiddlewares(handler http.Handler) http.Handler {
	return handler
}

// The middleware configuration happens before anything, this middleware also applies to serving the swagger.json document.
// So this is a good place to plug in a panic handling middleware, logging and metrics
func setupGlobalMiddleware(handler http.Handler) http.Handler {
	return handler
}
