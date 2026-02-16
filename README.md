# PolicyGenerator-AI 📋

**AI-Powered Security Policy Generator**

Author: **Ayi NEDJIMI**
Website: [ayinedjimi-consultants.fr](https://ayinedjimi-consultants.fr)

## Features

- ISO27001, RGPD/GDPR, NIS2, SOC2 policy generation
- AI-powered content generation with GPT-4
- Export to Word (DOCX) and PDF
- Multi-language support (EN/FR)
- Customizable templates

## Usage

```python
from policygenerator_ai import PolicyGenerator, PolicyConfig

generator = PolicyGenerator()

config = PolicyConfig(
    framework="ISO27001",
    organization_name="My Company",
    industry="Finance",
    size="medium"
)

policy = generator.generate_policy(config)
generator.export_to_docx(policy, "policy.docx")
generator.export_to_pdf(policy, "policy.pdf")
```

## License

MIT - Copyright (c) 2024 Ayi NEDJIMI

---

Made with ❤️ by Ayi NEDJIMI | [ayinedjimi-consultants.fr](https://ayinedjimi-consultants.fr)
