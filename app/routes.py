from mvc_flask import Router

Router.get("/", "books#index")

api = Router.namespace("/api/v1")
