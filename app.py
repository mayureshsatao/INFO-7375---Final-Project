# import streamlit as st
# from typing import List, Dict
# import requests
# import json
# import random
# from collections import defaultdict
# import matplotlib
#
# matplotlib.use('Agg')  # Use non-interactive backend
# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import numpy as np
# from io import BytesIO
# import base64
#
#
# # ============================================================================
# # DIAGRAM GENERATOR
# # ============================================================================
#
# class DiagramGenerator:
#     """Generate educational diagrams for technical topics"""
#
#     def __init__(self):
#         pass
#
#     def generate_architecture_diagram(self, title: str = "System Architecture"):
#         """Generate a system architecture diagram"""
#         fig, ax = plt.subplots(figsize=(12, 8))
#
#         # Frontend
#         frontend = patches.FancyBboxPatch((1, 6), 3, 1.5,
#                                           boxstyle="round,pad=0.1",
#                                           fill=True, facecolor='lightblue',
#                                           edgecolor='blue', linewidth=2)
#         ax.add_patch(frontend)
#         ax.text(2.5, 6.75, 'Frontend\n(UI Layer)', ha='center', va='center',
#                 fontsize=12, fontweight='bold')
#
#         # API Gateway
#         api = patches.FancyBboxPatch((5.5, 6), 3, 1.5,
#                                      boxstyle="round,pad=0.1",
#                                      fill=True, facecolor='lightgreen',
#                                      edgecolor='green', linewidth=2)
#         ax.add_patch(api)
#         ax.text(7, 6.75, 'API Gateway\n(Routing)', ha='center', va='center',
#                 fontsize=12, fontweight='bold')
#
#         # Backend Services
#         services = [
#             (1.5, 3.5, 'Auth\nService'),
#             (4.5, 3.5, 'Business\nLogic'),
#             (7.5, 3.5, 'Data\nService'),
#         ]
#
#         for x, y, label in services:
#             service_box = patches.FancyBboxPatch((x - 0.8, y - 0.5), 1.6, 1,
#                                                  boxstyle="round,pad=0.1",
#                                                  fill=True, facecolor='lightyellow',
#                                                  edgecolor='orange', linewidth=2)
#             ax.add_patch(service_box)
#             ax.text(x, y, label, ha='center', va='center',
#                     fontsize=10, fontweight='bold')
#
#         # Database
#         db = patches.FancyBboxPatch((4, 1), 4, 1,
#                                     boxstyle="round,pad=0.1",
#                                     fill=True, facecolor='lightcoral',
#                                     edgecolor='red', linewidth=2)
#         ax.add_patch(db)
#         ax.text(6, 1.5, 'Database Layer', ha='center', va='center',
#                 fontsize=12, fontweight='bold')
#
#         # Arrows
#         # Frontend to API
#         ax.annotate('', xy=(5.5, 6.75), xytext=(4, 6.75),
#                     arrowprops=dict(arrowstyle='->', lw=2, color='black'))
#
#         # API to Services
#         for x, y in [(2.3, 4.5), (5.3, 4.5), (8.3, 4.5)]:
#             ax.annotate('', xy=(x, y), xytext=(7, 6),
#                         arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))
#
#         # Services to DB
#         for x in [2.3, 5.3, 8.3]:
#             ax.annotate('', xy=(6, 2), xytext=(x, 3.5),
#                         arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'))
#
#         ax.set_xlim(0, 10)
#         ax.set_ylim(0, 8.5)
#         ax.axis('off')
#         ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
#
#         return self._fig_to_base64(fig)
#
#     def generate_api_flow_diagram(self):
#         """Generate API request/response flow"""
#         fig, ax = plt.subplots(figsize=(12, 8))
#
#         # Client
#         client = patches.FancyBboxPatch((1, 6), 2, 1,
#                                         boxstyle="round,pad=0.1",
#                                         fill=True, facecolor='lightblue',
#                                         edgecolor='blue', linewidth=2)
#         ax.add_patch(client)
#         ax.text(2, 6.5, 'Client', ha='center', va='center',
#                 fontsize=12, fontweight='bold')
#
#         # Server
#         server = patches.FancyBboxPatch((7, 6), 2, 1,
#                                         boxstyle="round,pad=0.1",
#                                         fill=True, facecolor='lightgreen',
#                                         edgecolor='green', linewidth=2)
#         ax.add_patch(server)
#         ax.text(8, 6.5, 'Server', ha='center', va='center',
#                 fontsize=12, fontweight='bold')
#
#         # Flow steps
#         steps = [
#             (5, 5, '1. HTTP Request\nGET /api/data', 'blue'),
#             (5, 4, '2. Authentication', 'orange'),
#             (5, 3, '3. Process Request', 'purple'),
#             (5, 2, '4. Query Database', 'red'),
#             (5, 1, '5. HTTP Response\n200 OK + Data', 'green'),
#         ]
#
#         for x, y, label, color in steps:
#             ax.text(x, y, label, ha='center', va='center',
#                     fontsize=10,
#                     bbox=dict(boxstyle='round', facecolor=color, alpha=0.3))
#
#         # Arrows
#         ax.annotate('', xy=(7, 6.3), xytext=(3, 6.3),
#                     arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
#         ax.text(5, 5.8, 'Request →', ha='center', fontsize=9)
#
#         ax.annotate('', xy=(3, 6.7), xytext=(7, 6.7),
#                     arrowprops=dict(arrowstyle='->', lw=2, color='green'))
#         ax.text(5, 7.2, '← Response', ha='center', fontsize=9)
#
#         ax.set_xlim(0, 10)
#         ax.set_ylim(0, 8)
#         ax.axis('off')
#         ax.set_title('API Request/Response Flow', fontsize=16, fontweight='bold')
#
#         return self._fig_to_base64(fig)
#
#     def generate_data_structure_diagram(self, structure_type: str = "array"):
#         """Generate data structure visualization"""
#         fig, ax = plt.subplots(figsize=(12, 6))
#
#         if structure_type.lower() == "array":
#             # Array visualization
#             for i in range(6):
#                 rect = patches.Rectangle((i * 1.5 + 2, 3), 1.2, 1,
#                                          fill=True, facecolor='lightblue',
#                                          edgecolor='black', linewidth=2)
#                 ax.add_patch(rect)
#                 ax.text(i * 1.5 + 2.6, 3.5, str(i * 10), fontsize=14, ha='center')
#                 ax.text(i * 1.5 + 2.6, 2.5, f'[{i}]', fontsize=10, ha='center')
#
#             ax.text(6, 5, 'Array: Contiguous Memory', fontsize=14,
#                     ha='center', fontweight='bold')
#             ax.text(6, 1.5, 'O(1) Access • O(n) Insert/Delete',
#                     fontsize=12, ha='center')
#
#         elif structure_type.lower() == "linked list":
#             # Linked list visualization
#             for i in range(5):
#                 circle = patches.Circle((i * 2.5 + 2, 3.5), 0.5,
#                                         fill=True, facecolor='lightgreen',
#                                         edgecolor='black', linewidth=2)
#                 ax.add_patch(circle)
#                 ax.text(i * 2.5 + 2, 3.5, str(i * 10), fontsize=12, ha='center')
#
#                 if i < 4:
#                     ax.arrow(i * 2.5 + 2.6, 3.5, 1.7, 0,
#                              head_width=0.2, head_length=0.2,
#                              fc='black', ec='black')
#
#             ax.text(6, 5, 'Linked List: Dynamic Memory', fontsize=14,
#                     ha='center', fontweight='bold')
#             ax.text(6, 1.5, 'O(n) Access • O(1) Insert/Delete',
#                     fontsize=12, ha='center')
#
#         ax.set_xlim(0, 12)
#         ax.set_ylim(0, 6)
#         ax.axis('off')
#         ax.set_title(f'{structure_type.title()} Structure',
#                      fontsize=16, fontweight='bold')
#
#         return self._fig_to_base64(fig)
#
#     def generate_workflow_diagram(self, steps: List[str]):
#         """Generate a workflow/process diagram"""
#         fig, ax = plt.subplots(figsize=(10, len(steps) * 1.5 + 2))
#
#         y_start = len(steps)
#
#         for i, step in enumerate(steps):
#             y = y_start - i * 1.5
#
#             # Step box
#             box = patches.FancyBboxPatch((2, y - 0.4), 6, 0.8,
#                                          boxstyle="round,pad=0.1",
#                                          fill=True,
#                                          facecolor='lightblue' if i % 2 == 0 else 'lightgreen',
#                                          edgecolor='black', linewidth=2)
#             ax.add_patch(box)
#             ax.text(5, y, f'{i + 1}. {step}', ha='center', va='center',
#                     fontsize=11, fontweight='bold')
#
#             # Arrow to next step
#             if i < len(steps) - 1:
#                 ax.annotate('', xy=(5, y - 0.6), xytext=(5, y - 0.9),
#                             arrowprops=dict(arrowstyle='->', lw=2, color='black'))
#
#         ax.set_xlim(0, 10)
#         ax.set_ylim(-1, len(steps) + 1)
#         ax.axis('off')
#         ax.set_title('Process Workflow', fontsize=16, fontweight='bold', pad=20)
#
#         return self._fig_to_base64(fig)
#
#     def generate_comparison_diagram(self, items: List[Dict]):
#         """Generate a comparison diagram"""
#         fig, ax = plt.subplots(figsize=(12, 8))
#
#         n_items = len(items)
#         width = 8 / n_items
#
#         for i, item in enumerate(items):
#             x = i * (width + 0.5) + 1
#
#             # Box
#             box = patches.FancyBboxPatch((x, 2), width, 5,
#                                          boxstyle="round,pad=0.1",
#                                          fill=True, facecolor='lightblue',
#                                          edgecolor='blue', linewidth=2)
#             ax.add_patch(box)
#
#             # Title
#             ax.text(x + width / 2, 6.5, item['name'],
#                     ha='center', va='top',
#                     fontsize=12, fontweight='bold')
#
#             # Features
#             y_pos = 5.5
#             for feature in item.get('features', []):
#                 ax.text(x + width / 2, y_pos, f'• {feature}',
#                         ha='center', va='top', fontsize=9)
#                 y_pos -= 0.5
#
#         ax.set_xlim(0, 10)
#         ax.set_ylim(0, 8)
#         ax.axis('off')
#         ax.set_title('Feature Comparison', fontsize=16, fontweight='bold', pad=20)
#
#         return self._fig_to_base64(fig)
#
#     def _fig_to_base64(self, fig):
#         """Convert matplotlib figure to base64 string"""
#         buf = BytesIO()
#         fig.savefig(buf, format='png', bbox_inches='tight', dpi=100)
#         buf.seek(0)
#         img_base64 = base64.b64encode(buf.read()).decode('utf-8')
#         plt.close(fig)
#         return img_base64
#
#
# # ============================================================================
# # OLLAMA API
# # ============================================================================
#
# def get_available_models() -> List[str]:
#     try:
#         response = requests.get('http://localhost:11434/api/tags', timeout=2)
#         if response.status_code == 200:
#             models = response.json().get('models', [])
#             return [m['name'] for m in models]
#     except:
#         pass
#     return []
#
#
# def generate_with_ollama(prompt: str, model: str = "mistral", system: str = "") -> str:
#     try:
#         if len(prompt) > 500:
#             prompt = prompt[:500] + "... (shortened for speed)"
#
#         payload = {
#             'model': model,
#             'prompt': prompt,
#             'stream': False,
#             'options': {
#                 'temperature': 0.7,
#                 'num_predict': 500,
#                 'num_ctx': 2048
#             }
#         }
#         if system:
#             payload['system'] = system
#
#         response = requests.post(
#             'http://localhost:11434/api/generate',
#             json=payload,
#             timeout=180
#         )
#         if response.status_code == 200:
#             return response.json().get('response', '')
#     except requests.exceptions.Timeout:
#         return "⚠️ Generation timed out. Try a shorter prompt or simpler topic."
#     except Exception as e:
#         return f"Error: {str(e)}"
#     return ""
#
#
# def generate_embedding(text: str, model: str = "mistral") -> List[float]:
#     """Generate embeddings using Ollama"""
#     try:
#         response = requests.post(
#             'http://localhost:11434/api/embeddings',
#             json={'model': model, 'prompt': text},
#             timeout=30
#         )
#         if response.status_code == 200:
#             return response.json().get('embedding', [])
#     except:
#         pass
#     return []
#
#
# # ============================================================================
# # SIMPLE VECTOR STORE (No ChromaDB - Pure Python)
# # ============================================================================
#
# class SimpleVectorStore:
#     """Simple in-memory vector store - RAG implementation"""
#
#     def __init__(self):
#         self.documents = []
#         self.embeddings = []
#         self.metadata = []
#
#     def add_documents(self, docs: List[str], meta: List[Dict] = None, model: str = "mistral") -> int:
#         """Add documents with embeddings"""
#         count = 0
#         for i, doc in enumerate(docs):
#             chunks = self._chunk_text(doc)
#             for j, chunk in enumerate(chunks):
#                 embedding = generate_embedding(chunk, model)
#                 if embedding:
#                     self.documents.append(chunk)
#                     self.embeddings.append(embedding)
#                     doc_meta = {'doc_id': i, 'chunk_id': j}
#                     if meta and i < len(meta):
#                         doc_meta.update(meta[i])
#                     self.metadata.append(doc_meta)
#                     count += 1
#         return count
#
#     def search(self, query: str, n_results: int = 5, model: str = "mistral") -> List[tuple]:
#         """Search with cosine similarity"""
#         if not self.embeddings:
#             return []
#
#         query_embedding = generate_embedding(query, model)
#         if not query_embedding:
#             return []
#
#         similarities = []
#         for i, doc_embedding in enumerate(self.embeddings):
#             sim = self._cosine_similarity(query_embedding, doc_embedding)
#             similarities.append((sim, i))
#
#         similarities.sort(reverse=True)
#
#         results = []
#         for sim, idx in similarities[:n_results]:
#             results.append((self.documents[idx], sim, self.metadata[idx]))
#
#         return results
#
#     def _chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
#         """Simple chunking"""
#         paragraphs = text.split('\n\n')
#         chunks = []
#         current = []
#         current_size = 0
#
#         for para in paragraphs:
#             if current_size + len(para) > chunk_size and current:
#                 chunks.append('\n\n'.join(current))
#                 current = []
#                 current_size = 0
#             current.append(para)
#             current_size += len(para)
#
#         if current:
#             chunks.append('\n\n'.join(current))
#
#         return chunks
#
#     def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
#         """Calculate cosine similarity"""
#         if len(a) != len(b):
#             return 0.0
#
#         dot = sum(x * y for x, y in zip(a, b))
#         norm_a = sum(x * x for x in a) ** 0.5
#         norm_b = sum(x * x for x in b) ** 0.5
#
#         if norm_a == 0 or norm_b == 0:
#             return 0.0
#
#         return dot / (norm_a * norm_b)
#
#     def get_context(self, query: str, n: int = 3, model: str = "mistral") -> str:
#         results = self.search(query, n, model)
#         context = []
#         for i, (doc, score, meta) in enumerate(results, 1):
#             context.append(f"[Source {i}] (Relevance: {score:.1%})")
#             context.append(doc)
#             context.append("")
#         return '\n'.join(context)
#
#     def clear(self):
#         self.documents = []
#         self.embeddings = []
#         self.metadata = []
#
#     def stats(self) -> Dict:
#         return {'total_chunks': len(self.documents)}
#
#
# # ============================================================================
# # PROMPT ENGINEERING
# # ============================================================================
#
# class PromptTemplates:
#     """Systematic prompt templates - Requirement 1"""
#
#     @staticmethod
#     def research_prompt(topic: str, context: str = "") -> str:
#         return f"""Research: {topic}
# {f'Context: {context}' if context else ''}
# Provide: key concepts, technical details, examples. Be concise."""
#
#     @staticmethod
#     def documentation_prompt(topic: str, research: str = "") -> str:
#         return f"""Create documentation for: {topic}
# {f'Based on: {research[:200]}' if research else ''}
# Include: overview, explanation, code example, usage. Be concise."""
#
#     @staticmethod
#     def code_prompt(concept: str, language: str = "python") -> str:
#         return f"""Write working {language} code for: {concept}
# Include comments and example. Keep it simple and short."""
#
#     @staticmethod
#     def review_prompt(content: str) -> str:
#         return f"""Review briefly: {content[:300]}
# List 3 improvements."""
#
#
# # ============================================================================
# # DOCUMENTATION AGENT
# # ============================================================================
#
# class DocumentationAgent:
#     """Multi-step documentation generation"""
#
#     def __init__(self, model: str = "mistral"):
#         self.model = model
#         self.templates = PromptTemplates()
#
#     def create_documentation(self, topic: str, context: str = "", include_code: bool = True) -> str:
#         # Step 1: Research
#         research = generate_with_ollama(
#             self.templates.research_prompt(topic, context),
#             self.model,
#             "You are a technical researcher"
#         )
#
#         # Step 2: Write
#         doc = generate_with_ollama(
#             self.templates.documentation_prompt(topic, research),
#             self.model,
#             "You are a technical writer"
#         )
#
#         # Step 3: Add code
#         if include_code:
#             code = generate_with_ollama(
#                 self.templates.code_prompt(topic),
#                 self.model,
#                 "You are a code expert"
#             )
#             doc += f"\n\n## Code Example\n\n```python\n{code}\n```"
#
#         return doc
#
#     def generate_code(self, concept: str, languages: List[str]) -> Dict[str, str]:
#         examples = {}
#         for lang in languages:
#             code = generate_with_ollama(
#                 self.templates.code_prompt(concept, lang),
#                 self.model,
#                 f"You are a {lang} expert"
#             )
#             examples[lang] = code
#         return examples
#
#
# # ============================================================================
# # SYNTHETIC DATA GENERATOR
# # ============================================================================
#
# class SyntheticGenerator:
#     """Generate synthetic documentation - Requirement 4"""
#
#     def __init__(self, model: str = "mistral"):
#         self.model = model
#
#     def generate_api_docs(self, count: int = 3) -> List[Dict]:
#         types = ['REST', 'GraphQL', 'gRPC']
#         examples = []
#
#         for _ in range(count):
#             api_type = random.choice(types)
#             prompt = f"""Generate realistic {api_type} API documentation with endpoints, parameters, examples. Markdown format."""
#             result = generate_with_ollama(prompt, self.model)
#             examples.append({'type': 'api', 'api_type': api_type, 'content': result})
#
#         return examples
#
#     def generate_tutorials(self, count: int = 3) -> List[Dict]:
#         topics = ['Getting Started', 'Installation', 'Configuration']
#         examples = []
#
#         for topic in random.sample(topics, min(count, len(topics))):
#             prompt = f"""Create tutorial: {topic}. Include intro, steps, examples, troubleshooting. Markdown."""
#             result = generate_with_ollama(prompt, self.model)
#             examples.append({'type': 'tutorial', 'topic': topic, 'content': result})
#
#         return examples
#
#
# # ============================================================================
# # STREAMLIT UI
# # ============================================================================
#
# st.set_page_config(page_title="Tech Doc Assistant", page_icon="📚", layout="wide")
#
#
# def init():
#     if 'vector_store' not in st.session_state:
#         st.session_state.vector_store = SimpleVectorStore()
#     if 'agent' not in st.session_state:
#         st.session_state.agent = None
#     if 'synth' not in st.session_state:
#         st.session_state.synth = None
#     if 'ready' not in st.session_state:
#         st.session_state.ready = False
#     if 'model' not in st.session_state:
#         st.session_state.model = "mistral"
#     if 'diagram_gen' not in st.session_state:
#         st.session_state.diagram_gen = DiagramGenerator()
#
#
# def sidebar():
#     st.sidebar.title("⚙️ Settings")
#
#     models = get_available_models()
#
#     if not models:
#         st.sidebar.error("❌ Ollama not running!")
#         st.sidebar.code("ollama serve\nollama pull mistral")
#         return
#
#     model = st.sidebar.selectbox("Model", models)
#     st.session_state.model = model
#
#     if st.sidebar.button("🚀 Initialize", type="primary"):
#         with st.spinner("Initializing..."):
#             st.session_state.agent = DocumentationAgent(model)
#             st.session_state.synth = SyntheticGenerator(model)
#             st.session_state.ready = True
#             st.sidebar.success("✅ Ready!")
#
#     if st.session_state.ready:
#         stats = st.session_state.vector_store.stats()
#         st.sidebar.metric("KB Chunks", stats['total_chunks'])
#
#     st.sidebar.markdown("---")
#     st.sidebar.markdown("""
#     ### ✅ Requirements Met
#     - ✅ Prompt Engineering
#     - ✅ RAG (Vector Store)
#     - ✅ Multimodal (Text+Code+Diagrams)
#     - ✅ Synthetic Data
#     """)
#
#
# def tab_generate():
#     st.header("📝 Generate Documentation")
#
#     if not st.session_state.ready:
#         st.warning("⚠️ Click Initialize in sidebar first!")
#         return
#
#     topic = st.text_input("Topic", placeholder="e.g., JWT Authentication")
#     context = st.text_area("Additional Context", height=100)
#
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         include_code = st.checkbox("Include Code Examples", value=True)
#     with col2:
#         use_rag = st.checkbox("Use Knowledge Base")
#     with col3:
#         include_diagram = st.checkbox("Include Diagram", value=True)
#
#     if st.button("✨ Generate Documentation", disabled=not topic):
#         with st.spinner("Generating... (this may take 30-60 seconds)"):
#             try:
#                 full_context = context
#                 if use_rag:
#                     rag_context = st.session_state.vector_store.get_context(
#                         topic, 3, st.session_state.model
#                     )
#                     full_context = f"{context}\n\n{rag_context}"
#
#                 doc = st.session_state.agent.create_documentation(
#                     topic, full_context, include_code
#                 )
#
#                 st.success("✅ Documentation generated!")
#
#                 # Show diagram first if requested
#                 if include_diagram:
#                     st.markdown("### 📊 Architecture Diagram")
#                     diagram_base64 = st.session_state.diagram_gen.generate_architecture_diagram(topic)
#                     st.markdown(f'<img src="data:image/png;base64,{diagram_base64}" style="max-width:100%;"/>',
#                                 unsafe_allow_html=True)
#                     st.markdown("---")
#
#                 # Show documentation
#                 st.markdown(doc)
#
#                 st.download_button("📥 Download", doc, f"{topic.replace(' ', '_')}.md")
#             except Exception as e:
#                 st.error(f"Error: {e}")
#
#
# def tab_diagrams():
#     """New tab for diagram generation"""
#     st.header("📊 Diagram Generator")
#
#     if not st.session_state.ready:
#         st.warning("⚠️ Initialize system first!")
#         return
#
#     diagram_type = st.selectbox(
#         "Diagram Type",
#         ["System Architecture", "API Flow", "Data Structure", "Process Workflow", "Comparison"]
#     )
#
#     if diagram_type == "System Architecture":
#         title = st.text_input("System Name", "My System Architecture")
#         if st.button("Generate Architecture Diagram"):
#             with st.spinner("Creating diagram..."):
#                 diagram = st.session_state.diagram_gen.generate_architecture_diagram(title)
#                 st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
#                             unsafe_allow_html=True)
#
#     elif diagram_type == "API Flow":
#         if st.button("Generate API Flow Diagram"):
#             with st.spinner("Creating diagram..."):
#                 diagram = st.session_state.diagram_gen.generate_api_flow_diagram()
#                 st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
#                             unsafe_allow_html=True)
#
#     elif diagram_type == "Data Structure":
#         structure = st.selectbox("Structure Type", ["Array", "Linked List"])
#         if st.button("Generate Data Structure Diagram"):
#             with st.spinner("Creating diagram..."):
#                 diagram = st.session_state.diagram_gen.generate_data_structure_diagram(structure)
#                 st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
#                             unsafe_allow_html=True)
#
#     elif diagram_type == "Process Workflow":
#         st.markdown("Enter workflow steps (one per line):")
#         steps_text = st.text_area("Steps",
#                                   "Initialize System\nProcess Request\nValidate Data\nExecute Logic\nReturn Response")
#         if st.button("Generate Workflow Diagram"):
#             steps = [s.strip() for s in steps_text.split('\n') if s.strip()]
#             with st.spinner("Creating diagram..."):
#                 diagram = st.session_state.diagram_gen.generate_workflow_diagram(steps)
#                 st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
#                             unsafe_allow_html=True)
#
#     elif diagram_type == "Comparison":
#         st.markdown("Compare different options:")
#         col1, col2 = st.columns(2)
#         with col1:
#             item1_name = st.text_input("Item 1 Name", "Option A")
#             item1_features = st.text_area("Item 1 Features (one per line)", "Fast\nScalable\nCheap")
#         with col2:
#             item2_name = st.text_input("Item 2 Name", "Option B")
#             item2_features = st.text_area("Item 2 Features (one per line)", "Secure\nReliable\nEasy to use")
#
#         if st.button("Generate Comparison Diagram"):
#             items = [
#                 {
#                     'name': item1_name,
#                     'features': [f.strip() for f in item1_features.split('\n') if f.strip()]
#                 },
#                 {
#                     'name': item2_name,
#                     'features': [f.strip() for f in item2_features.split('\n') if f.strip()]
#                 }
#             ]
#             with st.spinner("Creating diagram..."):
#                 diagram = st.session_state.diagram_gen.generate_comparison_diagram(items)
#                 st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
#                             unsafe_allow_html=True)
#
#
# def tab_kb():
#     st.header("📚 Knowledge Base (RAG)")
#
#     tab1, tab2 = st.tabs(["Upload", "Search"])
#
#     with tab1:
#         st.subheader("Add Documents")
#         files = st.file_uploader("Upload", type=['txt', 'md'], accept_multiple_files=True)
#
#         if files and st.button("Add to Knowledge Base"):
#             with st.spinner("Processing..."):
#                 docs = []
#                 meta = []
#                 for f in files:
#                     content = f.read().decode('utf-8')
#                     docs.append(content)
#                     meta.append({'filename': f.name})
#
#                 chunks = st.session_state.vector_store.add_documents(
#                     docs, meta, st.session_state.model
#                 )
#                 st.success(f"✅ Added {chunks} chunks")
#
#     with tab2:
#         st.subheader("Search Knowledge Base")
#         query = st.text_input("Search Query")
#
#         if query and st.button("🔍 Search"):
#             with st.spinner("Searching..."):
#                 results = st.session_state.vector_store.search(
#                     query, 5, st.session_state.model
#                 )
#
#                 if results:
#                     for i, (doc, score, meta) in enumerate(results, 1):
#                         with st.expander(f"Result {i} - Relevance: {score:.1%}"):
#                             st.markdown(f"**File:** {meta.get('filename', 'Unknown')}")
#                             st.markdown(doc)
#                 else:
#                     st.info("No results found")
#
#
# def tab_code():
#     st.header("💻 Code Examples Generator")
#
#     if not st.session_state.ready:
#         st.warning("⚠️ Initialize system first!")
#         return
#
#     concept = st.text_input("Programming Concept", placeholder="e.g., Binary Search Tree")
#     langs = st.multiselect(
#         "Languages",
#         ["Python", "JavaScript", "Java", "Go", "Rust"],
#         ["Python"]
#     )
#
#     if st.button("Generate Code", disabled=not concept or not langs):
#         with st.spinner("Generating code examples..."):
#             try:
#                 examples = st.session_state.agent.generate_code(concept, langs)
#
#                 for lang, code in examples.items():
#                     st.subheader(f"{lang} Implementation")
#                     st.code(code, language=lang.lower())
#             except Exception as e:
#                 st.error(f"Error: {e}")
#
#
# def tab_synthetic():
#     st.header("🔄 Synthetic Data Generation")
#
#     if not st.session_state.ready:
#         st.warning("⚠️ Initialize system first!")
#         return
#
#     data_type = st.radio("Data Type", ["API Documentation", "Tutorials"])
#     count = st.slider("Number of Examples", 1, 5, 2)
#
#     if st.button("Generate Synthetic Data"):
#         with st.spinner(f"Generating {count} examples..."):
#             try:
#                 if data_type == "API Documentation":
#                     data = st.session_state.synth.generate_api_docs(count)
#                 else:
#                     data = st.session_state.synth.generate_tutorials(count)
#
#                 st.success(f"✅ Generated {len(data)} examples!")
#
#                 for i, item in enumerate(data, 1):
#                     with st.expander(f"Example {i} - {item.get('api_type', item.get('topic', 'Item'))}"):
#                         st.markdown(item['content'])
#
#                 total_len = sum(len(item['content']) for item in data)
#                 avg_len = total_len / len(data) if data else 0
#                 st.metric("Average Length", f"{avg_len:.0f} characters")
#             except Exception as e:
#                 st.error(f"Error: {e}")
#
#
# def main():
#     st.title("📚 Technical Documentation Assistant")
#     st.caption("🚀 INFO 7375 Prompt Engineering - Prof. Nik Bear Brown")
#
#     init()
#     sidebar()
#
#     tab1, tab2, tab3, tab4, tab5 = st.tabs([
#         "📝 Generate Docs",
#         "📊 Diagrams",
#         "📚 Knowledge Base",
#         "💻 Code Examples",
#         "🔄 Synthetic Data"
#     ])
#
#     with tab1:
#         tab_generate()
#     with tab2:
#         tab_diagrams()
#     with tab3:
#         tab_kb()
#     with tab4:
#         tab_code()
#     with tab5:
#         tab_synthetic()
#
#     st.markdown("---")
#     st.markdown("**Powered by:** Ollama (Local LLM) • Pure Python Vector Store • Matplotlib Diagrams • Streamlit")
#
#
# if __name__ == "__main__":
#     main()

import streamlit as st
from typing import List, Dict
import requests
import json
import random
from collections import defaultdict
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from io import BytesIO
import base64
from datetime import datetime


# ============================================================================
# CUSTOM CSS STYLING
# ============================================================================

def load_custom_css():
    st.markdown("""
    <style>
    /* Main background gradient */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2C3E50 0%, #34495E 100%);
    }

    /* Main title styling */
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 1rem;
    }

    .subtitle {
        font-size: 1.3rem;
        text-align: center;
        color: #ffffff;
        margin-bottom: 2rem;
        font-weight: 300;
    }

    /* Card styling */
    .info-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin: 1.5rem 0;
        color: #2c3e50 !important;
    }

    .info-card h4 {
        color: #2c3e50 !important;
        font-weight: 700;
    }

    .info-card p {
        color: #34495e !important;
        font-size: 1rem;
    }

    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }

    /* Section headers */
    .section-header {
        color: white;
        font-size: 2rem;
        font-weight: 700;
        margin: 2rem 0 1rem 0;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        border-left: 5px solid #66a6ff;
    }

    /* Button styling */
    .stButton>button {
        background: linear-gradient(120deg, #89f7fe 0%, #66a6ff 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(102, 166, 255, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)


# ============================================================================
# DIAGRAM GENERATOR (Simplified)
# ============================================================================

class DiagramGenerator:
    def __init__(self):
        plt.style.use('seaborn-v0_8-darkgrid')

    def generate_architecture_diagram(self, title: str = "System Architecture"):
        fig, ax = plt.subplots(figsize=(12, 8))
        fig.patch.set_facecolor('#f8f9fa')

        # Frontend
        frontend = patches.FancyBboxPatch((1, 6), 3, 1.5, boxstyle="round,pad=0.1",
                                          fill=True, facecolor='#667eea', edgecolor='#5568d3', linewidth=2)
        ax.add_patch(frontend)
        ax.text(2.5, 6.75, '🌐 Frontend', ha='center', fontsize=12, fontweight='bold', color='white')

        # API Gateway
        api = patches.FancyBboxPatch((6, 6), 3, 1.5, boxstyle="round,pad=0.1",
                                     fill=True, facecolor='#11998e', edgecolor='#0e8775', linewidth=2)
        ax.add_patch(api)
        ax.text(7.5, 6.75, '🚪 API Gateway', ha='center', fontsize=12, fontweight='bold', color='white')

        # Services
        services = [(2, 3.5, '🔐 Auth'), (5, 3.5, '💼 Logic'), (8, 3.5, '📊 Data')]
        for x, y, label in services:
            box = patches.FancyBboxPatch((x - 0.8, y - 0.5), 1.6, 1, boxstyle="round,pad=0.1",
                                         fill=True, facecolor='#ffa726', edgecolor='#333', linewidth=2)
            ax.add_patch(box)
            ax.text(x, y, label, ha='center', fontsize=10, fontweight='bold', color='white')

        # Database
        db = patches.FancyBboxPatch((4, 1), 4, 1, boxstyle="round,pad=0.1",
                                    fill=True, facecolor='#4ecdc4', edgecolor='#45b7af', linewidth=2)
        ax.add_patch(db)
        ax.text(6, 1.5, '🗄️ Database', ha='center', fontsize=12, fontweight='bold', color='white')

        # Arrows
        ax.annotate('', xy=(6, 6.75), xytext=(4, 6.75), arrowprops=dict(arrowstyle='->', lw=2, color='#333'))
        for x in [2, 5, 8]:
            ax.annotate('', xy=(x, 4.5), xytext=(7.5, 6), arrowprops=dict(arrowstyle='->', lw=1.5, color='#666'))
            ax.annotate('', xy=(6, 2), xytext=(x, 3), arrowprops=dict(arrowstyle='->', lw=1.5, color='#666'))

        ax.set_xlim(0, 11)
        ax.set_ylim(0, 8.5)
        ax.axis('off')
        ax.set_title(title, fontsize=16, fontweight='bold', color='#2c3e50')

        return self._fig_to_base64(fig)

    def generate_api_flow_diagram(self):
        fig, ax = plt.subplots(figsize=(12, 8))
        fig.patch.set_facecolor('#f8f9fa')

        # Client and Server
        client = patches.FancyBboxPatch((1, 6), 2, 1, boxstyle="round,pad=0.1",
                                        fill=True, facecolor='#667eea', edgecolor='#5568d3', linewidth=2)
        ax.add_patch(client)
        ax.text(2, 6.5, '👤 Client', ha='center', fontsize=12, fontweight='bold', color='white')

        server = patches.FancyBboxPatch((9, 6), 2, 1, boxstyle="round,pad=0.1",
                                        fill=True, facecolor='#11998e', edgecolor='#0e8775', linewidth=2)
        ax.add_patch(server)
        ax.text(10, 6.5, '🖥️ Server', ha='center', fontsize=12, fontweight='bold', color='white')

        # Timeline
        ax.plot([2, 2], [5.5, 1], 'k--', linewidth=1, alpha=0.3)
        ax.plot([10, 10], [5.5, 1], 'k--', linewidth=1, alpha=0.3)

        # Steps
        steps = [
            (6, 5, '1. HTTP Request', '#3498db'),
            (6, 4, '2. Authentication', '#e67e22'),
            (6, 3, '3. Process Data', '#9b59b6'),
            (6, 2, '4. Query DB', '#e74c3c'),
            (6, 1.5, '5. Response', '#27ae60'),
        ]

        for x, y, label, color in steps:
            ax.text(x, y, label, ha='center', fontsize=10, fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor=color, alpha=0.7, edgecolor='#333'))

        ax.annotate('', xy=(9, 6.3), xytext=(3, 6.3), arrowprops=dict(arrowstyle='->', lw=2, color='blue'))
        ax.annotate('', xy=(3, 6.7), xytext=(9, 6.7), arrowprops=dict(arrowstyle='->', lw=2, color='green'))

        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        ax.set_title('API Flow Diagram', fontsize=16, fontweight='bold', color='#2c3e50')

        return self._fig_to_base64(fig)

    def generate_data_structure_diagram(self, structure_type: str = "array"):
        fig, ax = plt.subplots(figsize=(12, 6))
        fig.patch.set_facecolor('#f8f9fa')

        if structure_type.lower() == "array":
            colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#4facfe', '#00f2fe']
            for i in range(6):
                rect = patches.Rectangle((i * 2 + 1, 3), 1.5, 1.5, fill=True,
                                         facecolor=colors[i], edgecolor='#333', linewidth=2)
                ax.add_patch(rect)
                ax.text(i * 2 + 1.75, 3.75, str(i * 10), fontsize=14, ha='center',
                        fontweight='bold', color='white')
                ax.text(i * 2 + 1.75, 2.5, f'[{i}]', fontsize=10, ha='center', color='#333')

            ax.text(6, 5.5, 'Array: O(1) Access', fontsize=14, ha='center', fontweight='bold')

        elif structure_type.lower() == "linked list":
            colors = ['#11998e', '#38ef7d', '#667eea', '#764ba2', '#f093fb']
            for i in range(5):
                circle = patches.Circle((i * 2.5 + 2, 3.5), 0.5, fill=True,
                                        facecolor=colors[i], edgecolor='#333', linewidth=2)
                ax.add_patch(circle)
                ax.text(i * 2.5 + 2, 3.5, str(i * 10), fontsize=12, ha='center',
                        fontweight='bold', color='white')

                if i < 4:
                    ax.arrow(i * 2.5 + 2.6, 3.5, 1.7, 0, head_width=0.2,
                             head_length=0.2, fc='#333', ec='#333')

            ax.text(6, 5, 'Linked List: O(1) Insert/Delete', fontsize=14,
                    ha='center', fontweight='bold')

        ax.set_xlim(0, 13)
        ax.set_ylim(0, 6)
        ax.axis('off')
        ax.set_title(f'{structure_type.title()} Structure', fontsize=16,
                     fontweight='bold', color='#2c3e50')

        return self._fig_to_base64(fig)

    def generate_workflow_diagram(self, steps: List[str]):
        fig, ax = plt.subplots(figsize=(10, len(steps) * 1.5 + 2))
        fig.patch.set_facecolor('#f8f9fa')

        y_start = len(steps) * 1.5
        colors = ['#667eea', '#11998e', '#f093fb', '#ffa726', '#42a5f5', '#66bb6a']

        for i, step in enumerate(steps):
            y = y_start - i * 1.5
            color = colors[i % len(colors)]

            box = patches.FancyBboxPatch((2, y - 0.4), 6, 0.8, boxstyle="round,pad=0.1",
                                         fill=True, facecolor=color, edgecolor='#333', linewidth=2)
            ax.add_patch(box)

            circle = patches.Circle((1.5, y), 0.3, fill=True, facecolor='#333', edgecolor='white', linewidth=2)
            ax.add_patch(circle)
            ax.text(1.5, y, str(i + 1), fontsize=10, ha='center', color='white', fontweight='bold')

            ax.text(5, y, step, ha='center', fontsize=11, fontweight='bold', color='white')

            if i < len(steps) - 1:
                ax.annotate('', xy=(5, y - 0.6), xytext=(5, y - 0.9),
                            arrowprops=dict(arrowstyle='->', lw=2, color='#333'))

        ax.set_xlim(0, 10)
        ax.set_ylim(y_start - len(steps) * 1.5 - 1, y_start + 1)
        ax.axis('off')
        ax.set_title('Process Workflow', fontsize=16, fontweight='bold', color='#2c3e50')

        return self._fig_to_base64(fig)

    def generate_comparison_diagram(self, items: List[Dict]):
        fig, ax = plt.subplots(figsize=(12, 8))
        fig.patch.set_facecolor('#f8f9fa')

        n_items = len(items)
        width = 8 / n_items
        colors = ['#667eea', '#11998e', '#f093fb', '#ffa726']

        for i, item in enumerate(items):
            x = i * (width + 1) + 2
            color = colors[i % len(colors)]

            box = patches.FancyBboxPatch((x, 2), width, 5, boxstyle="round,pad=0.1",
                                         fill=True, facecolor=color, edgecolor='#333', linewidth=2)
            ax.add_patch(box)

            ax.text(x + width / 2, 6.5, item['name'], ha='center', fontsize=12,
                    fontweight='bold', color='white')

            y_pos = 5.5
            for feature in item.get('features', []):
                ax.text(x + width / 2, y_pos, f'• {feature}', ha='center',
                        fontsize=9, color='white')
                y_pos -= 0.5

        ax.set_xlim(0, 12)
        ax.set_ylim(0, 8)
        ax.axis('off')
        ax.set_title('Feature Comparison', fontsize=16, fontweight='bold', color='#2c3e50')

        return self._fig_to_base64(fig)

    def _fig_to_base64(self, fig):
        buf = BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', dpi=150, facecolor=fig.get_facecolor())
        buf.seek(0)
        img_base64 = base64.b64encode(buf.read()).decode('utf-8')
        plt.close(fig)
        return img_base64


# ============================================================================
# OLLAMA API
# ============================================================================

def get_available_models() -> List[str]:
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=2)
        if response.status_code == 200:
            models = response.json().get('models', [])
            return [m['name'] for m in models]
    except:
        pass
    return []


def generate_with_ollama(prompt: str, model: str = "mistral", system: str = "") -> str:
    try:
        if len(prompt) > 500:
            prompt = prompt[:500] + "... (shortened for speed)"

        payload = {
            'model': model,
            'prompt': prompt,
            'stream': False,
            'options': {'temperature': 0.7, 'num_predict': 500, 'num_ctx': 2048}
        }
        if system:
            payload['system'] = system

        response = requests.post('http://localhost:11434/api/generate', json=payload, timeout=180)
        if response.status_code == 200:
            return response.json().get('response', '')
    except requests.exceptions.Timeout:
        return "⚠️ Generation timed out. Try a shorter prompt or simpler topic."
    except Exception as e:
        return f"Error: {str(e)}"
    return ""


def generate_embedding(text: str, model: str = "mistral") -> List[float]:
    try:
        response = requests.post('http://localhost:11434/api/embeddings',
                                 json={'model': model, 'prompt': text}, timeout=30)
        if response.status_code == 200:
            return response.json().get('embedding', [])
    except:
        pass
    return []


# ============================================================================
# SIMPLE VECTOR STORE
# ============================================================================

class SimpleVectorStore:
    def __init__(self):
        self.documents = []
        self.embeddings = []
        self.metadata = []

    def add_documents(self, docs: List[str], meta: List[Dict] = None, model: str = "mistral") -> int:
        count = 0
        for i, doc in enumerate(docs):
            chunks = self._chunk_text(doc)
            for j, chunk in enumerate(chunks):
                embedding = generate_embedding(chunk, model)
                if embedding:
                    self.documents.append(chunk)
                    self.embeddings.append(embedding)
                    doc_meta = {'doc_id': i, 'chunk_id': j}
                    if meta and i < len(meta):
                        doc_meta.update(meta[i])
                    self.metadata.append(doc_meta)
                    count += 1
        return count

    def search(self, query: str, n_results: int = 5, model: str = "mistral") -> List[tuple]:
        if not self.embeddings:
            return []
        query_embedding = generate_embedding(query, model)
        if not query_embedding:
            return []
        similarities = []
        for i, doc_embedding in enumerate(self.embeddings):
            sim = self._cosine_similarity(query_embedding, doc_embedding)
            similarities.append((sim, i))
        similarities.sort(reverse=True)
        results = []
        for sim, idx in similarities[:n_results]:
            results.append((self.documents[idx], sim, self.metadata[idx]))
        return results

    def _chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        paragraphs = text.split('\n\n')
        chunks = []
        current = []
        current_size = 0
        for para in paragraphs:
            if current_size + len(para) > chunk_size and current:
                chunks.append('\n\n'.join(current))
                current = []
                current_size = 0
            current.append(para)
            current_size += len(para)
        if current:
            chunks.append('\n\n'.join(current))
        return chunks

    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        if len(a) != len(b):
            return 0.0
        dot = sum(x * y for x, y in zip(a, b))
        norm_a = sum(x * x for x in a) ** 0.5
        norm_b = sum(x * x for x in b) ** 0.5
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return dot / (norm_a * norm_b)

    def get_context(self, query: str, n: int = 3, model: str = "mistral") -> str:
        results = self.search(query, n, model)
        context = []
        for i, (doc, score, meta) in enumerate(results, 1):
            context.append(f"[Source {i}] (Relevance: {score:.1%})")
            context.append(doc)
            context.append("")
        return '\n'.join(context)

    def clear(self):
        self.documents = []
        self.embeddings = []
        self.metadata = []

    def stats(self) -> Dict:
        return {'total_chunks': len(self.documents)}


# ============================================================================
# PROMPT ENGINEERING
# ============================================================================

class PromptTemplates:
    @staticmethod
    def research_prompt(topic: str, context: str = "") -> str:
        return f"""Research: {topic}
{f'Context: {context}' if context else ''}
Provide: key concepts, technical details, examples. Be concise."""

    @staticmethod
    def documentation_prompt(topic: str, research: str = "") -> str:
        return f"""Create documentation for: {topic}
{f'Based on: {research[:200]}' if research else ''}
Include: overview, explanation, code example, usage. Be concise."""

    @staticmethod
    def code_prompt(concept: str, language: str = "python") -> str:
        return f"""Write working {language} code for: {concept}
Include comments and example. Keep it simple and short."""


# ============================================================================
# DOCUMENTATION AGENT
# ============================================================================

class DocumentationAgent:
    def __init__(self, model: str = "mistral"):
        self.model = model
        self.templates = PromptTemplates()

    def create_documentation(self, topic: str, context: str = "", include_code: bool = True) -> str:
        research = generate_with_ollama(
            self.templates.research_prompt(topic, context),
            self.model, "You are a technical researcher"
        )
        doc = generate_with_ollama(
            self.templates.documentation_prompt(topic, research),
            self.model, "You are a technical writer"
        )
        if include_code:
            code = generate_with_ollama(
                self.templates.code_prompt(topic),
                self.model, "You are a code expert"
            )
            doc += f"\n\n## Code Example\n\n```python\n{code}\n```"
        return doc

    def generate_code(self, concept: str, languages: List[str]) -> Dict[str, str]:
        examples = {}
        for lang in languages:
            code = generate_with_ollama(
                self.templates.code_prompt(concept, lang),
                self.model, f"You are a {lang} expert"
            )
            examples[lang] = code
        return examples


# ============================================================================
# SYNTHETIC DATA GENERATOR
# ============================================================================

class SyntheticGenerator:
    def __init__(self, model: str = "mistral"):
        self.model = model

    def generate_api_docs(self, count: int = 3) -> List[Dict]:
        types = ['REST', 'GraphQL', 'gRPC']
        examples = []
        for _ in range(count):
            api_type = random.choice(types)
            prompt = f"""Generate realistic {api_type} API documentation with endpoints, parameters, examples. Markdown format."""
            result = generate_with_ollama(prompt, self.model)
            examples.append({'type': 'api', 'api_type': api_type, 'content': result})
        return examples

    def generate_tutorials(self, count: int = 3) -> List[Dict]:
        topics = ['Getting Started', 'Installation', 'Configuration']
        examples = []
        for topic in random.sample(topics, min(count, len(topics))):
            prompt = f"""Create tutorial: {topic}. Include intro, steps, examples, troubleshooting. Markdown."""
            result = generate_with_ollama(prompt, self.model)
            examples.append({'type': 'tutorial', 'topic': topic, 'content': result})
        return examples


# ============================================================================
# STREAMLIT UI
# ============================================================================

st.set_page_config(page_title="AI Documentation Assistant", page_icon="📚", layout="wide")
load_custom_css()


def init():
    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = SimpleVectorStore()
    if 'agent' not in st.session_state:
        st.session_state.agent = None
    if 'synth' not in st.session_state:
        st.session_state.synth = None
    if 'ready' not in st.session_state:
        st.session_state.ready = False
    if 'model' not in st.session_state:
        st.session_state.model = "mistral"
    if 'diagram_gen' not in st.session_state:
        st.session_state.diagram_gen = DiagramGenerator()
    if 'generation_count' not in st.session_state:
        st.session_state.generation_count = 0


def sidebar():
    with st.sidebar:
        st.markdown("# ⚙️ Configuration")
        st.markdown("---")

        models = get_available_models()

        if not models:
            st.error("❌ **Ollama Not Running!**")
            st.code("ollama serve\nollama pull mistral", language="bash")
            return

        st.success("✅ **Mistral Connected**")
        model = st.selectbox("🤖 Select Model", models)
        st.session_state.model = model

        st.markdown("---")

        if st.button("🚀 Initialize System", type="primary", use_container_width=True):
            with st.spinner("🔄 Initializing..."):
                st.session_state.agent = DocumentationAgent(model)
                st.session_state.synth = SyntheticGenerator(model)
                st.session_state.ready = True
                st.success("✅ Ready!")

        if st.session_state.ready:
            st.markdown("---")
            st.markdown("### 📊 Statistics")
            stats = st.session_state.vector_store.stats()
            col1, col2 = st.columns(2)
            with col1:
                st.metric("📚 Chunks", stats['total_chunks'])
            with col2:
                st.metric("🎯 Gens", st.session_state.generation_count)

        st.markdown("---")
        st.markdown("### ✨ Features")
        st.markdown("""
        <div class="feature-card">
        <b>🎯 Prompt Engineering</b><br>
        Systematic templates
        </div>
        <div class="feature-card">
        <b>🔍 RAG System</b><br>
        Vector search
        </div>
        <div class="feature-card">
        <b>🎨 Multimodal</b><br>
        Text + Code + Diagrams
        </div>
        <div class="feature-card">
        <b>🔄 Synthetic Data</b><br>
        AI-generated examples
        </div>
        """, unsafe_allow_html=True)


def tab_generate():
    st.markdown('<h2 class="section-header">📝 Documentation Generator</h2>', unsafe_allow_html=True)

    if not st.session_state.ready:
        st.warning("⚠️ **Initialize System First!**")
        return

    st.markdown("""
    <div class="info-card">
    <h4>🎯 Create Professional Documentation</h4>
    <p>Generate comprehensive technical documentation with AI assistance.</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        topic = st.text_input("📌 Topic", placeholder="e.g., JWT Authentication, Docker")
        context = st.text_area("📋 Context (Optional)", height=100)

    with col2:
        st.markdown("##### 🎛️ Options")
        include_code = st.checkbox("💻 Code Examples", value=True)
        use_rag = st.checkbox("🔍 Use RAG", value=True)
        include_diagram = st.checkbox("📊 Diagram", value=True)

    if st.button("✨ Generate", disabled=not topic, type="primary", use_container_width=True):
        with st.spinner("🔄 Generating..."):
            try:
                full_context = context
                if use_rag:
                    rag_context = st.session_state.vector_store.get_context(topic, 3, st.session_state.model)
                    full_context = f"{context}\n\n{rag_context}"

                doc = st.session_state.agent.create_documentation(topic, full_context, include_code)
                st.session_state.generation_count += 1

                st.success("✅ **Generated!**")

                if include_diagram:
                    st.markdown("### 📊 Architecture")
                    diagram = st.session_state.diagram_gen.generate_architecture_diagram(topic)
                    st.markdown(
                        f'<img src="data:image/png;base64,{diagram}" style="max-width:100%; border-radius:10px;"/>',
                        unsafe_allow_html=True)
                    st.markdown("---")

                st.markdown("### 📄 Documentation")
                st.markdown(doc)

                st.download_button("📥 Download", doc, f"{topic.replace(' ', '_')}.md")

            except Exception as e:
                st.error(f"❌ **Error:** {e}")


def tab_diagrams():
    st.markdown('<h2 class="section-header">📊 Diagram Generator</h2>', unsafe_allow_html=True)

    if not st.session_state.ready:
        st.warning("⚠️ **Initialize First!**")
        return

    diagram_type = st.selectbox("📋 Type",
                                ["System Architecture", "API Flow", "Data Structure", "Process Workflow",
                                 "Feature Comparison"])

    if diagram_type == "System Architecture":
        title = st.text_input("🏗️ System Name", "My System")
        if st.button("🎨 Generate", type="primary", use_container_width=True):
            with st.spinner("Creating..."):
                diagram = st.session_state.diagram_gen.generate_architecture_diagram(title)
                st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
                            unsafe_allow_html=True)

    elif diagram_type == "API Flow":
        if st.button("🎨 Generate", type="primary", use_container_width=True):
            with st.spinner("Creating..."):
                diagram = st.session_state.diagram_gen.generate_api_flow_diagram()
                st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
                            unsafe_allow_html=True)

    elif diagram_type == "Data Structure":
        structure = st.selectbox("Type", ["Array", "Linked List"])
        if st.button("🎨 Generate", type="primary", use_container_width=True):
            with st.spinner("Creating..."):
                diagram = st.session_state.diagram_gen.generate_data_structure_diagram(structure)
                st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
                            unsafe_allow_html=True)

    elif diagram_type == "Process Workflow":
        steps_text = st.text_area("Steps (one per line)",
                                  "Initialize\nAuthenticate\nProcess\nValidate\nRespond", height=150)
        if st.button("🎨 Generate", type="primary", use_container_width=True):
            steps = [s.strip() for s in steps_text.split('\n') if s.strip()]
            with st.spinner("Creating..."):
                diagram = st.session_state.diagram_gen.generate_workflow_diagram(steps)
                st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
                            unsafe_allow_html=True)

    elif diagram_type == "Feature Comparison":
        col1, col2 = st.columns(2)
        with col1:
            item1_name = st.text_input("Option A", "Solution A")
            item1_features = st.text_area("Features", "Fast\nScalable\nCheap", key="f1")
        with col2:
            item2_name = st.text_input("Option B", "Solution B")
            item2_features = st.text_area("Features", "Secure\nReliable\nEasy", key="f2")

        if st.button("🎨 Generate", type="primary", use_container_width=True):
            items = [
                {'name': item1_name, 'features': [f.strip() for f in item1_features.split('\n') if f.strip()]},
                {'name': item2_name, 'features': [f.strip() for f in item2_features.split('\n') if f.strip()]}
            ]
            with st.spinner("Creating..."):
                diagram = st.session_state.diagram_gen.generate_comparison_diagram(items)
                st.markdown(f'<img src="data:image/png;base64,{diagram}" style="max-width:100%;"/>',
                            unsafe_allow_html=True)


def tab_kb():
    st.markdown('<h2 class="section-header">📚 Knowledge Base</h2>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📤 Upload", "🔍 Search"])

    with tab1:
        files = st.file_uploader("Upload files", type=['txt', 'md'], accept_multiple_files=True)
        if files and st.button("📤 Add to KB", type="primary"):
            with st.spinner("Processing..."):
                docs = []
                meta = []
                for f in files:
                    content = f.read().decode('utf-8')
                    docs.append(content)
                    meta.append({'filename': f.name})
                chunks = st.session_state.vector_store.add_documents(docs, meta, st.session_state.model)
                st.success(f"✅ Added {chunks} chunks")

    with tab2:
        query = st.text_input("Search query")
        if query and st.button("🔍 Search"):
            with st.spinner("Searching..."):
                results = st.session_state.vector_store.search(query, 5, st.session_state.model)
                if results:
                    for i, (doc, score, meta) in enumerate(results, 1):
                        with st.expander(f"Result {i} - {score:.1%}"):
                            st.markdown(f"**File:** {meta.get('filename', 'Unknown')}")
                            st.markdown(doc)
                else:
                    st.info("No results")


def tab_code():
    st.markdown('<h2 class="section-header">💻 Code Generator</h2>', unsafe_allow_html=True)

    if not st.session_state.ready:
        st.warning("⚠️ **Initialize First!**")
        return

    concept = st.text_input("Concept", placeholder="e.g., Binary Search Tree")
    langs = st.multiselect("Languages", ["Python", "JavaScript", "Java", "Go"], ["Python"])

    if st.button("Generate Code", disabled=not concept or not langs, type="primary"):
        with st.spinner("Generating..."):
            try:
                examples = st.session_state.agent.generate_code(concept, langs)
                for lang, code in examples.items():
                    st.subheader(f"{lang}")
                    st.code(code, language=lang.lower())
            except Exception as e:
                st.error(f"Error: {e}")


def tab_synthetic():
    st.markdown('<h2 class="section-header">🔄 Synthetic Data</h2>', unsafe_allow_html=True)

    if not st.session_state.ready:
        st.warning("⚠️ **Initialize First!**")
        return

    data_type = st.radio("Type", ["API Documentation", "Tutorials"])
    count = st.slider("Count", 1, 5, 2)

    if st.button("Generate", type="primary"):
        with st.spinner(f"Generating {count} examples..."):
            try:
                if data_type == "API Documentation":
                    data = st.session_state.synth.generate_api_docs(count)
                else:
                    data = st.session_state.synth.generate_tutorials(count)

                st.success(f"✅ Generated {len(data)} examples!")

                for i, item in enumerate(data, 1):
                    with st.expander(f"Example {i} - {item.get('api_type', item.get('topic', 'Item'))}"):
                        st.markdown(item['content'])
            except Exception as e:
                st.error(f"Error: {e}")


def main():
    st.markdown('<h1 class="main-title">📚 AI Documentation Assistant</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">🚀 Advanced AI-Powered Documentation Generation System</p>',
                unsafe_allow_html=True)

    init()
    sidebar()

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Generate Docs", "📊 Diagrams", "📚 Knowledge Base",
        "💻 Code Examples", "🔄 Synthetic Data"
    ])

    with tab1:
        tab_generate()
    with tab2:
        tab_diagrams()
    with tab3:
        tab_kb()
    with tab4:
        tab_code()
    with tab5:
        tab_synthetic()

    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: white; padding: 2rem;">
    <b>Powered by:</b> Ollama (Local LLM) • Python Vector Store • Matplotlib • Streamlit<br>
    <small>AI Documentation Assistant v1.0.0 | INFO 7375 Prompt Engineering</small>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()