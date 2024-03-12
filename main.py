from random import randrange
from fastapi import FastAPI,status,Response,HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class createpost(BaseModel):
    name: str
    email: str
    city: str
    rating: Optional[int] = None
    publish: bool = False
    


students = [{"name":"Ravi","email":"ravi@ravi.com","city":"Hyderabad","id":1},{"name":"Babu","email":"babu@ravi.com","city":"Hyderabad","id":2}]

def findPost(id):
    
    for std in students:
        if std['id'] == id:
            return std

def find_index(id):
    for i,p in enumerate(students):
        if p['id']== id:
            return i    

@app.get('/')
def home(resp : Response):
    if not students:
        resp.status_code = status.HTTP_404_NOT_FOUND
    return {"data":students}


@app.get('/post/{id}')
def singelPost(id: int, resp: Response):
    res = findPost(id)
    if not res :
        resp.status_code = status.HTTP_404_NOT_FOUND
        return {"data":"no recoards"}
  
    return {"data": res}

@app.post('/create/')
def creatnew(post: createpost):
    res = post.dict()
    res['id'] = randrange(0,745864)
    students.append(res)
    return {"post data":res}
@app.put('/update/{id}')
def updatep(id: int, uppost: createpost):
    
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"no recoard found id no {id}") 
    
    up_dict = uppost.dict()
    
    up_dict['id'] = id
    up_dict['index'] = index
    
    return {"data":up_dict}

@app.delete("/delete/{id}",status_code=status.HTTP_202_ACCEPTED)
def delpost(id: int):  
     
    index = find_index(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail=f"no recoard found id no {id}")    
    students.pop(index)
    return {"data":"recoard deleted"}