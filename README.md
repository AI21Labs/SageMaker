# Deploy AI21 Labs Language Models on AWS SageMaker

Examples for using Jurassic-2 models through Amazon SageMaker.

## Installation

You can install the package using pip:

```
pip install -U "ai21[AWS]"
```

And then import the package:

```
import ai21
```

## Quickstart

In order to use this library, you must configure your AWS credentials.

All set up? Make your first interaction with Jurassic-2:

```python
response = ai21.Completion.execute(destination=ai21.SageMakerDestination("j2-ultra"),
                                   prompt="To be, or",
                                   maxTokens=4,
                                   temperature=0)

print(response['completions'][0]['data']['text'])
# not to be: that is the question
```

For more comprehensive quickstart guides, see:

#### Foundation models

[Jurassic-2 Ultra](J2_Ultra_example_model_use.ipynb)

[Jurassic-2 Mid Instruct](J2_Mid_example_model_use.ipynb)

[Jurassic-2 Light](J2_Light_example_model_use.ipynb)

### Task-specific models

[AI21 Summarize](AI21_Summarize_example_model_use.ipynb)

[AI21 Contextual Answers](AI21_ContextualAnswers_example_model_use.ipynb)

[AI21 Paraphrase](AI21_Paraphrase_example_model_use.ipynb)

[AI21 Grammatical Error Correction (GEC)](AI21_GEC_example_model_use.ipynb)

## Learn more

- [AI21 Studio website](http://www.ai21.com/studio)

- [Our technical docs](http://docs.ai21.com)

- [AI21 Studio playground](https://studio.ai21.com/playground) - no code environment to test and perfect your prompts
