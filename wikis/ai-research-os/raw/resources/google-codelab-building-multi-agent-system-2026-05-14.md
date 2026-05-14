---
source: https://codelabs.developers.google.com/codelabs/production-ready-ai-roadshow/1-building-a-multi-agent-system/building-a-multi-agent-system#0
date: 2026-05-14
type: resource
tags: [multi-agent-systems, google-cloud, adk, a2a, vertex-ai, cloud-run, orchestration, agent-evaluation, self-os]
---

# Google Codelab — Building a Multi-Agent System

## Summary

This Google Codelab by Amit Maraj teaches how to build and deploy a production-ready distributed multi-agent system on Google Cloud. The worked example is a **Course Creation System** with four specialist roles: Researcher, Judge, Content Builder, and Orchestrator. The lab uses Google ADK orchestration primitives, structured Pydantic judge output, Agent-to-Agent (A2A) remote-agent connectivity, Vertex AI/Gemini, and Cloud Run microservice deployment. The important architectural idea is that multi-agent systems should be decomposed into independently testable specialists, then recomposed with explicit control-flow patterns such as loops and sequences.

## Key points

- **System shape:** Course creation pipeline: Researcher gathers data, Judge critiques quality/completeness, Content Builder creates course content, Orchestrator coordinates the workflow.
- **Specialist agents:** The codelab argues that small, focused agents are easier to evaluate, debug, and prompt-tune than one monolithic “do everything” prompt.
- **Quality loop:** A `LoopAgent` cycles Researcher → Judge → EscalationChecker until research passes or `max_iterations` is reached.
- **Structured evaluation:** The Judge returns a predictable Pydantic schema, e.g. `status: pass | fail` plus feedback, so automation can branch reliably.
- **Non-LLM control logic:** An `EscalationChecker` implemented with `BaseAgent` reads session state and emits `EventActions(escalate=True)` to break the loop.
- **Final composition:** A `SequentialAgent` runs the research loop first, then sends approved research into the Content Builder.
- **Distributed production model:** The lab deploys agents as independent Cloud Run services and connects them with A2A agent-card URLs rather than keeping every agent inside one Python process.
- **Local-to-cloud parity:** The local script runs separate uvicorn processes for each agent and passes the same style of remote-agent URLs that production Cloud Run uses.

## Architecture pattern

```text
User topic
  → Orchestrator / SequentialAgent
      → Research Loop / LoopAgent
          → Researcher Agent: web search and summarize
          → Judge Agent: structured pass/fail critique
          → EscalationChecker: break loop on pass
      → Content Builder Agent: create structured course module
  → Final course output
```

Production deployment shape:

```text
Researcher Cloud Run service
Judge Cloud Run service
Content Builder Cloud Run service
        ↑ agent-card URLs
        │
Orchestrator Cloud Run service
```

## Why it matters

This is a practical, production-oriented multi-agent tutorial rather than only a conceptual article. It demonstrates three patterns that matter for robust agent systems: **specialization**, **evaluation-before-output**, and **deployment boundaries**. The Judge + LoopAgent section is especially relevant because it turns “review” from a vague prompt into an explicit control-flow mechanism.

## Self-OS / Hermes implications

- **Matches Day/Night shift QA thinking:** The Researcher → Judge → loop pattern resembles the Self-OS preference for worker output to pass through review before becoming final.
- **Useful canonical pattern for agent workflows:** `LoopAgent` + structured Judge is a clean reference for future Hermes skills that need retry-until-quality rather than one-shot generation.
- **Distributed agents as services:** Cloud Run + A2A is a useful external reference for when Hermes/Self-OS agents need to cross process or machine boundaries, though Self-OS should still start from its current Telegram + markdown + kanban loop rather than prematurely migrating everything to cloud microservices.
- **Structured outputs over prose reviews:** The Pydantic Judge is directly relevant to avoiding vague QA. Hermes workflows should prefer explicit verdict schemas when a downstream step needs to branch.
- **Local-to-production parity:** The lab’s local uvicorn-per-agent simulation is a good reminder that local test harnesses should mimic production wiring, not hide orchestration assumptions.

## Setup commands surfaced

```bash
cd ~
git clone --depth 1 --filter=blob:none --sparse https://github.com/GoogleCloudPlatform/devrel-demos.git temp-repo && cd temp-repo && git sparse-checkout set agents/build-with-ai/production-ready-ai/prai-roadshow-lab-1-starter && cd .. && mv temp-repo/agents/build-with-ai/production-ready-ai/prai-roadshow-lab-1-starter . && rm -rf temp-repo
cd prai-roadshow-lab-1-starter

gcloud services enable   run.googleapis.com   artifactregistry.googleapis.com   cloudbuild.googleapis.com   aiplatform.googleapis.com   compute.googleapis.com

uv sync

cat <<EOF > .env
export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value project)
export GOOGLE_CLOUD_LOCATION=global
export GOOGLE_GENAI_USE_VERTEXAI=true
EOF
source .env
```

## Extraction notes

- `web_extract` successfully captured a structured codelab summary.
- Direct HTML extraction was used to recover the codelab step labels and step text from `google-codelab-step` elements.
- The user URL contained newsletter tracking parameters; the canonical source recorded above strips those parameters.

## Raw codelab content

### 1. Introduction

1. Introduction

 Overview

 In this lab, you will go beyond simple chatbots and build a distributed multi-agent system .

 While a single LLM can answer questions, real-world complexity often requires specialized roles. You don't ask your backend engineer to design the UI, and you don't ask your designer to optimize database queries. Similarly, we can create specialized AI agents that focus on one task and coordinate with each other to solve complex problems.

 You will build a Course Creation System consisting of:

 Researcher Agent : Using `google_search` to find up-to-date information.

 Judge Agent : Critiquing the research for quality and completeness.

 Content Builder Agent : Turning the research into a structured course.

 Orchestrator Agent : Managing the workflow and communication between these specialists.

 Prerequisites

 Basic Python knowledge.

 Familiarity with Google Cloud Console.

 What you'll do

 Define a tool-using agent (`researcher`) that can search the web.

 Implement structured output with Pydantic for the `judge`.

 Connect to remote agents using the Agent-to-Agent (A2A) protocol.

 Construct a `LoopAgent` to create a feedback loop between the researcher and judge.

 Run the distributed system locally using the ADK.

 Deploy the multi-agent system to Google Cloud Run .

 Architecture & Orchestration Principles

 Before we write code, let's understand how these agents work together. We are building a Course Creation Pipeline .

 The System Design

 Orchestrating with Agents

 Standard agents (like the Researcher) do work. Orchestrator Agents (like `LoopAgent` or `SequentialAgent`) manage other agents. They don't have their own tools; their "tool" is delegation.

 `LoopAgent` : This acts like a `while` loop in code. It runs a sequence of agents repeatedly until a condition is met (or max iterations reached). We use this for the Research Loop : 
 Researcher finds info.

 Judge critiques it.

 If Judge says "Fail", the EscalationChecker lets the loop continue.

 If Judge says "Pass", the EscalationChecker breaks the loop.

 `SequentialAgent` : This acts like a standard script execution. It runs agents one after another. We use this for the High-Level Pipeline : 
 First, run the Research Loop (until it finishes with good data).

 Then, run the Content Builder (to write the course).

 By combining these, we create a robust system that can self-correct before generating the final output.

### 2. Setup

2. Setup

 Environment Setup

 Open Cloud Shell : Click the Activate Cloud Shell icon in the top-right of the Google Cloud Console.

 Get the Starter Code

 Clone the starter repository into your home directory: 

```
 cd ~ 
 git clone -- depth 1 -- filter = blob : none -- sparse https : // github . com / GoogleCloudPlatform / devrel - demos . git temp - repo && cd temp - repo && git sparse - checkout set agents / build - with - ai / production - ready - ai / prai - roadshow - lab - 1 - starter && cd .. && mv temp - repo / agents / build - with - ai / production - ready - ai / prai - roadshow - lab - 1 - starter . && rm - rf temp - repo 
 cd prai - roadshow - lab - 1 - starter 

```

 Enable APIs : Run the following command to enable the necessary Google Cloud services: 

```
 gcloud services enable \
 run . googleapis . com \
 artifactregistry . googleapis . com \
 cloudbuild . googleapis . com \
 aiplatform . googleapis . com \
 compute . googleapis . com 

```

 Open this folder in your editor.

 Install Dependencies

 We use `uv` for fast dependency management.

 Install the project dependencies: 

```
 # Ensure you have uv installed: pip install uv 
 uv sync 

```

 Set up environment variables. 
 Tip : You can find your Project ID in the Cloud Console dashboard, or by running `gcloud config get-value project`.

We'll create a `.env` file to store these variables so you can easily reload them if your session disconnects. 

```
 cat << EOF > . env 
 export GOOGLE_CLOUD_PROJECT = $ ( gcloud config get - value project ) 
 export GOOGLE_CLOUD_LOCATION = global 
 export GOOGLE_GENAI_USE_VERTEXAI = true 
 EOF 

```

 Source the environment variables: 

```
 source . env 

```

 Warning: Environment variables are not persisted across new terminal sessions. If you open a new terminal tab, run `source .env` to restore them.

### 3. 🕵️ The Researcher Agent

3. 🕵️ The Researcher Agent

 The Researcher is a specialist. Its only job is to find information. To do this, it needs access to a tool: Google Search.

 Why separate the Researcher?

 Deep Dive: Why not just have one agent do everything?

 Small, focused agents are easier to evaluate and debug . If the research is bad, you iterate on the Researcher's prompt. If the course formatting is bad, you iterate on the Content Builder. In a monolithic "do-it-all" prompt, fixing one thing often breaks another.

 If you are working in Cloud Shell, run the following command to open Cloud Shell editor: 

```
 cloudshell workspace . 

```

If you are working in your local environment, open your favorite IDE.

 Open `agents/researcher/agent.py`.

 You will see a skeleton with a TODO.

 Add the following code to define the `researcher` agent: 

```
 # ... existing imports ... 

 # Define the Researcher Agent 
 researcher = Agent ( 
 name = "researcher" , 
 model = MODEL , 
 description = "Gathers information on a topic using Google Search." , 
 instruction = """ 
 You are an expert researcher. Your goal is to find comprehensive and accurate information on the user's topic. 
 Summarize your findings clearly. 
 If you receive feedback that your research is insufficient, use the feedback to refine your next search. 
 DO NOT output any function calls. Provide your research directly as text. 
 """ , 
 ) 

 root_agent = researcher 

```

 Key Concept: Tool Use

 When using Gemini 3, the Google Search tool is automatically available. If you were using a different model, e.g. Gemini 2.5, you would need to pass `tools=[google_search]` as an additional parameter to the Agent() constructor. ADK handles the complexity of describing this tool to the LLM. When the model decides it needs information, it generates a structured tool call, the ADK executes the Python function `google_search`, and feeds the result back to the model.

### 4. ⚖️ The Judge Agent

4. ⚖️ The Judge Agent

 The Researcher works hard, but LLMs can be lazy. We need a Judge to review the work. The Judge accepts the research and returns a structured Pass/Fail assessment.

 Structured Output

 Deep Dive: To automate workflows, we need predictable outputs. A rambling text review is hard to parse programmatically. By enforcing a JSON schema (using Pydantic), we ensure the Judge returns a boolean `pass` or `fail` that our code can reliably act upon.

 Open `agents/judge/agent.py`.

 Define the `JudgeFeedback` schema and the `judge` agent. 

```
 # 1. Define the Schema 
 class JudgeFeedback ( BaseModel ): 
 """Structured feedback from the Judge agent.""" 
 status : Literal [ "pass" , "fail" ] = Field ( 
 description = "Whether the research is sufficient ('pass') or needs more work ('fail')." 
 ) 
 feedback : str = Field ( 
 description = "Detailed feedback on what is missing. If 'pass', a brief confirmation." 
 ) 

 # 2. Define the Agent 
 judge = Agent ( 
 name = "judge" , 
 model = MODEL , 
 description = "Evaluates research findings for completeness and accuracy." , 
 instruction = """ 
 You are a strict editor. 
 Evaluate the 'research_findings' against the user's original request. 
 If the findings are missing key info, return status='fail'. 
 If they are comprehensive, return status='pass'. 
 """ , 
 output_schema = JudgeFeedback , 
 # Disallow delegation because it should only output the schema 
 disallow_transfer_to_parent = True , 
 disallow_transfer_to_peers = True , 
 ) 

 root_agent = judge 

```

 Key Concept: Restricting Agent Behavior

 We set `disallow_transfer_to_parent=True` and `disallow_transfer_to_peers=True`. This forces the Judge to only return the structured `JudgeFeedback`. It cannot decide to "chat" with the user or delegate to another agent. This makes it a deterministic component in our logic flow.

### 5. 🧪 Testing in Isolation

5. 🧪 Testing in Isolation

 Before connecting them, we can verify that each agent works. The ADK allows you to run agents individually.

 Key Concept: The Interactive Runtime

 `adk run` spins up a lightweight environment where you are the "user". This allows you to test the agent's instructions and tool usage in isolation. If the agent fails here (e.g., can't use Google Search), it will definitely fail in the orchestration.

 Run the Researcher interactively. Note we point to the specific agent directory: 

```
 # This runs the researcher agent in interactive mode 
 uv run adk run agents / researcher 

```

 In the chat prompt, type: 

```
 Find the population of Tokyo in 2020 

```

 It should use the Google Search tool and return the answer. Note: If you see an error indicating the project, location and use of vertex is not set, make sure your project ID is set and execute the following: 

```
 export GOOGLE_CLOUD_PROJECT = $ ( gcloud config get - value project ) 
 export GOOGLE_CLOUD_LOCATION = global 
 export GOOGLE_GENAI_USE_VERTEXAI = true 

```

 Exit the chat (Ctrl+C).

 Run the Judge interactively: 

```
 uv run adk run agents / judge 

```

 In the chat prompt, simulate the input: 

```
 Topic : Tokyo . Findings : Tokyo is a city . 

```

 It should return `status='fail'` because the findings are too brief.

### 6. ✍️ The Content Builder Agent

6. ✍️ The Content Builder Agent

 The Content Builder is the creative writer. It takes the approved research and turns it into a course.

 Open `agents/content_builder/agent.py`.

 Define the `content_builder` agent. 

```
 content_builder = Agent ( 
 name = "content_builder" , 
 model = MODEL , 
 description = "Transforms research findings into a structured course." , 
 instruction = """ 
 You are an expert course creator. 
 Take the approved 'research_findings' and transform them into a well-structured, engaging course module. 

 **Formatting Rules:** 
 1. Start with a main title using a single `#` (H1). 
 2. Use `##` (H2) for main section headings. 
 3. Use bullet points and clear paragraphs. 
 4. Maintain a professional but engaging tone. 

 Ensure the content directly addresses the user's original request. 
 """ , 
 ) 
 root_agent = content_builder 

```

 Key Concept: Context Propagation

 You might wonder: "How does the Content Builder know what the Researcher found?" In the ADK, agents in a pipeline share a `session.state`. Later, in the Orchestrator, we will configure the Researcher and Judge to save their outputs to this shared state. The Content Builder's prompt effectively has access to this history.

### 7. 🎻 The Orchestrator

7. 🎻 The Orchestrator

 The Orchestrator is the manager of our multi-agent team. Unlike the specialist agents (Researcher, Judge, Content Builder) who perform specific tasks, the Orchestrator's job is to coordinate the workflow and ensure information flows correctly between them.

 🌐 The Architecture: Agent-to-Agent (A2A)

 In this lab, we are building a distributed system . Instead of running all agents in a single Python process, we deploy them as independent microservices. This allows each agent to scale independently and fail without crashing the entire system.

 To make this possible, we use the Agent-to-Agent (A2A) protocol.

 The A2A Protocol

 Deep Dive: In a production system, agents run on different servers (or even different clouds). The A2A protocol creates a standard way for them to discover and talk to each other over HTTP. `RemoteA2aAgent` is the ADK client for this protocol.

 Open `agents/orchestrator/agent.py`.

 Locate the comment `# TODO: Define connections to remote agents` or the section for remote agent definitions.

 Add the following code to define the connections. Make sure to place this after the imports and before any other agent definitions. 

```
 # ... existing code ... 

 # Connect to the Researcher (Localhost port 8001) 
 researcher_url = os . environ . get ( "RESEARCHER_AGENT_CARD_URL" , "http://localhost:8001/a2a/agent/.well-known/agent-card.json" ) 
 researcher = RemoteA2aAgent ( 
 name = "researcher" , 
 agent_card = researcher_url , 
 description = "Gathers information using Google Search." , 
 # IMPORTANT: Save the output to state for the Judge to see 
 after_agent_callback = create_save_output_callback ( "research_findings" ), 
 # IMPORTANT: Use authenticated client for communication 
 httpx_client = create_authenticated_client ( researcher_url ) 
 ) 

 # Connect to the Judge (Localhost port 8002) 
 judge_url = os . environ . get ( "JUDGE_AGENT_CARD_URL" , "http://localhost:8002/a2a/agent/.well-known/agent-card.json" ) 
 judge = RemoteA2aAgent ( 
 name = "judge" , 
 agent_card = judge_url , 
 description = "Evaluates research." , 
 after_agent_callback = create_save_output_callback ( "judge_feedback" ), 
 httpx_client = create_authenticated_client ( judge_url ) 
 ) 

 # Content Builder (Localhost port 8003) 
 content_builder_url = os . environ . get ( "CONTENT_BUILDER_AGENT_CARD_URL" , "http://localhost:8003/a2a/agent/.well-known/agent-card.json" ) 
 content_builder = RemoteA2aAgent ( 
 name = "content_builder" , 
 agent_card = content_builder_url , 
 description = "Builds the course." , 
 httpx_client = create_authenticated_client ( content_builder_url ) 
 ) 

```

### 8. 🛑 The Escalation Checker

8. 🛑 The Escalation Checker

 A loop needs a way to stop. If the Judge says "Pass", we want to exit the loop immediately and move to the Content Builder.

 Custom Logic with BaseAgent

 Deep Dive: Not all agents use LLMs. Sometimes you need simple Python logic. `BaseAgent` lets you define an agent that just runs code. In this case, we check the session state and use `EventActions(escalate=True)` to signal the `LoopAgent` to stop.

 Still in `agents/orchestrator/agent.py`.

 Find the `EscalationChecker` TODO placeholder.

 Replace it with the following implementation: 

```
 class EscalationChecker ( BaseAgent ): 
 """Checks the judge's feedback and escalates (breaks the loop) if it passed.""" 

 async def _run_async_impl ( 
 self , ctx : InvocationContext 
 ) - > AsyncGenerator [ Event , None ]: 
 # Retrieve the feedback saved by the Judge 
 feedback = ctx . session . state . get ( "judge_feedback" ) 
 print ( f "[EscalationChecker] Feedback: { feedback } " ) 

 # Check for 'pass' status 
 is_pass = False 
 if isinstance ( feedback , dict ) and feedback . get ( "status" ) == "pass" : 
 is_pass = True 
 # Handle string fallback if JSON parsing failed 
 elif isinstance ( feedback , str ) and '"status": "pass"' in feedback : 
 is_pass = True 

 if is_pass : 
 # 'escalate=True' tells the parent LoopAgent to stop looping 
 yield Event ( author = self . name , actions = EventActions ( escalate = True )) 
 else : 
 # Continue the loop 
 yield Event ( author = self . name ) 

 escalation_checker = EscalationChecker ( name = "escalation_checker" ) 

```

 Key Concept: Control Flow via Events

 Agents communicate not just with text, but with Events . By yielding an event with `escalate=True`, this agent sends a signal up to its parent (the `LoopAgent`). The `LoopAgent` is programmed to catch this signal and terminate the loop.

### 9. 🔁 The Research Loop

9. 🔁 The Research Loop

 We need a feedback loop: Research -> Judge -> (Fail) -> Research -> ... 

 Still in `agents/orchestrator/agent.py`.

 Add the `research_loop` definition. Place this after the `EscalationChecker` class and `escalation_checker` instance. 

```
 research_loop = LoopAgent ( 
 name = "research_loop" , 
 description = "Iteratively researches and judges until quality standards are met." , 
 sub_agents = [ researcher , judge , escalation_checker ], 
 max_iterations = 3 , 
 ) 

```

 Key Concept: LoopAgent

 The `LoopAgent` cycles through its `sub_agents` in order.

 `researcher`: Finds data.

 `judge`: Evaluates data.

 `escalation_checker`: Decides whether to `yield Event(escalate=True)`. If `escalate=True` happens, the loop breaks early. Otherwise, it restarts at the researcher (up to `max_iterations`).

### 10. 🔗 The Final Pipeline

10. 🔗 The Final Pipeline

 Finally, stitch it all together.

 Still in `agents/orchestrator/agent.py`.

 Define the `root_agent` at the bottom of the file. Ensure this replaces any existing `root_agent = None` placeholder. 

```
 root_agent = SequentialAgent ( 
 name = "course_creation_pipeline" , 
 description = "A pipeline that researches a topic and then builds a course from it." , 
 sub_agents = [ research_loop , content_builder ], 
 ) 

```

 Key Concept: Hierarchical Composition

 Notice that `research_loop` is itself an agent (a `LoopAgent`). We treat it just like any other sub-agent in the `SequentialAgent`. This composability allows you to build complex logic by nesting simple patterns (loops inside sequences, sequences inside routers, etc.).

### 11. 💻 Run Locally

11. 💻 Run Locally

 Before we run everything, let's look at how the ADK simulates the distributed environment locally.

 Deep Dive: How Local Development Works

 In a microservices architecture, every agent runs as its own server. When you deploy, you'll have 4 different Cloud Run services. Simulating this locally can be painful if you have to open 4 terminal tabs and run 4 commands.

 This script starts `uvicorn` processes for the Researcher (port 8001), Judge (8002), and Content Builder (8003). It sets environment variables like `RESEARCHER_AGENT_CARD_URL` and passes them to the Orchestrator (port 8004). This is exactly how we'll configure it in the cloud later!

 Run the orchestration script: 

```
 perl - pi - e 's/us-central1/global/g' run_local . sh 
 ./ run_local . sh 

```

 This starts 4 separate processes. 

 Test it: 
 If using Cloud Shell: Click the Web Preview button (top right of the terminal) -> Preview on port 8080 -> Change port to `8000`.

 If running locally: Open `http://localhost:8000` in your browser.

 Prompt: "Create a course about the history of coffee." 

 Observe: The Orchestrator will call the Researcher. The output goes to the Judge. If the Judge fails it, the loop continues!

 Troubleshooting: 
 "Internal Server Error" / Auth Errors: If you see authentication errors (e.g., related to `google-auth`), ensure you have run `gcloud auth application-default login` if running on a local machine. In Cloud Shell, ensure your `GOOGLE_CLOUD_PROJECT` environment variable is set correctly.

 Terminal Errors: If the command fails in a new terminal window, remember to re-export your environment variables (`GOOGLE_CLOUD_PROJECT`, etc.).

 Testing Agents in Isolation: Even when the full system is running, you can test specific agents by targeting their ports directly. This is useful for debugging a specific component without triggering the entire chain. Note: These are API endpoints, not web pages. You cannot access them via a browser. Instead, use `curl` to verify they are running (e.g., by fetching their agent card). 
 Researcher Only (Port 8001): 
 Check status (and find the `url` endpoint): 

```
 curl http : // localhost : 8001 / a2a / agent /. well - known / agent - card . json 

```

 Send a query (using the A2A JSON-RPC protocol): 

```
 curl - X POST http : // localhost : 8001 / a2a / agent \
 - H "Content-Type: application/json" \
 - d '{ 
 "jsonrpc" : "2.0" , 
 "method" : "message/send" , 
 "id" : 1 , 
 "params" : { 
 "message" : { 
 "message_id" : "test-1" , 
 "role" : "user" , 
 "parts" : [ 
 { 
 "text" : "What is the capital of France?" , 
 "kind" : "text" 
 } 
 ] 
 } 
 } 
 } ' 

```

 Judge Only (Port 8002): 
 Check status: 

```
 curl http : // localhost : 8002 / a2a / agent /. well - known / agent - card . json 

```

 Send a query: 

```
 curl - X POST http : // localhost : 8002 / a2a / agent \
 - H "Content-Type: application/json" \
 - d '{ 
 "jsonrpc" : "2.0" , 
 "method" : "message/send" , 
 "id" : 1 , 
 "params" : { 
 "message" : { 
 "message_id" : "test-2" , 
 "role" : "user" , 
 "parts" : [ 
 { 
 "text" : "Topic: Tokyo. Findings: Tokyo is the capital of Japan." , 
 "kind" : "text" 
 } 
 ] 
 } 
 } 
 } ' 

```

 Content Builder Only (Port 8003): 

```
 curl http : // localhost : 8003 / a2a / agent /. well - known / agent - card . json 

```

 Orchestrator (Port 8004): 

```
 curl http : // localhost : 8004 / a2a / agent /. well - known / agent - card . json 

```

### 12. 🚀 Deploy to Cloud Run

12. 🚀 Deploy to Cloud Run

 The ultimate validation is running in the cloud. We will deploy each agent as a separate service.

 Understanding Deployment Configuration

 When deploying agents to Cloud Run, we pass several environment variables to configure their behavior and connectivity:

 `GOOGLE_CLOUD_PROJECT` : Ensures the agent uses the correct Google Cloud project for logging and Vertex AI calls.

 `GOOGLE_GENAI_USE_VERTEXAI` : Tells the agent framework (ADK) to use Vertex AI for model inference instead of calling Gemini APIs directly.

 `GOOGLE_CLOUD_LOCATION` : Tells the agent framework (ADK) to use which endpoint.

 `[AGENT]_AGENT_CARD_URL` : This is crucial for the Orchestrator. It tells the Orchestrator where to find the remote agents. By setting this to the deployed Cloud Run URL (specifically the agent card path), we enable the Orchestrator to discover and communicate with the Researcher, Judge, and Content Builder over the internet.

 Deploy the Sub-Agents (Parallel): To save time, we will deploy the Researcher, Judge, and Content Builder simultaneously. Open three new terminal tabs. In each new tab, run the following to setup your environment: 

```
 cd ~/ prai - roadshow - lab - 1 - starter 
 source . env 

```

 Tab 1: Run the Researcher deployment: 

```
 gcloud run deploy researcher \
 -- source agents / researcher / \
 -- region us - west1 \
 -- allow - unauthenticated \
 -- labels dev - tutorial = prod - ready - 1 \
 -- set - env - vars GOOGLE_CLOUD_PROJECT = $ GOOGLE_CLOUD_PROJECT \
 -- set - env - vars GOOGLE_CLOUD_LOCATION = $ GOOGLE_CLOUD_LOCATION \
 -- set - env - vars GOOGLE_GENAI_USE_VERTEXAI = "true" 

```

 Tab 2: Run the Judge deployment: 

```
 gcloud run deploy judge \
 -- source agents / judge / \
 -- region us - west1 \
 -- allow - unauthenticated \
 -- labels dev - tutorial = prod - ready - 1 \
 -- set - env - vars GOOGLE_CLOUD_PROJECT = $ GOOGLE_CLOUD_PROJECT \
 -- set - env - vars GOOGLE_CLOUD_LOCATION = $ GOOGLE_CLOUD_LOCATION \
 -- set - env - vars GOOGLE_GENAI_USE_VERTEXAI = "true" 

```

 Tab 3: Run the Content Builder deployment: 

```
 gcloud run deploy content - builder \
 -- source agents / content_builder / \
 -- region us - west1 \
 -- allow - unauthenticated \
 -- labels dev - tutorial = prod - ready - 1 \
 -- set - env - vars GOOGLE_CLOUD_PROJECT = $ GOOGLE_CLOUD_PROJECT \
 -- set - env - vars GOOGLE_CLOUD_LOCATION = $ GOOGLE_CLOUD_LOCATION \
 -- set - env - vars GOOGLE_GENAI_USE_VERTEXAI = "true" 

```

 Capture the URLs: Once all three deployments have finished, return to your original terminal (where you will deploy the Orchestrator). Run the following commands to capture the service URLs: 

```
 RESEARCHER_URL = $ ( gcloud run services describe researcher -- region us - west1 -- format = 'value(status.url)' ) 
 JUDGE_URL = $ ( gcloud run services describe judge -- region us - west1 -- format = 'value(status.url)' ) 
 CONTENT_BUILDER_URL = $ ( gcloud run services describe content - builder -- region us - west1 -- format = 'value(status.url)' ) 

 echo "Researcher: $RESEARCHER_URL" 
 echo "Judge: $JUDGE_URL" 
 echo "Content Builder: $CONTENT_BUILDER_URL" 

```

 Deploy the Orchestrator: Use the captured environment variables to configure the Orchestrator. 

```
 gcloud run deploy orchestrator \
 -- source agents / orchestrator / \
 -- region us - west1 \
 -- allow - unauthenticated \
 -- labels dev - tutorial = prod - ready - 1 \
 -- set - env - vars RESEARCHER_AGENT_CARD_URL = $ RESEARCHER_URL / a2a / agent /. well - known / agent - card . json \
 -- set - env - vars JUDGE_AGENT_CARD_URL = $ JUDGE_URL / a2a / agent /. well - known / agent - card . json \
 -- set - env - vars CONTENT_BUILDER_AGENT_CARD_URL = $ CONTENT_BUILDER_URL / a2a / agent /. well - known / agent - card . json \
 -- set - env - vars GOOGLE_CLOUD_PROJECT = $ GOOGLE_CLOUD_PROJECT \
 -- set - env - vars GOOGLE_CLOUD_LOCATION = $ GOOGLE_CLOUD_LOCATION \
 -- set - env - vars GOOGLE_GENAI_USE_VERTEXAI = "true" 

```

 Capture the URL: 

```
 ORCHESTRATOR_URL = $ ( gcloud run services describe orchestrator -- region us - west1 -- format = 'value(status.url)' ) 
 echo $ ORCHESTRATOR_URL 

```

 Deploy the Frontend: 

```
 gcloud run deploy course - creator \
 -- source app \
 -- region us - west1 \
 -- allow - unauthenticated \
 -- labels dev - tutorial = prod - ready - 1 \
 -- set - env - vars AGENT_SERVER_URL = $ ORCHESTRATOR_URL \
 -- set - env - vars GOOGLE_CLOUD_PROJECT = $ GOOGLE_CLOUD_PROJECT 

```

 Test Remote Deployment: Open the URL of your deployed Orchestrator. It's now running entirely in the cloud, utilizing Google's serverless infrastructure to scale your agents! Hint : You will find all the micro-services and their URLs in the Cloud Run interface

### 13. Summary

13. Summary

 Congratulations! You have successfully built and deployed a production-ready, distributed multi-agent system.

 What we've accomplished

 Decomposed a Complex Task : Instead of one giant prompt, we split the work into specialized roles (Researcher, Judge, Content Builder).

 Implemented Quality Control : We used a `LoopAgent` and a structured `Judge` to ensure only high-quality information reaches the final step.

 Built for Production : By using the Agent-to-Agent (A2A) protocol and Cloud Run , we created a system where each agent is an independent, scalable microservice. This is far more robust than running everything in a single Python script.

 Orchestration : We used `SequentialAgent` and `LoopAgent` to define clear control flow patterns.

 Next Steps

 Now that you have the foundation, you can extend this system:

 Add more tools : Give the Researcher access to internal documents or APIs.

 Improve the Judge : Add more specific criteria or even a "Human in the Loop" step.

 Swap Models : Try using different models for different agents (e.g., a faster model for the Judge, a stronger model for the Content Writer).

 You are now ready to build complex, reliable agentic workflows on Google Cloud!
