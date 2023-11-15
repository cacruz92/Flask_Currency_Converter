### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
 - JavaScript is used for manipulating the DOM and creating formulas that interact with the client facing side. It uses the curly brackets ({}) and is more flexible with its syntax. Javascript is executed in the browser but can also be used on the server side. Python allows you to use methods to interact with databases and other mechanisms affecting the back-end/server side. Python uses a cleaner and more readable code where spacing and indentation matter. Python is typically executed on the server side.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  - You can use the 'get()' method. This will allow you to look for it and set a default value for the key, if it is not found. You can also use a "try-except block" This can catch the error if the key is missing and let that exception be raised and you can set the value to a default as well.

- What is a unit test?
 - Unit tests test one "unit" of functionality. Doesn't test the integration of components. It promotes modular code

- What is an integration test?
 - Integration tests test that the components of the code are working together, such as how a URL path maps to a route function, if the right HTML is returned by a route, is the right status code appearing after a route is followed, etc.

- What is the role of web application framework, like Flask?
 - It contains a set of methods, rules, and functionality to allow for the simplification and acceleration of web/app development. It provides a structured and organized way to build these applications.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  - You should use a route parameter when the information is fundamentally part of the identity of the resource or it is an important part of the URL structure. This is used typically for retrieving speciic resources and are user friendly and descriptive bc the info is included directly in the URL. URL query params can be used when the information is optional, to filter criteria, or to configure options for a resource and it it doesn't fundamentally define the resource itself. Often used for searching, filtering, or specifying parameters. It allows you to alter resources without actually changing the URL.

- How do you collect data from a URL placeholder parameter using Flask?
 - using the angled brackets(<>) you can define a route with the palceholder paramenter. Then you can define a function including a corresponding parameter in the function deinition. Then you can access the variable in the function to process the information

- How do you collect data from the query string using Flask?
 - Import the request module from Flask. When you access a URL with a query string in it, the query parametrs will be collected and processed by the function that is defined on that route and the collected data will be included in the response. 

- How do you collect data from the body of the request using Flask?
 - Import the request module from Flask. Define a route that will handle the incoming POST request and will collect data from the body of the request. Then you use request.form or request.data
 
- What is a cookie and what kinds of things are they commonly used for?
 - Cookies are small pieces of data that a web server sends to the user's browser during an HTTP request. The browser stores the data and sends it back to the server with future requests from the same user. They are used for authentication, personalization, tracking, targeted ads, and shopping carts.

- What is the session object in Flask?
 - The session object is a built in object allowing you to store and manage user-specific data between different requests. It provides a way to maintain user sessions and keep track of data associated with individual users as they interact with a web application.

- What does Flask's `jsonify()` do?
 - jsonify() creates JSON responses from Python dictionaries or other data structures. It is used to serialize Python data into a JSON format and set the appropriate HTTP headers to indicate that the response should be interpreted as JSON by the client.
