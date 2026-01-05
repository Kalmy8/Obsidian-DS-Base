# DeepEval Judge Models Guide

## What Are Judge Models?

**Judge models** are the LLMs used by DeepEval metrics to evaluate outputs using the **LLM-as-a-judge** approach. Instead of using rule-based evaluation, metrics use another LLM (the "judge") to assess the quality, correctness, or other properties of your LLM's outputs.

**Key Points:**
- Judge models evaluate your LLM application's outputs
- They're used internally by metrics (you don't call them directly)
- You can configure which judge model to use per metric or globally
- Default judge model is typically GPT-4.1

---

## Available Judge Models

### **1. OpenAI Models**

**Supported Models:**
- `gpt-4.1` (default)
- `gpt-4o`
- `gpt-4-turbo`
- `gpt-3.5-turbo`
- `o1-preview`
- `o1-mini`

**Initialization:**

**Option A: Via Model String (Simplest)**
```python
from deepeval.metrics import AnswerRelevancyMetric

metric = AnswerRelevancyMetric(
    model="gpt-4o",  # Specify model as string
    threshold=0.7
)
```

**Option B: Via Environment Variable**
```bash
export OPENAI_API_KEY=<your-openai-api-key>
```

Then use in Python:
```python
# Uses default model (gpt-4.1) if not specified
metric = AnswerRelevancyMetric(model="gpt-4o")
```

**Option C: Via OpenAI Model Class**
```python
from deepeval.models import OpenAIModel
from deepeval.metrics import AnswerRelevancyMetric

model = OpenAIModel(
    model="gpt-4o",
    api_key="your-api-key"  # Optional if env var is set
)

metric = AnswerRelevancyMetric(model=model)
```

**When to Use:**
- High-quality evaluation needed
- Most common choice
- Good balance of quality and cost

---

### **2. Anthropic Models**

**Supported Models:**
- `claude-3-7-sonnet-latest`
- `claude-3-5-sonnet-20241022`
- `claude-3-opus-20240229`
- `claude-3-haiku-20240307`

**Initialization:**

**Option A: Via Environment Variable**
```bash
export ANTHROPIC_API_KEY=<your-anthropic-api-key>
```

Then in Python:
```python
from deepeval.metrics import AnswerRelevancyMetric

metric = AnswerRelevancyMetric(
    model="claude-3-7-sonnet-latest"
)
```

**Option B: Via AnthropicModel Class**
```python
from deepeval.models import AnthropicModel
from deepeval.metrics import AnswerRelevancyMetric

model = AnthropicModel(
    model="claude-3-7-sonnet-latest",
    api_key="your-anthropic-api-key"  # Optional if env var is set
)

metric = AnswerRelevancyMetric(model=model)
```

**When to Use:**
- Alternative to OpenAI
- High-quality evaluation
- Different reasoning style

---

### **3. Grok Models (xAI)**

**Supported Models:**
- `grok-4.1`
- `grok-beta`

**Initialization:**

**Step 1: Install SDK**
```bash
pip install xai-sdk
```

**Step 2: Configure via CLI**
```bash
deepeval set-grok \
    --model grok-4.1 \
    --api-key="your-api-key" \
    --temperature=0 \
    --save  # Persist settings
```

**Step 3: Use in Python**
```python
from deepeval.metrics import AnswerRelevancyMetric

# Uses Grok as default judge model
metric = AnswerRelevancyMetric()
```

**To Unset Grok:**
```bash
deepeval unset-grok
```

**When to Use:**
- Alternative provider
- xAI ecosystem integration

---

### **4. Gemini Models (Google)**

**Supported Models:**
- `gemini-2.0-flash-001`
- `gemini-1.5-pro`
- `gemini-1.5-flash`

**Initialization:**

**Option A: Via CLI**
```bash
deepeval set-gemini \
    --model-name="gemini-2.0-flash-001" \
    --google-api-key="your-api-key" \
    --save
```

**Option B: Via Python (Vertex AI)**
```python
from deepeval.models import GeminiModel

model = GeminiModel(
    model_name="gemini-1.5-pro",
    project="your-project-id",
    location="us-central1"
)

from deepeval.metrics import AnswerRelevancyMetric
metric = AnswerRelevancyMetric(model=model)
```

**To Unset Gemini:**
```bash
deepeval unset-gemini
```

**When to Use:**
- Google Cloud integration
- Cost-effective evaluation
- Alternative to OpenAI/Anthropic

---

### **5. Azure OpenAI**

**Initialization:**

**Via CLI:**
```bash
deepeval set-azure-openai \
    --openai-endpoint="https://your-resource.openai.azure.com" \
    --openai-api-key="your-api-key" \
    --openai-model-name="gpt-4" \
    --deployment-name="gpt-4-deployment" \
    --openai-api-version="2024-02-15-preview" \
    --save
```

**Then use in Python:**
```python
from deepeval.metrics import AnswerRelevancyMetric

# Uses Azure OpenAI as default
metric = AnswerRelevancyMetric()
```

**To Unset Azure OpenAI:**
```bash
deepeval unset-azure-openai
```

**When to Use:**
- Enterprise Azure deployments
- Compliance requirements
- Azure-specific infrastructure

---

### **6. Amazon Bedrock**

**Supported Models:**
- Any model available through Bedrock Runtime Converse API
- Claude models via Bedrock
- Llama models via Bedrock

**Initialization:**

**Step 1: Set AWS Credentials**
```bash
export AWS_ACCESS_KEY_ID=<your-aws-access-key-id>
export AWS_SECRET_ACCESS_KEY=<your-aws-secret-access-key>
export AWS_REGION=us-east-1  # Optional
```

**Step 2: Use in Python**
```python
from deepeval.models import AmazonBedrockModel
from deepeval.metrics import AnswerRelevancyMetric

model = AmazonBedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20241022-v2:0",
    region="us-east-1"
)

metric = AnswerRelevancyMetric(model=model)
```

**Note:** Requires `aiobotocore` and `botocore`. DeepEval will prompt for installation if missing.

**When to Use:**
- AWS infrastructure
- Using Bedrock models
- Enterprise AWS deployments

---

### **7. DeepSeek Models**

**Supported Models:**
- `deepseek-chat`
- `deepseek-reasoner`

**Initialization:**

**Via Python:**
```python
from deepeval.models import DeepSeekModel
from deepeval.metrics import AnswerRelevancyMetric
import os

model = DeepSeekModel(
    model="deepseek-chat",
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    temperature=0
)

metric = AnswerRelevancyMetric(model=model)
```

**Environment Variable:**
```bash
export DEEPSEEK_API_KEY=<your-api-key>
```

**When to Use:**
- Cost-effective alternative
- DeepSeek model access

---

### **8. LiteLLM (Universal Provider)**

**Description:** Use any model supported by LiteLLM, including:
- OpenAI models
- Anthropic models
- Google models
- Local models (Ollama, etc.)
- Many other providers

**Initialization:**

**Step 1: Install LiteLLM**
```bash
pip install litellm
```

**Step 2: Configure via CLI**
```bash
# OpenAI via LiteLLM
deepeval set-litellm openai/gpt-3.5-turbo

# Anthropic via LiteLLM
deepeval set-litellm anthropic/claude-3-opus

# Google via LiteLLM
deepeval set-litellm google/gemini-pro

# With API key
deepeval set-litellm openai/gpt-4 --api-key="your-key"
```

**Step 3: Use in Python**
```python
from deepeval.metrics import AnswerRelevancyMetric

# Uses LiteLLM-configured model
metric = AnswerRelevancyMetric()
```

**When to Use:**
- Multiple provider support
- Local models (Ollama)
- Unified interface for many providers
- Custom model endpoints

---

## Default Judge Models

**Default Behavior:**
- If no model is specified, DeepEval uses **GPT-4.1** as the default judge
- You can override this per-metric or globally via CLI

**Setting Global Default:**

**Via CLI (OpenAI):**
```bash
# Already default, but you can explicitly set
deepeval set-openai --model gpt-4o --save
```

**Via CLI (Other Providers):**
```bash
# Set Grok as default
deepeval set-grok --model grok-4.1 --save

# Set Anthropic as default
# (Set ANTHROPIC_API_KEY env var, then use AnthropicModel in code)
```

---

## Using Judge Models in Metrics

### **Method 1: Per-Metric Configuration**

```python
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric

# Different models for different metrics
relevancy_metric = AnswerRelevancyMetric(
    model="gpt-4o",  # High-quality judge
    threshold=0.7
)

faithfulness_metric = FaithfulnessMetric(
    model="gpt-3.5-turbo",  # Cost-effective judge
    threshold=0.8
)
```

### **Method 2: Shared Model Instance**

```python
from deepeval.models import AnthropicModel
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric

# Create model once, reuse
judge_model = AnthropicModel(model="claude-3-7-sonnet-latest")

# Use same model for multiple metrics
relevancy_metric = AnswerRelevancyMetric(model=judge_model)
faithfulness_metric = FaithfulnessMetric(model=judge_model)
```

### **Method 3: Global Default (CLI)**

```bash
# Set global default
deepeval set-grok --model grok-4.1 --save

# All metrics use Grok unless overridden
```

```python
from deepeval.metrics import AnswerRelevancyMetric

# Uses global default (Grok)
metric = AnswerRelevancyMetric()
```

---

## Model Selection Guidelines

### **Quality vs Cost Trade-offs**

| Model | Quality | Cost | Speed | Use Case |
|-------|---------|------|-------|----------|
| `gpt-4.1` | Highest | High | Medium | Production, critical evaluations |
| `gpt-4o` | Very High | Medium | Fast | Balanced quality/cost |
| `gpt-3.5-turbo` | Good | Low | Fast | High-volume, cost-sensitive |
| `claude-3-7-sonnet` | Very High | High | Medium | Alternative to GPT-4 |
| `gemini-1.5-pro` | High | Low | Fast | Cost-effective alternative |
| `grok-4.1` | High | Medium | Fast | xAI ecosystem |

### **Recommendations**

**For Production:**
- Use `gpt-4.1` or `gpt-4o` for critical metrics
- Use `gpt-3.5-turbo` for high-volume, less critical metrics

**For Development:**
- Use `gpt-3.5-turbo` or `gemini-1.5-flash` for faster iteration
- Switch to `gpt-4.1` for final validation

**For Cost Optimization:**
- Use `gpt-3.5-turbo` for most metrics
- Use `gpt-4o` only for critical quality checks
- Consider `gemini-1.5-flash` for high-volume evaluations

---

## Advanced Configuration

### **Custom Model Parameters**

```python
from deepeval.models import OpenAIModel

model = OpenAIModel(
    model="gpt-4o",
    temperature=0,  # Deterministic evaluation
    max_tokens=1000,
    api_key="your-key"
)

metric = AnswerRelevancyMetric(model=model)
```

### **Custom LLM Integration**

Create a custom judge model by extending `DeepEvalBaseLLM`:

```python
from deepeval.models import DeepEvalBaseLLM
from deepeval.metrics import AnswerRelevancyMetric

class CustomJudgeModel(DeepEvalBaseLLM):
    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key
    
    def generate(self, prompt: str) -> str:
        # Implement your model's generation logic
        # Return the generated text
        pass
    
    async def a_generate(self, prompt: str) -> str:
        # Async version
        pass
    
    def get_model_name(self) -> str:
        return self.model_name

# Use custom model
custom_model = CustomJudgeModel("my-model", "api-key")
metric = AnswerRelevancyMetric(model=custom_model)
```

---

## Environment Variables Summary

```bash
# OpenAI
export OPENAI_API_KEY=<key>

# Anthropic
export ANTHROPIC_API_KEY=<key>

# Google (for Gemini)
export GOOGLE_API_KEY=<key>

# AWS (for Bedrock)
export AWS_ACCESS_KEY_ID=<key>
export AWS_SECRET_ACCESS_KEY=<key>
export AWS_REGION=us-east-1

# DeepSeek
export DEEPSEEK_API_KEY=<key>
```

---

## Common Patterns

### **Pattern 1: High-Quality Evaluation**
```python
from deepeval.metrics import AnswerRelevancyMetric, FaithfulnessMetric

metrics = [
    AnswerRelevancyMetric(model="gpt-4.1", threshold=0.7),
    FaithfulnessMetric(model="gpt-4.1", threshold=0.8)
]
```

### **Pattern 2: Cost-Optimized**
```python
metrics = [
    AnswerRelevancyMetric(model="gpt-3.5-turbo", threshold=0.7),
    FaithfulnessMetric(model="gpt-3.5-turbo", threshold=0.8)
]
```

### **Pattern 3: Mixed Strategy**
```python
# Critical metric uses better model
faithfulness = FaithfulnessMetric(model="gpt-4.1", threshold=0.8)

# Less critical uses cheaper model
relevancy = AnswerRelevancyMetric(model="gpt-3.5-turbo", threshold=0.7)
```

### **Pattern 4: Provider Diversity**
```python
from deepeval.models import AnthropicModel, OpenAIModel

# Use different providers for comparison
openai_metric = AnswerRelevancyMetric(model=OpenAIModel("gpt-4o"))
anthropic_metric = AnswerRelevancyMetric(model=AnthropicModel("claude-3-7-sonnet-latest"))
```

---

## Troubleshooting

### **Issue: Model Not Found**
```python
# Ensure model name is correct
metric = AnswerRelevancyMetric(model="gpt-4o")  # ✅ Correct
metric = AnswerRelevancyMetric(model="gpt4")    # ❌ Wrong
```

### **Issue: API Key Not Set**
```bash
# Check environment variable
echo $OPENAI_API_KEY

# Or set it
export OPENAI_API_KEY="your-key"
```

### **Issue: Model Not Supported**
- Check provider documentation for supported models
- Use LiteLLM for broader model support
- Verify API access/permissions

---

## References

- [DeepEval Model Integrations](https://deepeval.com/integrations/models)
- [OpenAI Integration](https://deepeval.com/integrations/models/openai)
- [Anthropic Integration](https://deepeval.com/integrations/models/anthropic)
- [Grok Integration](https://deepeval.com/integrations/models/grok)
- [Gemini Integration](https://deepeval.com/integrations/models/gemini)
- [Azure OpenAI Integration](https://deepeval.com/integrations/models/azure-openai)
- [Amazon Bedrock Integration](https://deepeval.com/integrations/models/amazon-bedrock)
- [LiteLLM Integration](https://deepeval.com/integrations/models/litellm)




