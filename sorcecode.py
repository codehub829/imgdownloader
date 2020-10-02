#author: codeHub
import requests
URL=""
r=request.get(URL)
with open(path,"wb") as file:
     file.write(r.content)
