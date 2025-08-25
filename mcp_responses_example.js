const fetch = require('node-fetch');

async function callModel(message) {
  const apiKey = process.env.OPENAI_API_KEY;
  if (!apiKey) {
    throw new Error('Missing OPENAI_API_KEY environment variable');
  }

  const body = {
    model: "gpt-4o", // adjust to the model you have access to
    tools: [
      {
        type: "mcp",
        server_label: "my-mcp",
        server_url: "https://mcp-server-z6rm.onrender.com",
        require_approval: "never"
      }
    ],
    input: message
  };

  const res = await fetch("https://api.openai.com/v1/responses", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${apiKey}`
    },
    body: JSON.stringify(body)
  });

  const data = await res.json();
  console.log(JSON.stringify(data, null, 2));
}

// Example usage
callModel("Hello, use my MCP server to perform a search.").catch(err => {
  console.error(err);
});
