# REACT (reason-act) workflow

## Toy low-level manual example
We use custom class which will create a simple agent, capable of handling user prompts

The main entity here is **self.messages**, which is an array containing our user-model conversation history

The example below uses external GPT-4o reference and pass the conversation history to it. For now, we do not allow the language model to actually grab some data by itself.

But! The model is capable of asking for some information from as, saying **Thought** (reason) and **Action** (the desired action it wants from us)
When we provide our answer with the **Observation** keyword, and the model can come back with the **Answer**

![Pasted image 20241212134059.png](Pasted%20image%2020241212134059.png)

### Create an Agent
```python

client = OpenAI()
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)

class Agent:
    def __init__(self, system=""):
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})

    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        completion = client.chat.completions.create(
                        model="gpt-4o", 
                        temperature=0,
                        messages=self.messages)
        return completion.choices[0].message.content
```

### Create a special prompt
This **prompt should mention all the available actions (tools) for our agent, and provide examples of their usages**

>[!prompt]-
>"You run in a loop of Thought, Action, PAUSE, Observation.
>At the end of the loop you output an Answer
>Use Thought to describe your thoughts about the question you have been asked.
>Use Action to run one of the actions available to you - then return PAUSE.
>Observation will be the result of running those actions.
>
>Your available actions are:
>
>calculate:
>e.g. calculate: 4 * 7 / 3
>Runs a calculation and returns the number - uses Python so be sure to use floating point syntax if necessary
>
>average_dog_weight:
>e.g. average_dog_weight: Collie
>returns average weight of a dog when given the breed
>
>Example session:
>
>Question: How much does a Bulldog weigh?
>Thought: I should look the dogs weight using average_dog_weight
>Action: average_dog_weight: Bulldog
>PAUSE
>
>You will be called again with this:
>
>Observation: A Bulldog weights 51 lbs
>
>You then output:
>
>Answer: A bulldog weights 51 lbs"



### Create mentioned tools
Implement tools as python functions, wrap them up in a dictionary, where keys are the names of the functions mentioned on a previous step 

> 
```python
def calculate(what):
    return eval(what)

def average_dog_weight(name):
    if name in "Scottish Terrier": 
        return("Scottish Terriers average 20 lbs")
    elif name in "Border Collie":
        return("a Border Collies average weight is 37 lbs")
    elif name in "Toy Poodle":
        return("a toy poodles average weight is 7 lbs")
    else:
        return("An average dog weights 50 lbs")

known_actions = {
    "calculate": calculate,
    "average_dog_weight": average_dog_weight
}
```

### Create a loop
Now, in order to run the REACT model, we have to manually implement a loop, which **will re-prompt LLM with new information **gathered with help of tools

```python
def query(question, max_turns=5):
    i = 0
    bot = Agent(prompt)
    next_prompt = question
    while i < max_turns:
        i += 1
        result = bot(next_prompt)
        print(result)
        actions = <parse_actions_code>
        if actions:
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception("Unknown action: {}: {}".format(action, action_input))
            print(" -- running {} {}".format(action, action_input))
            observation = known_actions[action](action_input)
            print("Observation:", observation)
            next_prompt = "Observation: {}".format(observation)
        else:
            return
```
## Enhanced version with usage of LangGraph

### Creating a prompt with LangGraph components

For creating a prompt, you should define not a simple python `str` object but rather:
```python
from langchain.prompts import PromptTemplate
```

Generally speaking, **the PromptTemplate is an f-string**, which can look smth like this:
![Pasted image 20241212135223.png](Pasted%20image%2020241212135223.png)
The community has came up with all kinds of useful prompts, gathered here:[LangSmith](https://smith.langchain.com/hub)

#### Creating a tool with langchain_community.tools
They act just like ordinary user-defined tools mentioned above, but, as well as with prompts, **there are a bunch of useful tools already developed by community** available inside the `langchain_community.tools` library

Some of the examples might include **Tavile web-search tool**, which can be binded to the model like:
![Pasted image 20241212135456.png](Pasted%20image%2020241212135456.png)

### Creating a Graph instead of a loop
**Most part of the designed agentic workflows include multiple agent-tool and agent-agent interactions**, which is a [RAG mechanism](Retrieval%20Augmented%20Generation%20(RAG).md), meaning that some additional information is added to the user's prompt

**The LangGraph uses graphs to represent those interactions**, so we should present a few core entities used for such representation

##### Graph State
One of the most important conception within LangGraph usage

**State is a custom user-defined object, representing the information within the graph**. 
![400](Pasted%20image%2020241212140935.png)

You should decide which information you would like to keep track of while executing the graph. For the simple REACT workflow, such as we designed manually above, the state can be defined simply as:
![Pasted image 20241212141003.png](Pasted%20image%2020241212141003.png)

This means that we do only keep track of the conversation history.
**Annotated** keyword means that we are applying some operation to the incoming data, **operator.add** here denotes that new messages are being added to the history, and do not override old one.

If we want to have a more covering representation of our graph, we can implement some other state like:
![Pasted image 20241212141134.png](Pasted%20image%2020241212141134.png)

Note, how `input`, `chat_history`, `agent_outcome` variables are **not annotated** here, meaning that they will be simply overwritten with the new data

`intermediate_steps` **is annotated** with **operator.add**, meaning that the model could use multiple loop executions to use different tools thus **accumulate more information before giving the final answer**

##### Graph overall structure
![Pasted image 20241212135827.png](Pasted%20image%2020241212135827.png)
Data is flowing from the entry point to the end point, possibly looping around for a while, to achieve greater results

In-code graph implementation may look smth like follows
```python
class ReflexionAgentGraph:  
    def __init__(self,  
                 model: BaseChatModel = None,  
                 tools: list[tool] = None,  
                 system_prompt: str = ""):  
  
        self.system = system_prompt  
        self.tools = tools or []  
  
        if model:  
            self.model = model.bind_tools(self.tools)  
  
        # Build Graph  
        self.graph = StateGraph(ReflexionAgentGraphState)  
        self.graph.add_node("llm", self.some_method)  
        self.graph.add_node("tools", ToolNode(self.tools))  
        self.graph.set_entry_point("llm")  
        self.graph.add_conditional_edges("llm", self.should_continue, {True: "tools", False: END})  
        self.graph.add_edge("tools", "llm")  
	
	def some_method(...):
		...
  
```

LangGraph has built-in tool for visualizing compiled graphs:
 ![Pasted image 20241213121253.png](Pasted%20image%2020241213121253.png)

##### Launching a graph
In order to launch a graph, we should **create an initial message, and run the invoke** command
![Pasted image 20241213121816.png](Pasted%20image%2020241213121816.png)
Here we use HumanMessage standard template to create the initial message

**The result of  `invoke()` method is the final model state:**
- **Purpose**: Executes the graph until it reaches the **end node**.
- **Output**: Returns the **final state** of the graph once the execution is complete. This includes the cumulative results from all nodes in the graph and their corresponding outputs.
- **Usage**: Best for workflows where you need the complete result at the end of the process, such as summarization, full data processing, or generating a final report.

In the example given below, our State is just a list of messages, so is our result 
>[!Note]- Result: 
>```python
{'messages': [HumanMessage(content='What is the weather in sf?'),
  AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_PvPN1v7bHUxOdyn4J2xJhYOX', 'function': {'arguments': '{"query":"weather in San Francisco"}', 'name': 'tavily_search_results_json'}, 'type': 'function'}]}, response_metadata={'token_usage': {'completion_tokens': 21, 'prompt_tokens': 153, 'total_tokens': 174, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-f8740c13-4599-4d85-8520-ae65a4606298-0', tool_calls=[{'name': 'tavily_search_results_json', 'args': {'query': 'weather in San Francisco'}, 'id': 'call_PvPN1v7bHUxOdyn4J2xJhYOX'}]),
  ToolMessage(content='[{\'url\': \'https://www.weatherapi.com/\', \'content\': "{\'location\': {\'name\': \'San Francisco\', \'region\': \'California\', \'country\': \'United States of America\', \'lat\': 37.775, \'lon\': -122.4183, \'tz_id\': \'America/Los_Angeles\', \'localtime_epoch\': 1734074379, \'localtime\': \'2024-12-12 23:19\'}, \'current\': {\'last_updated_epoch\': 1734074100, \'last_updated\': \'2024-12-12 23:15\', \'temp_c\': 13.3, \'temp_f\': 55.9, \'is_day\': 0, \'condition\': {\'text\': \'Partly cloudy\', \'icon\': \'//cdn.weatherapi.com/weather/64x64/night/116.png\', \'code\': 1003}, \'wind_mph\': 13.6, \'wind_kph\': 22.0, \'wind_degree\': 261, \'wind_dir\': \'W\', \'pressure_mb\': 1018.0, \'pressure_in\': 30.05, \'precip_mm\': 0.0, \'precip_in\': 0.0, \'humidity\': 80, \'cloud\': 75, \'feelslike_c\': 11.4, \'feelslike_f\': 52.5, \'windchill_c\': 10.0, \'windchill_f\': 49.9, \'heatindex_c\': 11.9, \'heatindex_f\': 53.5, \'dewpoint_c\': 9.7, \'dewpoint_f\': 49.4, \'vis_km\': 16.0, \'vis_miles\': 9.0, \'uv\': 0.0, \'gust_mph\': 19.7, \'gust_kph\': 31.7}}"}, {\'url\': \'https://forecast.weather.gov/MapClick.php?lat=37.7800771&lon=-122.4201615\', \'content\': \'SAN FRANCISCO DOWNTOWN (SFOC1) Lat: 37.77056°NLon: 122.42694°WElev: 150.0ft. NA. 52°F. 11°C. Humidity: 78%: ... More Information: Local Forecast Office More Local Wx 3 Day History Hourly Weather Forecast. Extended Forecast for San Francisco CA . Coastal Flood Advisory December 12, 06:00am until December 16, 01:00pm ... 12am PST Dec 12, 2024\'}, {\'url\': \'https://world-weather.info/forecast/usa/san_francisco/december-2024/\', \'content\': \'Detailed ⚡ San Francisco Weather Forecast for December 2024 - day/night 🌡️ temperatures, precipitations - World-Weather.info ... World; United States; California; Weather in San Francisco; Weather in San Francisco in December 2024. San Francisco Weather Forecast for December 2024 is based on long term prognosis and previous years\'}, {\'url\': \'https://www.almanac.com/weather/longrange/CA/San+Francisco\', \'content\': "60-Day Extended Weather Forecast for San Francisco, CA | Almanac.com Weather Weather sub-navigation FALL Forecast 2024 60-Day Long-Range Forecast 5-Day Forecast Weather Store Gardening Gardening sub-navigation Garden Store Calendar Store Weather 60-Day Extended Weather Forecast for San Francisco, CA See the 60-Day Weather Forecast for  Free 2-Month Weather Forecast October 2024 Long Range Weather Forecast for Pacific Southwest Sunny, then a few showers; mild October November 2024 Long Range Weather Forecast for Pacific Southwest The 12-Month Long-Range Weather Report From The 2024 Old Farmer\'s Almanac November 2024 to October 2025 September and October will be warmer in the north and drier than normal.See the complete 12-month weather predictions in The 2024 Old Farmer\'s Almanac. November 2024 to October 2025 Yankee Magazine"}]', name='tavily_search_results_json', tool_call_id='call_PvPN1v7bHUxOdyn4J2xJhYOX'),
  AIMessage(content='The current weather in San Francisco is partly cloudy with a temperature of 55.9°F (13.3°C). The humidity is at 80%, and the wind speed is 22.0 kph coming from the west.', response_metadata={'token_usage': {'completion_tokens': 48, 'prompt_tokens': 1062, 'total_tokens': 1110, 'prompt_tokens_details': {'cached_tokens': 0, 'audio_tokens': 0}, 'completion_tokens_details': {'reasoning_tokens': 0, 'audio_tokens': 0, 'accepted_prediction_tokens': 0, 'rejected_prediction_tokens': 0}}, 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-22f54a6e-1cb5-4d79-8b10-d0f1a19a7d1c-0')]}
  >```

# Agents Search tools

Agentic search tools are used for processing complex queries. 
- By default, LLM will try to answer the user question based on it's static weights. However, such approach has 2 main limitations
	- Relevant data can not be retrieved, so we can not ask model questions like "What was the result of the last-night football match?"
	- The LLM could not provide any source references, which leads to greater hallucinations and less trust


![Pasted image 20241213122649.png](Pasted%20image%2020241213122649.png)
Implementation of a typical agentic search-tool includes several steps:
1. Query is being split down to the subqueries. This is necessary for processing complex, nested questions like "Who was the winner of the last-night football match? Where does that team originates from? What was the weather state?"
2. For each subquery, agent decides which tool should it use to fetch corresponding data (sport-source API, weather API, wikipedia...)
3. The agent scores and filters fetched answers, keeping only the most relevant part of it
	- This can be achieved by chunking: The fetched data is being split into several chunks, and only most \<N> relevant chunks are preserved
1. The agent outputs the final answer using fetched data


# Persistence and streaming
 [Lesson](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/5/persistence-and-streaming)

- **Persistence** is about durability: storing data for future use.
- **Streaming** is about immediacy: processing and responding to data in real-time.
## Definitions

**1. Persistence**

Persistence in LangChain refers to storing intermediate data or conversational state so it can be reused later. This concept is essential for enabling applications to maintain context across sessions or allow later analysis of interactions. Key use cases and methods for persistence include:

- **Chat History Persistence**:
    
    - Storing conversations for context-aware agents or chatbots.
    - Commonly stored in databases (like SQLite, MongoDB) or file systems.
- **Vector Store Persistence**:
    
    - Storing embeddings (vector representations of text) for retrieval-augmented generation (RAG).
    - Example: Using tools like **Pinecone**, **Weaviate**, or **FAISS** to store and query vectors.
- **Pipeline or State Persistence**:
    
    - Saving the state of a chain or task execution for reproducibility.
    - Used to resume a partially completed workflow or analyze past runs.

**2. Streaming**

Streaming in LangChain refers to the real-time flow of generated data, such as outputs from a model or intermediate steps in a chain. Streaming is important for enhancing responsiveness and user experience in applications like chatbots or live data processing.

- **Token-Level Streaming**:
    
    - For LLMs that support it (like OpenAI GPT models), token-level streaming enables outputs to be displayed incrementally as they are generated.
    - Improves responsiveness, especially for large outputs.
- **Real-Time Data Streams**:
    
    - Using streaming APIs to process continuous data, like live sensor readings or financial data.
- **Streaming Callbacks**:
    
    - LangChain supports callbacks to handle streaming data at different stages of a chain (e.g., logging or visualizing intermediate steps).

## Implementing persistence
1.  Create a checkpointer (supports many External Databases):
 ![Pasted image 20241217134908.png](Pasted%20image%2020241217134908.png)
2. Compile the graph using the checkpointer:
![Pasted image 20241217140233.png](Pasted%20image%2020241217140233.png)

## Implementing streaming with persistence
1. Create a "thread" dictionary and configure a thread with a thread ID
![Pasted image 20241217140622.png](Pasted%20image%2020241217140622.png)
1. Use **`stream()`** method instead of **`ivoke()`** and pass the created thread to it:
   ![Pasted image 20241217140746.png](Pasted%20image%2020241217140746.png)

**An output of the  `stream()` method is the history of all State  changes which happened during the execution**:
- **Purpose**: Executes the graph while **streaming intermediate results** as they are generated.
- **Output**: Yields the **output of each node** as the graph progresses, in real-time.
    - Typically, it streams outputs as they become available, such as token-by-token model outputs or intermediate computation results.
- **Usage**: Ideal for real-time applications where partial results are valuable, such as:
    - Token-level streaming in a chatbot or assistant.
    - Monitoring intermediate steps in a chain or graph for debugging.
    - Displaying progress to a user as the graph executes.

As long as we keep the consistent thread id, we can ask any amount of follow up questions. If model's graph was compiled with use of the checkpointer, it will remember all the past conversation:
![Pasted image 20241217141428.png](Pasted%20image%2020241217141428.png)
![Pasted image 20241217141521.png](Pasted%20image%2020241217141521.png)


## Implementing all of that asyncrhonously

We can replace used methods with asyncrhonous analogues, pursuing several goals at once:

1.  **Handle multiple requests simultaneously without blocking the event loop**, ideal for scenarios with many simultaneous tasks (e.g., streaming tokens from multiple users in real-time).
2. **Dealing with I/O-bound tasks:** e.g., querying databases, fetching data from APIs [python multiprocessing, multithreading, asyncio](python%20multiprocessing,%20multithreading,%20asyncio.md)
3. **Resource efficency:** avoid tying up threads for tasks waiting on I/O, conserving CPU and memory resources.
4. **Convinient output:** Asynchronous streaming lets you process partial responses from the model (e.g., token-by-token) and respond dynamically.

In order to achieve this, we should modify previous steps:

1. Implement persistence by creating async checkpointer (same as before, but with slightly different methods)
```python
from langgraph.checkpoint.aiosqlite import AsyncSqliteSaver

memory = AsyncSqliteSaver.from_conn_string(":memory:")
abot = Agent(model, [tool], system=prompt, checkpointer=memory)
```

1. Implement asyncrhonous streaming
```python
messages = [HumanMessage(content="What is the weather in SF?")]
thread = {"configurable": {"thread_id": "4"}}
async for event in abot.graph.astream_events({"messages": messages}, thread, version="v1"):
    kind = event["event"]
    if kind == "on_chat_model_stream":
        content = event["data"]["chunk"].content
        if content:
            # Empty content in the context of OpenAI means
            # that the model is asking for a tool to be invoked.
            # So we only print non-empty content
            print(content, end="|")
```


# Human-in-the loop capabilities
[AI Agents in LangGraph - DeepLearning.AI](https://learn.deeplearning.ai/courses/ai-agents-in-langgraph/lesson/6/human-in-the-loop)

To let human affect the state of the graph, **we are implementing a function which could replace messages within the state**:

```python
from uuid import uuid4
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, AIMessage

"""
In previous examples we've annotated the `messages` state key
with the default `operator.add` or `+` reducer, which always
appends new messages to the end of the existing messages array.

Now, to support replacing existing messages, we annotate the
`messages` key with a customer reducer function, which replaces
messages with the same `id`, and appends them otherwise.
"""
def reduce_messages(left: list[AnyMessage], right: list[AnyMessage]) -> list[AnyMessage]:
    # assign ids to messages that don't have them
    for message in right:
        if not message.id:
            message.id = str(uuid4())
    # merge the new messages with the existing messages
    merged = left.copy()
    for message in right:
        for i, existing in enumerate(merged):
            # replace any existing messages with the same id
            if existing.id == message.id:
                merged[i] = message
                break
        else:
            # append any new messages to the end
            merged.append(message)
    return merged

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], reduce_messages]
```

Now we compile a graph using the **`interrupt_before`** parameter, which would **pause the execution before the specified node**:

```python
self.graph = graph.compile(
	checkpointer=checkpointer,
	interrupt_before=["action"]
)
```

The graph will be paused. To continue the execution, we should use the **`stream()`** method again, passing **`None`**:
```python
for event in abot.graph.stream(None, thread):
    for v in event.values():
        print(v)
```


# State memory
LangGraph do have in-built memory mechanism, which makes snapshots as the graph state changes
![Pasted image 20241218124354.png](Pasted%20image%2020241218124354.png)
This snapshots include:
	- The state itself
	- Additional configurational info, including **thread_id** and **thead_ts**
		- First one is used for asynchornous processing, sort of creating 

We can use memory in a variaty of ways:
##### 1. Accessing current state

**`get_state(thread)`** graph method is used to retrieve current state for a certain thread
![Pasted image 20241218124701.png](Pasted%20image%2020241218124701.png)

##### 2. Access the iterator of all states
![Pasted image 20241218124734.png](Pasted%20image%2020241218124734.png)

**`get_state_history(thread)`** graph method is used to retrieve all states from new to the old ones for a certain thread

##### 3. Execute from the point (Time Travel)
![Pasted image 20241218124816.png](Pasted%20image%2020241218124816.png)

This one is called "Time travel" in the official documentation
We can use both **`stream()`** and **`invoke()`** methods, passing **{thread, thread_ts}** as parameters, which allows you to launch exact thread from the exact point in a history

##### 4. Modifying the state (update_state)
[**`update_state()`**](https://langchain-ai.github.io/langgraph/how-tos/human_in_the_loop/time-travel/) is a method which allows you to modify/replace the selected state, selecting with **{thread, thread_ts}** parameters

![Pasted image 20241218125920.png](Pasted%20image%2020241218125920.png)

Here we do:
- Access the past state
- Modify current state with previous vaoules via **`update_state()`** method
- Run graph via **`stream()`** method again, running the modified current state

###### as_node
Is an additional parameter, which allows as to modify the state as we were a node. If we go re-launch the graph after that, it will continue the execution as if we just left the specified note

```python
branch_and_add = abot.graph.update_state(
    to_replay.config, 
    state_update, 
    as_node="action")
```


# Another workflows

##### Multi-agent workflow
When multiple agents modify the shared state
![Pasted image 20241219134443.png](Pasted%20image%2020241219134443.png)

##### Supervisor workflow
Basically same idea without the shared state
Is often used with great LLM as a supervisor, because reasoning and planning requires a lot of intelligence
![Pasted image 20241219134620.png](Pasted%20image%2020241219134620.png)

##### Flow engineering
This is basically a graph, which could have some cycles within it
![Pasted image 20241219134746.png](Pasted%20image%2020241219134746.png)

##### Plan and execute
Allows for the agent itself decide when to output the result to the user. One model is responsible for task-generation, woker models are responsible for solving them
![Pasted image 20241219134949.png](Pasted%20image%2020241219134949.png)

##### Language Agent Tree Search
![Pasted image 20241219135435.png](Pasted%20image%2020241219135435.png)