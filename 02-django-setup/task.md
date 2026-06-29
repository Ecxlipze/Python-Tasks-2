## Task 5 - Request Flow

When a user enters a URL in the browser, the browser sends an HTTP request to the Django server. 
Django checks `urls.py` to determine which view should handle the request.
The matched view processes the request and returns an HTTP response.
Finally, the browser receives the response and displays the result to the user.

Flow:
Browser → HTTP Request → urls.py → View → HTTP Response → Browser