# Deploy AI21 Labs Language Models on AWS SageMaker

Examples for using Jurassic-2 models through Amazon SageMaker.

## Installation

You can install the package using pip:

```
pip install -U "ai21[SM]"
```

And then import the package:

```
import ai21
```

## Quickstart

In order to use this library, you must configure your AWS credentials.

All set up? Make your first interaction with Jurassic-2:

```python
response = ai21.Completion.execute(
    sm_endpoint="j2-grande",
    prompt="To be, or",
    maxTokens=4,
)

print(response['completions'][0]['data']['text'])
# not to be: that is the question
```

For more comprehensive quickstart guides, see:

#### Foundation models

[Jurassic-2 Jumbo Instruct](J2_JumboInstruct_example_model_use.ipynb) | [Jurassic-2 Jumbo](J2_Jumbo_example_model_use.ipynb)

[Jurassic-2 Grande Instruct](J2_GrandeInstruct_example_model_use.ipynb) | [Jurassic-2 Grande](J2_Grande_example_model_use.ipynb)

[Jurassic-2 Large](J2_Large_example_model_use.ipynb)

### Task-specific models

[AI21 Summarize](AI21_Summarize_example_model_use.ipynb)

## Learn more

- [AI21 Studio website](http://www.ai21.com/studio)

- [Our technical docs](http://docs.ai21.com)

- [AI21 Studio playground](https://studio.ai21.com/playground) - no code environment to test and perfect your prompts
