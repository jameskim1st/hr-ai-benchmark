---
url: "https://blogs.cisco.com/cisco-on-cisco/cisco-secure-internal-ai-assistant"
title: "Transforming work at Cisco with our internal AI assistant, purpose-built with security"
publisher: "Cisco"
publication_date: 2025-11-17
fetched_at: 2026-09-27
http_status: 200
content_hash: "3f6e0790d0065216"
snapshot_quality: full
chars: 10502
note: "raw 스냅샷 — 수정 금지. 본문은 trafilatura 자동 추출 결과이며 광고·내비게이션이 섞일 수 있음."
---
# Transforming work at Cisco with our internal AI assistant, purpose-built with security

Cisco wanted to make generative AI available to every single employee in a secure, cost-optimized way. To do this, Cisco IT developed an internal AI-powered assistant — purpose-built with security — designed to elevate how employees work. More than just another tool, Cisco’s internal AI assistant drives significant efficiency and frictionless experiences for employees – with 73% of users reporting increased productivity and an average time savings of 5 hours per week.
As AI tools like ChatGPT emerged in the marketplace, we saw both opportunity and risk. While Cisco recognized the transformative power of AI and the outcomes these tools could enable for our organization, the increasing usage of public AI solutions also raised critical safety and security concerns for enterprises.
Seven in ten executives believe generative AI in the enterprise introduces new security risks for company data and are concerned about employees inputting personally identifiable information (PII), client data, or propriety information into engines like ChatGPT and Google Gemini (Salesforce, 2023). Relying on external AI services could expose sensitive Cisco data to public training sets — a risk we weren’t willing to take.
We needed a solution that made generative AI available to every single employee, no matter where they work from, while keeping Cisco data secure and internal.
First steps to a secure solution
From day one, our priority was keeping Cisco’s data secure and in-house, not in someone else’s training set. The original architecture Cisco’s Development Team released in April 2023 was designed to provide a secure environment for employees to safely experiment with AI tools. It was an enterprise-wide solution powered by Azure OpenAI models that maintained a conversation prompt store, audited prompts in real time, and automatically redacted personally identifiable information (PII) prior to processing.
Eight months after launch, the Cisco IT design team stepped in to enhance user experience and drive broader adoption. Initially, only 30% of the workforce — primarily technical employees — were using the tool. The goal was to ensure all employees, regardless of their technical background, could benefit from it.
The team took a user-centric and data-driven approach, conducting foundational and generative research to fully understand what employees needed from this tool. By leveraging all the available data about user pain points, identifying what employees were searching for, and comparing it with the top areas of friction, the design team built out key use cases for the assistant. These included features to help employees brainstorm, code, translate, generate content, learn about Cisco products, and more — ultimately lifting the load of everyday work.
This research revealed that the number one thing employees were looking for was IT support — meaning the true potential of Cisco’s internal AI assistant could be unlocked through ingesting Cisco data. This became the highest priority.
Moving forward to support employees
We started by ingesting Cisco People and Communities and Help Zone data (articles, websites, and reports) into the tool. We had Retrieval Augmented Generation (RAG) solutions built for Cisco.com and SalesConnect (internal content portal for all sales resources) applications earlier. The same capabilities were added to the internal AI assistant as well to gauge the needs of sales users — a target audience our team wanted to address.
With this high-quality Cisco data ingested in the tool, employees can use AI for support case troubleshooting, creative writing, data analysis, questions, and even technical tasks like network monitoring and configuration. It can also streamline the onboarding process for new hires by supporting laptop or mobile phone setup and answering questions about expense reports.
Establishing an ongoing operating model
Cisco’s internal AI assistant was built for rapid integration, robust security, and actionable insights, all at a global scale. This is supported by an ongoing operating model where our team continuously monitors user feedback and delivers features with agility, creating an iterative, full-circle process.
To design an internal assistant best suited for Cisco’s global workforce, we developed a layered architecture around these components:
- AI agent, MCP, and enterprise search platform: The AI Agent and Model Context Protocol (MCP) platform hosts all the AI agents and MCP servers developed using open-source AI frameworks. Its modular, plug-and-play architecture gives the Enterprise AI/ML engineering team the ability to onboard new AI agents and search applications without operational overhead. The platform also provides LLM-as-a-service and RAG-as-a-service offering to over 4300+ teams across Cisco.
- Enterprise AI agent registry and MCP registry: This registry allows employees to register and connect all remote AI agents and remote MCP servers developed by teams across the enterprise with standardized agent and MCP security, agentic protocols and entitlements so that employees can securely access this connected agentic mesh from the internal assistant.
- Hybrid multi-cloud model and AI agent orchestration: Using a federated approach, our internal AI assistant connects to multiple Cisco AI agents and leading AI models such as Azure OpenAI, Claude, Google Gemini and Cisco’s internal large language model — Deep Network Model. The platform automatically routes each request to the best available AI model for deployments based on workload, latency, reliability, and use-case. This ensures users always get fast, accurate results.
- Built-in security, data governance, and observability: Security is woven into every layer of the tool, ensuring our workplace stays resilient against evolving threats while enabling innovation. Cisco’s AI Defense guardrails are used to scan user prompts and MCP server tools for malicious code and hidden or overlooked threats.
- Advanced data operations and AI-driven business impact: Domain specific AI agents have been developed to enable intelligent automation of business processes by leveraging AI ready enterprise data.
This platform, alongside our ongoing operating model, enables us to deploy new features and efficiently and consistently refine our roadmap — ensuring we stay at the forefront of AI innovation.
“Designed with a security-first mindset, our internal AI assistant has powerful guardrails that automatically detect and redact sensitive data before it’s sent to a public AI model — giving our employees an intelligent partner they can trust.” – Sujith Joseph, Principal Engineer, Cisco
Driving greater efficiency across our workforce
Since its launch, Cisco’s internal AI assistant has handled more than 45 million+ interactions, serving 100,000+ users across our global workforce.
Cisco’s internal AI assistant is more than just a chatbot. It has quickly become the most widely used AI tool at Cisco, facilitating an average of 156,000 daily interactions and driving greater efficiency as 73% of users reported increased productivity and an average time saved of 5 hours per week.
This is made possible by features and advancements currently available in the tool, including:
- Access to the latest AI models
- AI agents and LLM orchestration
- Data and image analysis
- PowerPoint generation
- Personal RAG (RAG on employee data stored in our corporate OneDrive environment)
- Unlimited Deep Research (Research reports using Cisco internal data and web data)
- Data analysis AI agent
- Enterprise AI Agent and Connector Registry (Integration of remote AI agents and MCP servers)
Lessons learned along the way
AI tools are only ever as reliable as the data they are trained on. One challenge we faced early on was ensuring that we were only ingesting clean, quality, and structured data into the tool. Anything less could really decrease the quality of the responses and the usefulness of the solution. The Dev Team conducted continual and rigorous testing to help ensure that the assistant does not hallucinate and consistently provides up to date and accurate responses.
Additionally, driving adoption across our global workforce presented challenges, especially among AI-cautious or non-technical employees. Despite the solution’s approval for highly confidential Cisco data, there was a level of apprehension surrounding its use and potential misuse. This spurred an effort to upskill our employees by creating effective demos, enablement resources, and increasing general AI awareness.
Our user-driven, design-led approach was crucial for navigating these challenges and allowed us to build a tool that caters to the needs of our diverse workforce. We continue to complete generative research to understand how our employees use the AI assistant and how it will resonate with them in their day-to-day work.
From product to platform
AI is transforming industries at an unprecedented rate. While most organizations recognize the urgent need to adopt AI technologies and tools, many are not fully prepared to effectively leverage AI. At Cisco, we know that AI is no longer a futuristic concept. We are continuously innovating internally — developing AI-powered tools, securing them, and ultimately empowering our employees to do their best work every day.
Building on its strong foundation, Cisco is focused on evolving the AI assistant from a product into a dynamic platform, empowering employees to have a hand in shaping their AI experience. The Agent Registry and upcoming Agent Builder features will enable users to tailor the tool to best fit their needs at work. Not only will this increase the overall usefulness and value of the AI assistant, but it will also help upskill our workforce, building a more technically proficient and AI-fluent employee population.
As a commitment to Cisco’s investment in AI, the Cisco Automation and AI Center was recently created to focus on expanding the adoption of AI. Looking ahead, the vision for the internal AI assistant is to become a reliable, always-on partner that can seamlessly integrate into every workflow, anticipate needs, and enable teams to focus on what matters most.
The internal AI assistant isn’t just changing how we work at Cisco; it’s a cornerstone of building a future-proofed workplace that is secure, adaptable, and ready for what’s next.
Additional resources:
Report: 77% of Employees Share Company Secrets on ChatGPT Compromising Enterprise Policies
