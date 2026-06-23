class APIConfig:
    def __init__(self,api_key,model,max_tokens=500):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens

# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key","GPT-5",max_tokens=1000)
prod_config = APIConfig("Ref-api-key","GPT-172.16.5",max_tokens=50)

print(dev_config.model)
print(prod_config.model)
print(prod_config.max_tokens)
