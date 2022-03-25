# order_app
Order App:
- Customers can login using username and password - Authentication
- Customers can view a list of all the products
- They can add the products to the cart.
- Initially the quantity of each product has been set to 1 for simplicity.
- The quantity in stock is a value attached to each product which will keep on decreasing as items are added.
- History view will enable a logged in user to view the history of their orders.

For deployment to Azure
- On the azure portal an App service will be created.
- The App service can then be linked to this GitHub repository
- CI/CD pipeline can also be setup to to deploy the app service when changes are made to the repository.
