# Minimal celery skeleton with local file system broker and backend

 * File system config from [here](https://www.distributedpython.com/2018/07/03/simple-celery-setup/)
 * For loading data at startup, see [here](https://theblog.workey.co/my-experiences-with-a-long-running-celery-based-microprocess-b2cc30da94f5)


 Starting the worker

 ```
>>> celery -A tasks worker --loglevel=info
```

Running the client

```
>>> python main.py
2
```
