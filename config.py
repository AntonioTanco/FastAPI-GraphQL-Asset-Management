import yaml

#Opens the config.yml file
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

# Now you can access your variables like this:
mongodb_collection = cfg['mongodb']['collection_name']
redis_url = cfg['redis']['url']
redis_port = cfg['redis']['port']
logger_name = cfg['logger']['name']
logger_file = cfg['logger']['file']