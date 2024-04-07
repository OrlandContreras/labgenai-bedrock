# Introduction to Amazon Bedrock

Amazon Bedrock is a fully managed service that offers leading foundation models
(FMs) and a set of tools to quickly build and scale generative AI applications.
The service also helps ensure privacy and security.

With agents for Amazon Bedrock (preview), you can automate complex business
tasks and orchestrations using fully managed agents.With knowledge bases for
Amazon Bedrock (preview), you can integrate company data with the query so the
responses from the FMs are specific to your domain and organization.

## Key benefits

1. Efficiently build with FMs
2. Securely build generative AI applications
3. Deliver customized experiences using your organization data
   1. **Automate orchestration and complex business tasks using agents for
      Amazon Bedrock (preview):** Agents for Amazon Bedrock (preview) makes it
      easy to create and deploy fully managed agents that perform complex business
      tasks by dynamically invoking APIs. Agents use automatic prompt creation to
      generate prompts from developer instructions, API schemas, and company
      knowledge bases. An agent breaks down user requests into subtasks and
      determines the optimal sequence to complete them. Agents can connect to
      company data sources, convert data to numeric representations, and augment
      user requests with relevant information. This allows the agent to generate
      more accurate and relevant responses by looking up details from knowledge bases.
   2. **Supplement organization-specific information to the FM and generate
      accurate responses using knowledge bases for Amazon Bedrock (preview):**
      You can deliver contextual and relevant responses by incorporating
      organization-specific data through a process known as Retrieval Augmented
      Generation (RAG). With knowledge bases for Amazon Bedrock (preview), you can
      connect to your data sources to make the FMs knowledgeable about your
      specific domain and organization.
   3. **Fine-tune FMs using Amazon Bedrock:** You can fine-tune a foundation
      model using Amazon Bedrock by providing your own labeled training dataset in
      order to improve the model’s performance on specific tasks. Through this
      process, you create a new model that improves upon the performance and
      efficiency of the original model for a given task. To fine-tune a model, you
      upload a training and a validation dataset to Amazon S3, and provide the
      S3 bucket path to the Amazon Bedrock fine-tuning job.
      The fine-tuning can be done using the Amazon Bedrock console or API.

See also: [Amazon Bedrock API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)
