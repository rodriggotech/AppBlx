# 
FROM python:3

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

EXPOSE 8080

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./AppBlx /code/Appblx

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]

