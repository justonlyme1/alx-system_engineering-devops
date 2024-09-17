## Tasks :page_with_curl:

* **0. Set up development with Python**
  * In this task, I configured the file `web_flask/0-hello_route.py` from my
  [AirBnB_clone_v2](https://github.com/aysuarex/AirBnB_clone_v2) to serve content
  on the route `/airbnb-onepage/`, running on port `5000`.

* **1. Set up production with Gunicorn**
  * This task involved setting up a production environment, installing and config>
  Gunicorn to serve the same file from task 0.

* **2. Serve a page with Nginx**
  * [2-app_server-nginx_config](./2-app_server-nginx_config): Nginx configuration>
  proxying requests on the route `/airbnb-onepage/` to the Gunicorn app running on
  port `5000`.

* **3. Add a route with query parameters**
  * [3-app_server-nginx_config](./3-app_server-nginx_config): Nginx configuration>
  proxying requests on the route `/airbnb-dynamic/number_odd_or_even/<int: num>` >
  Gunicorn app running on port `5000`.

* **4. Let's do this for your API**
  * In this task, I configured the API from my [AirBnB_clone_v3](https://github.c>
  * [4-app_server-nginx_config](./4-app_server-nginx_config): Nginx configuration>
  that proxies requests on the AirBnB API to the corresponding Gunicorn app.

* **5. Serve your AirBnB clone**
  * In this task, I configured the complete AirBnB app from [AirBnB_clone_v4](htt>
  * [5-app_server-nginx_config](./5-app_server-nginx_config): Nginx configuration>
  configured to serve the static assets from `web_dynamic/static/` on the Gunicor>
  app.


