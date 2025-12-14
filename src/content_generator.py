"""
Content Generator Module with Improved Mock Responses
Handles all content generation using LLMs and RAG
"""

import json
import os
from typing import Dict, Any, Optional
from src.prompt_engine import PromptEngine

try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("OpenAI not available, using improved mock responses")


class ContentGenerator:
    """Main content generation system"""

    def __init__(self, api_key: Optional[str] = None, rag_system=None):
        self.api_key = api_key
        self.rag_system = rag_system
        self.prompt_engine = PromptEngine()

        # Initialize OpenAI client if available
        if OPENAI_AVAILABLE and api_key:
            self.client = OpenAI(api_key=api_key)
            self.use_mock = False
        else:
            self.client = None
            self.use_mock = True

        # Knowledge database for improved mock responses
        self.topic_knowledge = self._load_topic_knowledge()

    def _load_topic_knowledge(self):
        """Load topic-specific knowledge for better mock responses"""
        return {
            # Mathematics
            "pythagorean theorem": {
                "definition": "a² + b² = c², where c is the hypotenuse of a right triangle",
                "examples": [
                    "A right triangle with sides 3 and 4 has hypotenuse 5 (3² + 4² = 9 + 16 = 25 = 5²)",
                    "Finding the distance between two points on a coordinate plane uses the Pythagorean theorem"
                ],
                "applications": "construction, navigation, computer graphics, distance calculations",
                "key_points": [
                    "Only applies to right triangles",
                    "The hypotenuse is always the longest side",
                    "Used to find missing side lengths",
                    "Foundation for trigonometry and distance formula"
                ]
            },
            "quadratic equations": {
                "definition": "equations of the form ax² + bx + c = 0",
                "examples": [
                    "x² - 5x + 6 = 0 factors to (x-2)(x-3) = 0, so x = 2 or x = 3",
                    "Using the quadratic formula: x = (-b ± √(b²-4ac))/(2a)"
                ],
                "applications": "projectile motion, optimization problems, physics calculations",
                "key_points": [
                    "Can be solved by factoring, completing the square, or quadratic formula",
                    "The discriminant (b²-4ac) determines the nature of roots",
                    "Graph forms a parabola",
                    "Two solutions, one solution, or no real solutions possible"
                ]
            },
            "algebra": {
                "definition": "branch of mathematics using symbols to represent numbers and quantities",
                "examples": [
                    "Solving 2x + 5 = 15 gives x = 5",
                    "Expanding (x + 3)(x - 2) = x² + x - 6"
                ],
                "applications": "solving real-world problems, economics, engineering, computer science",
                "key_points": [
                    "Variables represent unknown quantities",
                    "Equations express relationships between quantities",
                    "Operations must maintain equality",
                    "Foundation for advanced mathematics"
                ]
            },

            # Science
            "photosynthesis": {
                "definition": "process by which plants convert light energy into chemical energy",
                "examples": [
                    "Plants use sunlight, water, and CO₂ to produce glucose and oxygen",
                    "Chlorophyll in leaves absorbs light energy, primarily red and blue wavelengths"
                ],
                "applications": "food production, oxygen generation, understanding plant biology, biofuels",
                "key_points": [
                    "Occurs in chloroplasts using chlorophyll",
                    "Light-dependent reactions produce ATP and NADPH",
                    "Calvin cycle converts CO₂ into glucose",
                    "Essential for most life on Earth"
                ]
            },
            "cell structure": {
                "definition": "organization of organelles and components within cells",
                "examples": [
                    "Mitochondria are the powerhouse of the cell, producing ATP",
                    "Plant cells have cell walls and chloroplasts; animal cells don't"
                ],
                "applications": "medicine, biotechnology, understanding diseases, drug development",
                "key_points": [
                    "Prokaryotic cells lack a nucleus",
                    "Eukaryotic cells have membrane-bound organelles",
                    "Each organelle has specific functions",
                    "Cell membrane controls what enters and exits"
                ]
            },
            "newton's laws": {
                "definition": "three fundamental laws describing motion and forces",
                "examples": [
                    "First Law: A hockey puck slides until friction stops it",
                    "Second Law: F = ma means heavier objects need more force to accelerate",
                    "Third Law: Rocket propulsion - exhaust pushes down, rocket goes up"
                ],
                "applications": "engineering, aerospace, vehicle design, sports science",
                "key_points": [
                    "First law: objects resist changes in motion (inertia)",
                    "Second law: force equals mass times acceleration",
                    "Third law: every action has equal and opposite reaction",
                    "Foundation of classical mechanics"
                ]
            },

            # History
            "world war ii": {
                "definition": "global war from 1939-1945 involving most of the world's nations",
                "examples": [
                    "Allied Powers (USA, UK, USSR) vs Axis Powers (Germany, Italy, Japan)",
                    "Major battles: D-Day (1944), Battle of Stalingrad (1942-43), Pearl Harbor (1941)"
                ],
                "applications": "understanding modern geopolitics, international relations, human rights",
                "key_points": [
                    "Began September 1, 1939 with German invasion of Poland",
                    "Holocaust resulted in death of 6 million Jews",
                    "Ended with atomic bombs on Hiroshima and Nagasaki",
                    "Led to formation of United Nations and Cold War"
                ]
            },
            "world war i": {
                "definition": "global conflict from 1914-1918, also called 'The Great War'",
                "examples": [
                    "Trench warfare on Western Front",
                    "New technologies: tanks, poison gas, airplanes"
                ],
                "applications": "understanding nationalism, modern warfare, peace treaties",
                "key_points": [
                    "Triggered by assassination of Archduke Franz Ferdinand",
                    "Alliance system pulled nations into war",
                    "Treaty of Versailles created conditions for WWII",
                    "First use of mechanized warfare"
                ]
            },

            # Computer Science
            "data structures": {
                "definition": "ways of organizing and storing data for efficient access and modification",
                "examples": [
                    "Arrays store elements in contiguous memory with O(1) access",
                    "Linked lists allow O(1) insertion/deletion at known positions"
                ],
                "applications": "databases, operating systems, compilers, graphics",
                "key_points": [
                    "Choice depends on use case and access patterns",
                    "Trade-offs between time and space complexity",
                    "Arrays: fast access, slow insertion",
                    "Linked lists: fast insertion, slow access"
                ]
            },
            "algorithms": {
                "definition": "step-by-step procedures for solving computational problems",
                "examples": [
                    "Binary search finds element in sorted array in O(log n) time",
                    "Quicksort sorts array in O(n log n) average time"
                ],
                "applications": "search engines, AI, data analysis, optimization",
                "key_points": [
                    "Efficiency measured by time and space complexity",
                    "Big O notation describes growth rate",
                    "Different algorithms suited for different problems",
                    "Often trade time for space or vice versa"
                ]
            }
        }

    def _get_topic_info(self, topic: str):
        """Get information for a specific topic"""
        topic_lower = topic.lower()

        # Exact match
        if topic_lower in self.topic_knowledge:
            return self.topic_knowledge[topic_lower]

        # Partial match
        for key in self.topic_knowledge:
            if key in topic_lower or topic_lower in key:
                return self.topic_knowledge[key]

        # Generic fallback
        return {
            "definition": f"fundamental concept in the field",
            "examples": [
                f"Basic application of {topic}",
                f"Advanced example involving {topic}"
            ],
            "applications": "various real-world scenarios",
            "key_points": [
                f"Understanding {topic} is essential",
                "Builds on prerequisite knowledge",
                "Has practical applications",
                "Connects to other concepts"
            ]
        }

    def _call_llm(self, system_prompt: str, user_prompt: str) -> str:
        """Call LLM API or return mock response"""
        if not self.use_mock and self.client:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7,
                    max_tokens=2000
                )
                return response.choices[0].message.content
            except Exception as e:
                print(f"API call failed: {e}, using mock response")
                return self._get_mock_response(user_prompt)
        else:
            return self._get_mock_response(user_prompt)

    def _get_mock_response(self, prompt: str) -> str:
        """Generate mock response for demo mode"""
        lines = prompt.split('\n')
        topic = "the topic"
        subject = "the subject"
        level = "High School"

        for line in lines:
            if line.startswith("Topic:"):
                topic = line.split(":", 1)[1].strip()
            elif line.startswith("Subject:"):
                subject = line.split(":", 1)[1].strip()
            elif line.startswith("Target Level:"):
                level = line.split(":", 1)[1].split("(")[0].strip()

        # Determine content type from prompt
        if "explanation" in prompt.lower():
            return self._mock_explanation(subject, topic, level)
        elif "quiz" in prompt.lower():
            return self._mock_quiz(subject, topic, level)
        elif "practice" in prompt.lower():
            return self._mock_practice(subject, topic, level)
        elif "study guide" in prompt.lower():
            return self._mock_study_guide(subject, topic, level)
        elif "flashcard" in prompt.lower():
            return self._mock_flashcards(subject, topic, level)

        return "{}"

    def _mock_explanation(self, subject: str, topic: str, level: str) -> str:
        """Generate topic-specific mock explanation"""
        info = self._get_topic_info(topic)

        response = {
            "type": "explanation",
            "subject": subject,
            "topic": topic,
            "level": level,
            "content": f"""## Understanding {topic.title()}

{topic.title()} is {info['definition']}. At the {level} level, it's important to grasp both the conceptual understanding and practical applications.

### Core Concept
{info['definition'].capitalize()}. This fundamental concept is essential in {subject} and serves as a building block for more advanced topics.

### How It Works
The key to understanding {topic} lies in breaking it down systematically:
1. First, identify the basic components and relationships
2. Understand the underlying principles that govern how it works
3. Learn to apply these principles to solve problems
4. Practice with varied examples to build proficiency

### Detailed Explanation
{topic.title()} has important applications in {info['applications']}. When working with this concept, it's crucial to remember the fundamental definition and how it applies in different contexts.

The systematic approach to {topic} ensures that you can tackle both simple and complex problems effectively. By understanding the core principles, you'll be able to extend your knowledge to related concepts and advanced applications.""",
            "examples": info['examples'],
            "key_points": info['key_points'],
            "misconceptions": [
                f"Common misconception: {topic} is too difficult to understand",
                "Reality: With proper explanation and practice, it becomes clear"
            ],
            "importance": f"Understanding {topic} is crucial because it {info['applications']} and forms the foundation for advanced study in {subject}."
        }
        return json.dumps(response, indent=2)

    def _mock_quiz(self, subject: str, topic: str, level: str) -> str:
        """Generate topic-specific mock quiz"""
        info = self._get_topic_info(topic)

        # Generate questions based on topic
        questions = [
            {
                "question": f"What is {topic}?",
                "type": "multiple_choice",
                "options": [
                    f"A) {info['definition']}",
                    "B) A completely unrelated concept",
                    "C) Only a theoretical idea with no applications",
                    "D) Something that contradicts established science"
                ],
                "answer": f"A) {info['definition']}",
                "explanation": f"{topic.title()} is defined as {info['definition']}. This is the fundamental definition you need to know."
            },
            {
                "question": f"Which of the following is a real-world application of {topic}?",
                "type": "multiple_choice",
                "options": [
                    f"A) {info['applications'].split(',')[0].strip()}",
                    "B) Making coffee",
                    "C) Watching television",
                    "D) None of the above"
                ],
                "answer": f"A) {info['applications'].split(',')[0].strip()}",
                "explanation": f"{topic.title()} is used in {info['applications']}."
            },
            {
                "question": f"True or False: {topic.title()} is an important concept in {subject}.",
                "type": "true_false",
                "options": ["True", "False"],
                "answer": "True",
                "explanation": f"{topic.title()} is indeed a fundamental concept in {subject} with numerous practical applications."
            }
        ]

        # Add key point questions
        for i, point in enumerate(info['key_points'][:2]):
            questions.append({
                "question": f"Which statement about {topic} is correct?",
                "type": "multiple_choice",
                "options": [
                    f"A) {point}",
                    "B) It has no practical use",
                    "C) It contradicts basic principles",
                    "D) It's only used in theory"
                ],
                "answer": f"A) {point}",
                "explanation": f"This is correct: {point}"
            })

        response = {
            "type": "quiz",
            "subject": subject,
            "topic": topic,
            "level": level,
            "questions": questions[:5]  # Limit to 5 questions
        }
        return json.dumps(response, indent=2)

    def _mock_practice(self, subject: str, topic: str, level: str) -> str:
        """Generate topic-specific practice problems"""
        info = self._get_topic_info(topic)

        problems = []

        # Create problems based on examples
        for i, example in enumerate(info['examples'][:3]):
            difficulty = ["easy", "medium", "hard"][min(i, 2)]
            problems.append({
                "question": f"Problem {i + 1}: Apply your knowledge of {topic} to this scenario: {example}",
                "difficulty": difficulty,
                "answer": f"The solution involves applying {info['definition']}",
                "solution": f"""Step 1: Identify what we know from the problem
Step 2: Recall that {topic} is {info['definition']}
Step 3: Apply this concept to the given scenario: {example}
Step 4: Work through the calculation or reasoning
Step 5: Verify the answer makes sense

Therefore, by applying {topic}, we can solve this problem effectively.""",
                "hints": [
                    f"Remember: {info['key_points'][0]}",
                    f"Consider how {topic} applies in this context"
                ]
            })

        response = {
            "type": "practice",
            "subject": subject,
            "topic": topic,
            "level": level,
            "problems": problems
        }
        return json.dumps(response, indent=2)

    def _mock_study_guide(self, subject: str, topic: str, level: str) -> str:
        """Generate topic-specific study guide"""
        info = self._get_topic_info(topic)

        content = f"""# Study Guide: {topic.title()}

## Overview
This study guide covers {topic} at the {level} level in {subject}.

## Key Definition
**{topic.title()}:** {info['definition']}

## Core Principles

### Main Concept
{info['definition'].capitalize()}

### Key Points to Remember
"""
        for i, point in enumerate(info['key_points'], 1):
            content += f"{i}. {point}\n"

        content += f"""
## Examples and Applications

### Real-World Applications
{topic.title()} is used in {info['applications']}.

### Examples
"""
        for i, example in enumerate(info['examples'], 1):
            content += f"**Example {i}:** {example}\n\n"

        content += f"""
## Study Tips
✓ Understand the definition thoroughly
✓ Practice with varied examples
✓ Connect {topic} to related concepts in {subject}
✓ Focus on real-world applications
✓ Review key points regularly

## Practice Questions
1. What is {topic}?
2. How is {topic} used in real-world scenarios?
3. What are the key principles of {topic}?
4. Can you explain {topic} to someone unfamiliar with it?

## Review Checklist
- [ ] Understand the core definition
- [ ] Can explain key principles
- [ ] Know real-world applications
- [ ] Can solve basic problems
- [ ] Understand connections to other topics
"""

        response = {
            "type": "study_guide",
            "subject": subject,
            "topic": topic,
            "level": level,
            "content": content
        }
        return json.dumps(response, indent=2)

    def _mock_flashcards(self, subject: str, topic: str, level: str) -> str:
        """Generate topic-specific flashcards"""
        info = self._get_topic_info(topic)

        cards = [
            {
                "front": f"What is {topic}?",
                "back": info['definition']
            }
        ]

        # Add key points as flashcards
        for point in info['key_points']:
            cards.append({
                "front": f"Key fact about {topic}",
                "back": point
            })

        # Add application card
        cards.append({
            "front": f"What are the applications of {topic}?",
            "back": info['applications']
        })

        response = {
            "type": "flashcards",
            "subject": subject,
            "topic": topic,
            "level": level,
            "cards": cards[:5]
        }
        return json.dumps(response, indent=2)

    def generate_explanation(self, subject: str, topic: str, level: str,
                             num_examples: int, learning_style: str, **kwargs) -> Dict[str, Any]:
        """Generate explanation content"""
        # Get context from RAG if available
        context = ""
        if self.rag_system:
            context = self.rag_system.get_context_for_query(topic, subject, level)

        # Build prompt
        system_prompt = self.prompt_engine.get_system_prompt('explanation')
        user_prompt = self.prompt_engine.build_explanation_prompt(
            subject, topic, level, num_examples, learning_style, context
        )

        # Call LLM
        response = self._call_llm(system_prompt, user_prompt)

        # Parse JSON response
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "type": "explanation",
                "subject": subject,
                "topic": topic,
                "level": level,
                "content": response,
                "examples": [],
                "key_points": []
            }

    def generate_quiz(self, subject: str, topic: str, level: str,
                      num_questions: int, **kwargs) -> Dict[str, Any]:
        """Generate quiz content"""
        context = ""
        if self.rag_system:
            context = self.rag_system.get_context_for_query(topic, subject, level)

        system_prompt = self.prompt_engine.get_system_prompt('quiz')
        user_prompt = self.prompt_engine.build_quiz_prompt(
            subject, topic, level, num_questions, kwargs.get('learning_style', 'Balanced'), context
        )

        response = self._call_llm(system_prompt, user_prompt)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "type": "quiz",
                "subject": subject,
                "topic": topic,
                "level": level,
                "questions": []
            }

    def generate_practice_problems(self, subject: str, topic: str, level: str,
                                   num_questions: int, **kwargs) -> Dict[str, Any]:
        """Generate practice problems"""
        context = ""
        if self.rag_system:
            context = self.rag_system.get_context_for_query(topic, subject, level)

        system_prompt = self.prompt_engine.get_system_prompt('practice')
        user_prompt = self.prompt_engine.build_practice_prompt(
            subject, topic, level, num_questions, kwargs.get('learning_style', 'Balanced'), context
        )

        response = self._call_llm(system_prompt, user_prompt)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "type": "practice",
                "subject": subject,
                "topic": topic,
                "level": level,
                "problems": []
            }

    def generate_study_guide(self, subject: str, topic: str, level: str, **kwargs) -> Dict[str, Any]:
        """Generate study guide"""
        context = ""
        if self.rag_system:
            context = self.rag_system.get_context_for_query(topic, subject, level)

        system_prompt = self.prompt_engine.get_system_prompt('study_guide')
        user_prompt = self.prompt_engine.build_study_guide_prompt(
            subject, topic, level, kwargs.get('learning_style', 'Balanced'), context
        )

        response = self._call_llm(system_prompt, user_prompt)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "type": "study_guide",
                "subject": subject,
                "topic": topic,
                "level": level,
                "content": response
            }

    def generate_flashcards(self, subject: str, topic: str, level: str,
                            num_questions: int, **kwargs) -> Dict[str, Any]:
        """Generate flashcards"""
        context = ""
        if self.rag_system:
            context = self.rag_system.get_context_for_query(topic, subject, level)

        system_prompt = self.prompt_engine.get_system_prompt('flashcards')
        user_prompt = self.prompt_engine.build_flashcards_prompt(
            subject, topic, level, num_questions, context
        )

        response = self._call_llm(system_prompt, user_prompt)

        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {
                "type": "flashcards",
                "subject": subject,
                "topic": topic,
                "level": level,
                "cards": []
            }