# Linear dependent compute API
Simple API that starts async task to compute linear dependent columns (LDC) in the data provided by a CSV file.  
The file could be stored on AWS-S3 or at the `static` directory.  
For AWS-S3 storage using please provide the credentials with the `.env` file (for Docker) or `env variables`.  
Main components of the system highly decoupled.

# RUN
## Routes
The service provide 2 routes:
* `/proces/{file_name}` - start a task that will compute LDC from the `{filename}.csv`.
Could return:
    * `202` - task accepted. 
    The url for results provided by the `Location` header.   
    Task results could be deleted if the `TASK_RESULT_EXPIRED_SEC` option provided.
    * `404` - file not found.
    * `400` - file contains errors or could not be processed.
    * `500` - unexpected error acquired.
* `/task/{task_id}` - get results for the task. The URL will be provided by the `Location` header 
after the process task will be launched.
Could return:
    * `200` - return task results list contains the id of a LDC.
    * `404` - task with the ID not found. Task result could be expired (see the explanation above).  
    * `500` - unexpected error acquired.
    
Look at the tests for more details.
## Docker
`docker-compose up -d`
## Manually
`bash ./run.sh`

# TODO
1. Should close the thread pool gracefully at a shutdown.
2. Should implement memcached server support for scaling.
3. Authorization.
4. Request/Response schema validation support if necessary.
5. WebSocket or SSE for better UX.
