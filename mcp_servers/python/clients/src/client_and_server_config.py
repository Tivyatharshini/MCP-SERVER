ClientsConfig =[
    "MCP_CLIENT_AZURE_AI",
    "MCP_CLIENT_OPENAI",
	"MCP_CLIENT_GEMINI"
]
ServersConfig = [
	{
		"server_name": "MCP-GSUITE",
		"command":"uv",
		"args": [
			"--directory",
			"../servers/MCP-GSUITE/mcp-gsuite",
			"run",
			"mcp-gsuite"
		]
	}
 ,
    {
		"server_name":"MCP-WIKIDATA",
        "command":"python",
        "args": [
            "../servers/MCP-WIKIDATA/mcp-wikidata/src/server.py"
        ]
	},
    {
		"server_name":"MCP-PORTAINER",
		"command":"python",
		"args": [
			"../servers/MCP-PORTAINER/src/server.py"
		]
	},
    {
		"server_name":"MCP-FARGATE",
		"command":"python",
		"args": [
			"../servers/MCP-FARGATE/mcp-server-with-fargate/src/mcp_fargate_server.py"
		]
	}
 
]