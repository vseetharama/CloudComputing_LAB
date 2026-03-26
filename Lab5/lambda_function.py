def lambda_handler(event,context):
  return{
      "statusCode":200,
      "Body":"Hello from lambda!"
           }

# DockerFile(file name)
# FROM public.ecr.aws/lambda/python:3.9
# COPY lambda_function.py .
# CMD ["lambda_function.lambda_handler"]
#root@ubuntu:~$ vi lambda_function.py
# root@ubuntu:~$ vi Dockerfile
# root@ubuntu:~$ hostname -I
# 172.30.1.2 172.17.0.1 10.88.0.1 
# root@ubuntu:~$ docker build -t my-lambda .
#root@ubuntu:~$ docker run -p 9000:8080 my-lambda
#Tab 2 
#root@ubuntu:~$ curl -XPOST "http://172.30.1.2:9000/2015-03-31/functions/function/invocations" -d '{}'
