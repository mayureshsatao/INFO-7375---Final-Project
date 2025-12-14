#!/bin/bash

echo "======================================"
echo "Technical Documentation Assistant"
echo "Fast Setup Script"
echo "======================================"
echo ""

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing Python dependencies..."
echo "This may take 3-5 minutes..."
pip install crewai==0.28.8
pip install streamlit==1.29.0
pip install chromadb==0.4.22
pip install sentence-transformers==2.2.2
pip install langchain==0.1.0
pip install langchain-community==0.0.10
pip install ollama==0.1.6
pip install pypdf==3.17.4
pip install python-docx==1.1.0
pip install markdown==3.5.1
pip install Pillow==10.1.0
pip install faiss-cpu==1.7.4
pip install numpy==1.24.3
pip install pandas==2.0.3

echo ""
echo "======================================"
echo "Dependencies installed successfully!"
echo "======================================"
echo ""

# Check if Ollama is installed
echo "Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    echo "✅ Ollama is installed"

    # Check available models
    echo ""
    echo "Available Ollama models:"
    ollama list

    # Check if mistral is available
    if ollama list | grep -q "mistral"; then
        echo "✅ Mistral model found"
    else
        echo ""
        echo "⚠️  Mistral model not found"
        echo "Pulling Mistral model (this will take a few minutes)..."
        ollama pull mistral
    fi
else
    echo "❌ Ollama not found"
    echo ""
    echo "Please install Ollama:"
    echo "  Linux/Mac: curl https://ollama.ai/install.sh | sh"
    echo "  Windows: Download from https://ollama.ai/download"
    echo ""
    echo "After installing, run: ollama pull mistral"
fi

echo ""
echo "======================================"
echo "Setup Complete!"
echo "======================================"
echo ""
echo "To start the application:"
echo "  1. Activate virtual environment:"
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    echo "     venv\\Scripts\\activate"
else
    echo "     source venv/bin/activate"
fi
echo "  2. Run the app:"
echo "     streamlit run app.py"
echo ""
echo "The app will open in your browser at http://localhost:8501"
echo ""