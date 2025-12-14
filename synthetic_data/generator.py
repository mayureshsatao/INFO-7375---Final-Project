from typing import List, Dict
import random
import json
from langchain_community.llms import Ollama
import sys

sys.path.append('..')
from models.local_llm import PromptTemplates


class SyntheticDataGenerator:
    """Generate synthetic documentation data for training and testing"""

    def __init__(self, model_name: str = "mistral"):
        self.llm = Ollama(model=model_name, temperature=0.8)
        self.templates = PromptTemplates()

    def generate_api_docs(self, count: int = 5) -> List[Dict]:
        """Generate synthetic API documentation examples"""
        api_types = ['REST', 'GraphQL', 'gRPC', 'WebSocket', 'SOAP']
        methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']

        examples = []
        for i in range(count):
            api_type = random.choice(api_types)
            method = random.choice(methods)

            prompt = f"""Generate a realistic API documentation example for a {api_type} API endpoint.

Include:
1. Endpoint URL and method
2. Description and purpose
3. Request parameters and body
4. Response format and status codes
5. Example request/response
6. Authentication requirements
7. Error handling

Make it realistic and detailed. Format in markdown."""

            result = self.llm.invoke(prompt)
            examples.append({
                'type': 'api_documentation',
                'api_type': api_type,
                'content': result
            })

        return examples

    def generate_user_guides(self, count: int = 5) -> List[Dict]:
        """Generate synthetic user guide examples"""
        topics = [
            'Getting Started Guide',
            'Installation Instructions',
            'Configuration Guide',
            'Troubleshooting Guide',
            'Best Practices Guide'
        ]

        examples = []
        for topic in random.sample(topics, min(count, len(topics))):
            prompt = f"""Create a comprehensive user guide for: {topic}

Include:
1. Introduction and overview
2. Prerequisites
3. Step-by-step instructions
4. Screenshots or diagram descriptions
5. Common issues and solutions
6. Next steps

Make it beginner-friendly and detailed. Format in markdown."""

            result = self.llm.invoke(prompt)
            examples.append({
                'type': 'user_guide',
                'topic': topic,
                'content': result
            })

        return examples

    def generate_code_documentation(self, count: int = 5) -> List[Dict]:
        """Generate synthetic code documentation examples"""
        languages = ['Python', 'JavaScript', 'Java', 'Go', 'Rust']
        concepts = [
            'Class design pattern',
            'Function with error handling',
            'Async/await implementation',
            'Data structure implementation',
            'API client wrapper'
        ]

        examples = []
        for i in range(count):
            lang = random.choice(languages)
            concept = random.choice(concepts)

            prompt = f"""Generate well-documented {lang} code for: {concept}

Include:
1. Complete, working code
2. Detailed docstrings/comments
3. Type hints (if applicable)
4. Usage examples
5. Error handling
6. Best practices

Make it production-ready quality."""

            result = self.llm.invoke(prompt)
            examples.append({
                'type': 'code_documentation',
                'language': lang,
                'concept': concept,
                'content': result
            })

        return examples

    def generate_readme_files(self, count: int = 5) -> List[Dict]:
        """Generate synthetic README files"""
        project_types = [
            'Web application',
            'CLI tool',
            'Library/Package',
            'Mobile app',
            'Desktop application'
        ]

        examples = []
        for ptype in random.sample(project_types, min(count, len(project_types))):
            prompt = f"""Create a comprehensive README.md for a {ptype} project.

Include:
1. Project title and description
2. Features list
3. Installation instructions
4. Usage examples
5. Configuration options
6. Contributing guidelines
7. License information
8. Contact/support info

Make it professional and complete. Format in markdown."""

            result = self.llm.invoke(prompt)
            examples.append({
                'type': 'readme',
                'project_type': ptype,
                'content': result
            })

        return examples

    def augment_existing_docs(self, original_doc: str, variations: int = 3) -> List[str]:
        """Create variations of existing documentation"""
        augmented = []

        styles = ['more technical', 'more beginner-friendly', 'more concise']

        for style in styles[:variations]:
            prompt = f"""Rewrite the following documentation in a {style} style while maintaining accuracy:

{original_doc}

Keep the same information but adjust the tone, detail level, and explanation style."""

            result = self.llm.invoke(prompt)
            augmented.append(result)

        return augmented

    def generate_qa_pairs(self, documentation: str, count: int = 10) -> List[Dict]:
        """Generate Q&A pairs from documentation for testing"""
        prompt = f"""Based on this documentation, generate {count} realistic question-answer pairs that users might ask.

Documentation:
{documentation}

Format as JSON array with 'question' and 'answer' keys. Make questions varied and realistic."""

        result = self.llm.invoke(prompt)

        try:
            qa_pairs = json.loads(result)
            return qa_pairs
        except:
            return []

    def validate_quality(self, synthetic_data: List[Dict]) -> Dict:
        """Validate quality of synthetic data"""
        stats = {
            'total': len(synthetic_data),
            'avg_length': 0,
            'types': {},
            'quality_score': 0
        }

        total_length = 0
        quality_scores = []

        for item in synthetic_data:
            content = item.get('content', '')
            total_length += len(content)

            item_type = item.get('type', 'unknown')
            stats['types'][item_type] = stats['types'].get(item_type, 0) + 1

            score = self._assess_quality(content)
            quality_scores.append(score)

        stats['avg_length'] = total_length / len(synthetic_data) if synthetic_data else 0
        stats['quality_score'] = sum(quality_scores) / len(quality_scores) if quality_scores else 0

        return stats

    def _assess_quality(self, content: str) -> float:
        """Simple quality assessment"""
        score = 0.5

        if len(content) > 500:
            score += 0.1
        if len(content) > 1000:
            score += 0.1

        if '```' in content:
            score += 0.1

        if any(word in content.lower() for word in ['example', 'usage', 'note', 'warning']):
            score += 0.1

        if content.count('\n') > 10:
            score += 0.1

        return min(score, 1.0)

    def export_dataset(self, data: List[Dict], filename: str):
        """Export synthetic dataset to JSON"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

        return filename