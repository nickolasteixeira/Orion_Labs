package main

import (
	"fmt"
	"net/http"

	"github.com/go-swagger/go-swagger/errors"
	"github.com/go-swagger/go-swagger/httpkit"
	"github.com/go-swagger/go-swagger/httpkit/middleware"

	"github.com/onbeep/elevator-server/go-ele/restapi/operations"
)

// This file is safe to edit. Once it exists it will not be overwritten

func configureAPI(api *operations.LiftyAPI) http.Handler {
	// configure the api here
	api.ServeError = errors.ServeError

	api.JSONConsumer = httpkit.JSONConsumer()

	api.JSONProducer = httpkit.JSONProducer()

	api.CurrentFloorHandler = operations.CurrentFloorHandlerFunc(func(params operations.CurrentFloorParams) middleware.Responder {
		return middleware.NotImplemented("operation .CurrentFloor has not yet been implemented")
	})
	api.FloorCountHandler = operations.FloorCountHandlerFunc(func() middleware.Responder {
		return middleware.NotImplemented("operation .FloorCount has not yet been implemented")
	})
	api.InventoryHandler = operations.InventoryHandlerFunc(func(params operations.InventoryParams) middleware.Responder {
		return middleware.NotImplemented("operation .Inventory has not yet been implemented")
	})
	api.WelcomeHandler = operations.WelcomeHandlerFunc(func() middleware.Responder {
		return middleware.NotImplemented("operation .Welcome has not yet been implemented")
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
