# Development 
## Set Environment Variables Vars 
e.g.,  
`export CORS_WHITELIST=['localhost']`  
`export SECRET='$3CR3T'`

## Run the Server
`python manage.py runserver`

# Contracts 
## Endpoint: `/posts/`  

method: POST  
  - body: `JSON: { content: String, title: String, score: Int, rating: Int, picture: String }`  
  - headers: "Content-Type": "application/json"    
  - return: `Object: { id: Int content: String, title: String, score: Int, rating: Int, picture: String }`

method: GET 
  - body: null  
  - headers: null  
  - return: `Array<Object> [ { id: Int content: String, title: String, score: Int, rating: Int, picture: String } ]` 

## Endpoint: `/posts/:id` 

method: PATCH  
  - body: `JSON: { content: String?, title: String?, score: Int?, rating: Int?, picture: String? }`   
  - headers: "Content-Type": "application/json"  
  - return: `Object: { id: Int content: String, title: String, score: Int, rating: Int, picture: String }`
  
method: PUT  
  - body: `JSON: { content: String, title: String, score: Int, rating: Int, picture: String }`   
  - headers: "Content-Type": "application/json"  
  - return: `Object: { id: Int content: String, title: String, score: Int, rating: Int, picture: String }`
  
method: DELETE
  - body: null  
  - headers: null  
  - return: null
