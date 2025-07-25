Quickstart Guide
===============

This guide will help you get started with the agent-template-repo API quickly.

Installation
-----------

1. Clone the repository:
   .. code-block:: bash
   
      git clone <repository-url>
      cd agent-template-repo

2. Install dependencies:
   .. code-block:: bash
   
      uv sync
      # or install with all optional dependencies
      uv pip install ".[all]"

3. Set up environment variables:
   .. code-block:: bash
   
      export OPENAI_API_KEY="your-openai-api-key"
      export VERBOSE=true

Running the API
--------------

Start the FastAPI server:

.. code-block:: bash

   make dev

The API will be available at `http://localhost:8000`

API Documentation
----------------

Once running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

Basic Usage
----------

Health Check
~~~~~~~~~~~

Check if the API is running:

.. code-block:: bash

   curl http://localhost:8000/health

Response:
.. code-block:: json

   {"status": "healthy"}

Search Endpoint
~~~~~~~~~~~~~~

Perform a search using the search agent:

.. code-block:: bash

   curl -X POST "http://localhost:8000/api/v1/search" \
        -H "Content-Type: application/json" \
        -d '{"query": "What is machine learning?", "max_results": 5}'

Response:
.. code-block:: json

   {
     "result": "Machine learning is a subset of artificial intelligence...",
     "query": "What is machine learning?"
   }

Search Health Check
~~~~~~~~~~~~~~~~~~

Check the search service health:

.. code-block:: bash

   curl http://localhost:8000/api/v1/search/health

Response:
.. code-block:: json

   {"status": "search service healthy"}

Python Client Example
--------------------

.. code-block:: python

   import requests
   
   # Base URL
   base_url = "http://localhost:8000"
   
   # Health check
   response = requests.get(f"{base_url}/health")
   print(response.json())
   
   # Search
   search_data = {
       "query": "Explain neural networks",
       "max_results": 10
   }
   response = requests.post(f"{base_url}/api/v1/search", json=search_data)
   result = response.json()
   print(f"Search result: {result['result']}")

Configuration
------------

The application uses the following configuration options:

- ``OPENAI_API_KEY``: Your OpenAI API key (required)
- ``VERBOSE``: Enable verbose logging (default: false)

Environment Variables
~~~~~~~~~~~~~~~~~~~

You can set these via environment variables or create a `.env` file:

.. code-block:: bash

   OPENAI_API_KEY=your-api-key-here
   VERBOSE=true

Development
----------

Running Tests
~~~~~~~~~~~~

.. code-block:: bash

   pytest

Building Documentation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd docs
   make html

The documentation will be available in `docs/build/html/`

Next Steps
----------

- Explore the :doc:`API documentation <api/index>` for detailed endpoint information
- Check out the :doc:`Agents documentation <agents/index>` to understand the agent architecture
- Review the source code in the `app/` directory for implementation details 