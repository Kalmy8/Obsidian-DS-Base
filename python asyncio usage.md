[Асинхронный python без головной боли](https://habr.com/ru/articles/667630/)

#🃏/job_questions
## Key questions
Provide a simple asyncio example which will run multiple functions asynchronously and will gather the returned values of that functions
?
```python
import asyncio  
    
async def busy1()->str:  
    print('Busy1 starts working...')  
    await asyncio.sleep(2)  
    print('Busy1 ends working...')  
    return 'result1'  
  
async def busy2()->str:  
    print('Busy2 starts working...')  
    await asyncio.sleep(2)  
    print('Busy2 ends working...')  
    return 'result2'  
  
async def main():  
    results = await asyncio.gather(busy1(), busy2())  
    print(results)  
  
asyncio.run(main())
```
